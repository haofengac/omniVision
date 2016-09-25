from firebase import firebase as fb

class Firebase:
    def __init__(self):
        auth = fb.FirebaseAuthentication('hLayIOoCcxdSMSVoN5TaN8yLX97lfRlDqsFsptLo', 'bhpfelix@gmail.com')
        self.firebase = fb.FirebaseApplication('https://omnivision-a2b18.firebaseio.com', authentication=auth)

    def create_message(self):
        return {}

    def get_messages(self):
        return self.firebase.get('/messages', name=None, connection=None, params={'print': 'pretty'})

    def send_message(self, url, image_id='666666', time=''):
        return self.firebase.post('/messages', {'imageUrl': url, 'id': image_id, 'time': time, 'name': 'User1'})
