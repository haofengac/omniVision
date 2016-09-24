from firebase import firebase as fb

auth = fb.FirebaseAuthentication('hLayIOoCcxdSMSVoN5TaN8yLX97lfRlDqsFsptLo', 'bhpfelix@gmail.com')

firebase = fb.FirebaseApplication('https://omnivision-a2b18.firebaseio.com', authentication=auth)

result = firebase.get('/messages', name=None, connection=None, params={'print': 'pretty'})

print result

print help(firebase)

result = firebase.post('/messages', {'imageUrl': 'https://www.dropbox.com/s/lfgklsbgtj7ns7b/0a3cba.jpg?raw=1', 'name': 'bhp'})

print result