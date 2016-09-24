#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox

class TransferData:
    def __init__(self):
        self.access_token = 'rDTXhwIRvIAAAAAAAAAACA04mgp3sK5gF05qTBk3KtbgMyScHMgfeLen1b_BLkde'
        self.dbx = dropbox.Dropbox(self.access_token)
        self.client = dropbox.client.DropboxClient(self.access_token)

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """

        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f, file_to)

        return self.client.share(file_to, short_url=False)