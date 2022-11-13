import sys
import os
import json
from telethon import sync, TelegramClient, events
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import traceback
import logging

formatter = logging.Formatter()
logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

def get_member_by_group_username(client, group_username):

	"""
	:param client: TelegramClient
	:param group_username: username's group
	:return: list telethon.tl.types.User
  
	Get all member of group by group username
	"""
	all_data = [] # list telethon.tl.types.User
	
	entity = client.get_entity(group_username)
	limit = 200
	my_filter = ChannelParticipantsSearch('')

	i = 0
	while True:
		offset = limit * i
		user_list = client(GetParticipantsRequest(entity, my_filter, offset=offset, limit=limit, hash=0))

		if not user_list.users:
			logging.info('get member done')
			break
		
		all_data.extend(user_list.users)

		i += 1

	return all_data
	

def get_member_by_group_id(client, group_id):

	"""
	:param client: TelegramClient
	:param group_username: id's group
	:return: list telethon.tl.types.User
  
	Get all member of group by group id
	"""

	entity = client.get_entity(group_id)
	return client.get_participants(entity=entity)

def add_member_to_group(client, group_entity, user):

	"""
	:param client: TelegramClient
	:param group_entity: entity group
	:param user: InputPeerUser
	:return: string - SUCCESS, FLOOD, FLOOD_WAIT, USER_PRIVACY, ERROR_OTHER
  
	add one member to group
	"""
	
	result = 'SUCCESS'
	try:
		client(InviteToChannelRequest(
			group_entity,
			[user]
		))
	except PeerFloodError as e:
		logging.error("Error PeerFloodError")
		traceback.print_exc()
		result = 'FLOOD'
	except FloodWaitError as e:
		logging.error("Error FloodWaitError")
		traceback.print_exc()
		result = 'FLOOD_WAIT'
	except UserPrivacyRestrictedError:
		logging.error("Error UserPrivacyRestrictedError")
		result = 'USER_PRIVACY'
	except BaseException:
		logging.error("Error other")
		traceback.print_exc()
		result = 'ERROR_OTHER'

	return result

def update_count(path, current_index):
	with open(path, 'w') as g:
		g.write(str(current_index))
		g.close()

def add_multiple_member_to_group(client, group_entity, users):

	"""
	:param client: TelegramClient
	:param group_entity: entity group
	:param user: InputPeerUser
	:return: string - SUCCESS, FLOOD, FLOOD_WAIT, USER_PRIVACY, ERROR_OTHER
  
	add one member to group
	"""
	
	result = 'SUCCESS'
	try:
		client(InviteToChannelRequest(
			group_entity,
			users
		))
	except PeerFloodError as e:
		logging.error("Error PeerFloodError")
		traceback.print_exc()
		result = 'FLOOD'
	except FloodWaitError as e:
		logging.error("Error FloodWaitError")
		traceback.print_exc()
		result = 'FLOOD_WAIT'
	except UserPrivacyRestrictedError:
		logging.error("Error UserPrivacyRestrictedError")
		result = 'USER_PRIVACY'
	except BaseException:
		logging.error("Error other")
		traceback.print_exc()
		result = 'ERROR_OTHER'

	return result

def update_count(path, current_index):
	with open(path, 'w') as g:
		g.write(str(current_index))
		g.close()