import Vue from 'vue'
import VueFire from 'vuefire'
import Firebase from 'firebase'

Vue.use(VueFire)

const firebaseApp = Firebase.initializeApp({
    apiKey: 'AIzaSyBZO7hNeIAAKSwlTD7iNByGbd6zgzn4dKU',
    authDomain: 'beerhacks-87b75.firebaseapp.com',
    databaseURL: 'https://beerhacks-87b75.firebaseio.com',
    storageBucket: 'beerhacks-87b75.appspot.com'
})

const database = firebaseApp.database()
const firebaseAuth = firebaseApp.auth()
const storage = firebaseApp.storage().ref()

export { database, firebaseAuth, storage }
