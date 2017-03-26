#!/usr/bin/env python3.4

import pyrebase

db = None

def startFireBase(apiKey, authDomain, databaseURL, storageBucket):
    config = {
        "apiKey": apiKey,
        "authDomain": authDomain,
        "databaseURL": databaseURL,
        "storageBucket": storageBucket,
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

def sendData(data):
  db.child("data").child("fridge1").set(data)
