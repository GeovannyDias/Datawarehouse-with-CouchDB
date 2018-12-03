#import nombreArchivo  => importa modulos de otro archivo python
#from direcctorio import nombreArchivo  => importa modulos dentro de otro direcctorio
#que contiene un archivo python // pero tambien crear un archivo __init__.py para que leea archivo
import csv, json
import couchdb

csvFilePath = "catsvdogs.csv"
jsonFilePath = "prueba1.json"

db = None
#========================================================================
#Conexión CouchDB
#========================================================================
url = "http://geo:geo@localhost:5984/"
db = "mascotas_2"
couch = couchdb.Server(url)

if db in couch:
        db = couch['mascotas_2']       
        print("Existing Data Base")
else:
        db = couch.create('mascotas_2')
        print("Creating Data Base")

#========================================================================
#========================================================================
data = {}
#Leer archivo CSV y agregar datos al Diccionario
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        print("llega")
        print(json.dumps(csvRow)) #Solo agregar a CouchDB // db.save(csvRow)
        db.save(csvRow)
        #nombre = csvRow['nombre']
        #data[nombre] = csvRow


#print("")
#print (data)

#Escribir datos del diccionario a un archivo JSON
#with open(jsonFilePath, "w") as jsonFile:
#    jsonFile.write(json.dumps(data, indent=4))



