import couchdb #Libreria de CouchDB (requiere ser instalada primero)
from tweepy import Stream #tweepy es la libreria que trae tweets desde la API de Twitter (requiere ser instalada primero)
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json #Libreria para manejar archivos JSON


###Credenciales de la cuenta de Twitter########################
#Poner aqui las credenciales de su cuenta privada, caso contrario la API bloqueara esta cuenta de ejemplo
ckey = "m4Fq2Pr4yHn1YLLg6nmPYxXYz"
csecret = "0WC0ZlD9sT4aMiBY5xDrRjFIQqT3KbU8oSaNEsFEkKPHZCASe4"
atoken = "999027411613356032-NvGF9YveYjVjQq4sf61x5IbFDe0KBej"
asecret = "ZHTEn2rxBoKLIkFa57Ksm3Hs4jYtwimhgYcsq8TtAXVXv"
#####################################
i = 1
class listener(StreamListener):    
    def on_data(self, data):
        global i
        dictTweet = json.loads(data)
        try:            
            dictTweet["_id"] = str(dictTweet['id'])
            #Antes de guardar el documento puedes realizar parseo, limpieza y cierto analisis o filtrado de datos previo
            #a guardar el documento en la base de datos
            doc = db.save(dictTweet) #Aqui se guarda el tweet en la base de couchDB
            print (str(i) + ". Guardado " + "=> " + dictTweet["_id"])
            i += 1
        except:
            print (i +". Documento ya existe")
            i += 1
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#Setear la URL del servidor de couchDB
server = couchdb.Server('http://geo:geo@localhost:5984/')#add user and pass
try:
    #Si no existe la Base de datos la crea
    db = server.create('quito')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['quito']
    
#Aqui se define el bounding box con los limites geograficos donde recolectar los tweets
twitterStream.filter(track=["quito","ecuador","metro","accidentes"]) #referencias a buscar
#twitterStream.filter(locations=[-78.509669,-0.114833,-78.488211,-0.101272]) #recoge toda informacion por coodenadas

#http://boundingbox.klokantech.com/
