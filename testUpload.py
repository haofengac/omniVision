from upload import TransferData

transferData = TransferData()

file_from = 'Documents/omniVision.png' # local relative path for the file
file_to = '/omniVision.png'  # The full path on Dropbox to upload the file to, including the file name

# API v2

# upload files
print transferData.upload_file(file_from, file_to)
# get file time stamp
print transferData.get_file_meta(file_to)