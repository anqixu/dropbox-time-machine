#!/usr/bin/env python3

# See v2 tutorial and docs: https://www.dropbox.com/developers/documentation/python#tutorial

import dropbox
import os
import sys

import settings
app_key = settings.APP_KEY
app_secret = settings.APP_SECRET

dbx = dropbox.Dropbox(settings.SECRET_KEY)
#print('get_current_account:', dbx.users_get_current_account())

deleted_count = 0
for entry in dbx.files_list_folder(path='/SCRIPTS/', recursive=True, include_deleted=True).entries:
  if isinstance(entry, dropbox.files.DeletedMetadata):
    if entry.name.find('conflicted copy') >= 0:
      continue
    if entry.name[-1] == '~':
      continue
    if entry.name == 'untitled document' or entry.name == 'new text document.txt':
      continue
    _, ext = os.path.splitext(entry.name)
    if ext == '.pyc':
      continue
    print(entry.path_display)
    deleted_count += 1
sys.stderr.write('Total deleted files found: %d\n' % deleted_count)
