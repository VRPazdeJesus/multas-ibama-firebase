import pyrebase

config = {
    "apiKey": "AIzaSyADvetnTG1aUvqmZuV5yQphJm1enwIMaYI",
    "authDomain": "python-firebase-45b33.firebaseapp.com",
    "databaseURL": "https://python-firebase-45b33.firebaseio.com",
    "projectId": "python-firebase-45b33",
    "storageBucket": "python-firebase-45b33.appspot.com",
    "messagingSenderId": "85688199834"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class BancoDeDados():
    @staticmethod
    def salvar_firebase(lista, nome):
        contador = 0
        for elemento in lista:
            print("Salvando multa", contador)
            db.child(nome).child("multa{}".format(contador)).set(elemento)
            contador = contador + 1
            
    @staticmethod
    def atualizar(table, child, data):
        db.child(table).child(child).update(data)
    
    @staticmethod
    def remover(table, child):
        db.child(table).child(child).remove()

