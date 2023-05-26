from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb+srv://admin:admin@mimongodbhelbert.iohwb3r.mongodb.net/')
db = client['Flaskql']
collectionGrades = db['grades']
