from firebase import firebase as fb
auth = fb.FirebaseAuthentication('hLayIOoCcxdSMSVoN5TaN8yLX97lfRlDqsFsptLo', 'bhpfelix@gmail.com')
# , auth_payload={'uid': 'rgYuTjBxZ6cTjUUM35YVxcO6CYb2'}
# NB renamed extras -> auth_payload, id -> uid here
firebase = fb.FirebaseApplication('https://omnivision-a2b18.firebaseio.com', authentication=auth)
result = firebase.get('/messages', name=None, connection=None,
                      params={'print': 'pretty'})
# HTTPError: 401 Client Error: Unauthorized
print result

new_user = 'Ozgur Vatansever'

result = firebase.post('/users', new_user)
print result