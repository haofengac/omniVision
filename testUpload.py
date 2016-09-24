from upload import TransferData
import urllib2
from os import listdir, remove
from os.path import isfile, join
from time import sleep

# macros for the script
image_dir = 'data'
dropbox_dir = '/omniVision'
loop_frequency = 0.5
remove_uploaded_file = True

while True:

    # read file names from the directory
    files = [f for f in listdir(image_dir) if isfile(join(image_dir, f)) and not f.startswith('.')]
    print files

    # initiate data transfer with dropbox
    transferData = TransferData()

    # API v2
    # upload files
    for fn in files:
        transferData.upload_file(join(image_dir, fn), join(dropbox_dir, fn))
        print "Successfully uploaded " + fn

        print " Deleting file..."
        if remove_uploaded_file:
            remove(join(image_dir, fn))

    sleep(loop_frequency)
