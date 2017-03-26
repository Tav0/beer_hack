#!/usr/bin/env python3.4

import pyrebase

config = {
    "apiKey": "apiKey",
    "authDomain": "project-id.firebaseapp.com",
    "databaseURL": "https://project-id.firebaseio.com",
    "storageBucket": "project-id.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {"first": "test1", "second": "test2"}
db.child("data").child("thermo").set(data)
