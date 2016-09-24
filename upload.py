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

    def get_file_time(self, fn):
        return self.dbx.files_get_metadata(fn).server_modified

    def get_file_url(self, fn):
        meta = self.client.share(fn, short_url=False)
        return meta['url'][:meta['url'].rfind('?')+1] + 'raw=1'

    def list_all_files(self, drct):
        metadata = self.client.metadata(drct)
        return [content['path'].split('/')[-1] for content in metadata['contents']]

