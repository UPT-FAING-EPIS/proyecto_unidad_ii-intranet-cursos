from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Flaskql']
collectionGrades = db['grades']
