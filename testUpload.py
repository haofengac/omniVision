from upload import TransferData

from firebase_send import Firebase

import urllib2
from os import listdir, remove
from os.path import isfile, join
from time import sleep

# macros for the script
image_dir = 'data'
dropbox_dir = '/omniVision'
loop_frequency = 0.5
remove_uploaded_file = True

# initialize data transfer with dropbox
transferData = TransferData()
# initialize Firebase connection
firebase = Firebase()
# Initialize send array
url_array = []

while True:
    # read file names from the directory
    files = [f for f in listdir(image_dir) if isfile(join(image_dir, f)) and not f.startswith('.')]

    # API v2
    # upload files
    for fn in files:
        lcl_path = join(image_dir, fn)
        dpx_path = join(dropbox_dir, fn)

        # upload image to dropbox
        transferData.upload_file(lcl_path, dpx_path)
        print "Successfully uploaded " + fn

        # delete file from local memory
        print " Deleting file..."
        if remove_uploaded_file:
            remove(lcl_path)

        # get file image and send to firebase app
        print "Sending image data to firebase app"
        url = transferData.get_file_url(dpx_path)
        firebase.send_message(url, fn[6:], transferData.get_file_time(dpx_path))

    sleep(loop_frequency)