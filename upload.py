#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)
        self.client = dropbox.client.DropboxClient(self.access_token)

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """

        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f, file_to)

        return self.client.share('/omniVision.png', short_url=False)

def main():
    access_token = 'rDTXhwIRvIAAAAAAAAAACA04mgp3sK5gF05qTBk3KtbgMyScHMgfeLen1b_BLkde'
    transferData = TransferData(access_token)

    file_from = 'omniVision.png'
    file_to = '/omniVision.png'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()