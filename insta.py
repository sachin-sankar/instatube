from helpers import log
from rich.pretty import pprint as print
from rich.traceback import install
from rich.progress import track
from instagrapi import Client
from json import load,dump

install(show_locals=True)
cl = Client()

def getCreators():
  try:
    with open('creators.txt','rt') as file:
      creatorsNameList = file.read().split('\n')
  except FileNotFoundError:
    log.error('Creators name list file not found.')
    return
  # Check creators data file if not create one
  try:
    with open('creators.json','r') as file:
      creators = load(file)
  except FileNotFoundError:
    log.info('Creators data file not found. Creating one')
    creators = {}
    for creator in track(creatorsNameList,description='Getting Creator Id'):
      try:
        creators[creator] = cl.user_id_from_username(creator)
      except:
        log.exception('Exception when getting creator id')
    with open('creators.json','w') as file:
      dump(creators,file)
      log.info('Wrote creators data file')
  # Update creators data if new creator
  if len(creatorsNameList) > len(creators):
    log.info('Updating creators data for new creator')
    newCreators = []
    for creator in track(creatorsNameList,description='Finding New creators'):
      if creator not in creators:
        newCreators.append(creator)
    for creator in track(newCreators,description='Getting Creator Id'):
      try:
        creators[creator] = cl.user_id_from_username(creator)
      except:
        log.exception('Exception when getting creator id')
    with open('creators.json','w') as file:
      dump(creators,file)
      log.info('Updated creators data file')
  return creators
    
  