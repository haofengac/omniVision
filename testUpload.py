from upload import TransferData
import urllib2

transferData = TransferData()

file_from = 'omniVision/images/log.png' # local relative path for the file
file_to = '/omniVision.png'  # The full path on Dropbox to upload the file to, including the file name

# API v2

# upload files
transferData.upload_file(file_from, file_to)
# get file time stamp
time = transferData.get_file_time(file_to)

url = transferData.get_file_url(file_to)

response = urllib2.urlopen(url)
page_source = response.read()

print page_source

