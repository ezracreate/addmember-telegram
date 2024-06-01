import os
import time
import random
from pyrogram import Client
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.errors import PeerFlood
from pyrogram.errors import UserPrivacyRestricted
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserChannelsTooMuch
from pyrogram.errors import UserBannedInChannel
from pyrogram.errors import RPCError
import time
import csv
from csv import reader
from colorama import Fore, Style, init
import colorama
colorama.init(autoreset=True)
from telethon import utils
from licensing.models import *
scam = '@notoscam'
init()

if not os.path.exists('./sessions'):
    os.mkdir('./sessions')

api_id = '24682062'
api_hash = "45b4668a1cdb20d40c7cd097ed9127e4"

r = Fore.RED
n = Fore.RESET
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs
re="\033[1;31m"
gr="\033[1;32m"
wi="\033[1;35m"

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def hiddenadder():

    TARGET_group = "mangomanintell"
    my_group = "playbunnycoin"
    print(Style.BRIGHT + Fore.GREEN + f'This option scrape messages of group after scraping message it print sender id, sender username, everything of message in data.csv, this is how this option scrape hidden members of Group No fill below information if you understand this.')
    
    scrlimit = 1000
    HackingZone_dev = 3
    maximamem = 45
    existing_members = set()
    addedchutiya = set()
    rajloda = set()
    async def rajn():
        with open('phone.csv', 'r')as f:
           str_list = [row[0] for row in csv.reader(f)]
           phone = utils.parse_phone(str_list[0])
           print(Style.BRIGHT + Fore.GREEN + f"Getting Members from {phone}")
           async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                   try:
                      await app.join_chat(my_group)
                      print(f'{gr}Joined Your Group')
                   except UserAlreadyParticipant:
                      time.sleep(0)
                   try:
                       my_group_entity = await app.get_chat(my_group)
                       rajloda.add(my_group_entity.id)
                   except Exception as e:
                       print('Failed to get chat entity:', e)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Scraping Your Group to Filter Common Members')
                   async for my_group_member in app.get_chat_members(chat_id=my_group_entity.id):
                       existing_members.add(my_group_member.user.id)
    asyncio.run(rajn())
    gomuhu = str(rajloda)
    chutiya = gomuhu.strip('{}')
    lodabolo = int(chutiya)
    phone = []
    with open('phone.csv', 'r') as delta_obj:
            csv_reader = reader(delta_obj)
            list_of_phone = tuple(csv_reader)
            for phone_ in list_of_phone:
                phone.append(int(phone_[0]))
            pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')
    
    stacno = 1
    endacno = 5000000
    
    From = int(stacno) - 1
    Upto = int(endacno)
    
    async def mainn():
        indexx = 0
        a = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            phone = utils.parse_phone(xd)
            async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {cy}Starting session... ')
                try:
                   await app.join_chat(TARGET_group)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Joined Group to Scrape')
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.get_chat(TARGET_group)
                except Exception as e:
                    print('Failed to get chat entity:', e)
                    return
                
                nu = 1
                stop = 0
                flood = 0
                added = 0
                peer = 0
                userbanned = 0
                
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Scraping Target Group')
                existing_memberst = {}

                async for message in app.get_chat_history(target_group_entity.id, limit=scrlimit):
                        if not message.from_user:
                           continue
                        try:
                           user = await app.get_users(message.from_user.id)
                        except Exception as e:
                           continue

                        if user is not None:
                            user_id = user.id
                            first_name = user.first_name or ''
                            last_name = user.last_name or ''
                            username = user.username or ''
 
                            if user_id not in existing_memberst and user_id not in existing_members and user_id not in addedchutiya:
                                existing_memberst[user_id] = {
                                    'first_name': first_name,
                                    'last_name': last_name,
                                    'username': username
                                }
                        
                                if stop == maximamem:
                                    print(f'{re}added {maximamem} members breaking')
                                    break

                                if flood == 5:
                                    print(f'{re}flood errors breaking')
                                    print('total added user ===', added)
                                    break

                                if peer == 5:
                                    print(f'{re}peer flood errors breaking')
                                    print('total added user ===', added)
                                    break

                                if userbanned == 5:
                                    print(f'{re}UserBannedInChannelError errors breaking')
                                    print('total added user ===', added)
                                    break

                                user_idd = await app.resolve_peer(int(user_id))
                                addedchutiya.add(user_id)
                                try:
                                    access_hash = user_idd.access_hash
                                    await app.add_chat_members(lodabolo, user_idd.user_id, access_hash)
                                    #print("user added", str(first_name), str(last_name))
                                    raj = str(first_name)
                                    print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group}')
                                    stop = stop + 1
                                    added = added + 1
                                    time.sleep(HackingZone_dev)
                            
                                except UserPrivacyRestricted as e:
                                    await asyncio.sleep(random.randint(2,3))
                            
                                except UserChannelsTooMuch as e:
                                    await asyncio.sleep(0)
                            
                                except PeerFlood as e:
                                    print(f'{re}PeerFloodError on your account', nu)
                                    await asyncio.sleep(random.randint(2,5))
                                    nu = nu + 1
                                    peer = peer + 1

                                except UserBannedInChannel as e:
                                    print(f'{re}User Banned In Channel Error', nu)
                                    await asyncio.sleep(random.randint(2,5))
                                    nu = nu + 1
                                    userbanned = userbanned + 1

                                except FloodWait as e:
                                    print(f'{gr}FloodWait of{re} {e.value}', nu)
                                    await asyncio.sleep(random.randint(2,5))
                                    nu = nu + 1
                                    flood = flood + 1

                                except RPCError as e:
                                     status = e.__class__.__name__
                                     print(f'{status}')
                            else:
                                pass
        a += 1
    asyncio.run(mainn())

hiddenadder()


def ramexadder():

    TARGET_group = "mangomanintell"
    my_group = "playbunnycoin"
    HackingZone_dev = 3
    maximamem = 45
    existing_members = set()
    addedchutiya = set()
    rajloda = set()
    async def rajn():
        with open('phone.csv', 'r')as f:
           str_list = [row[0] for row in csv.reader(f)]
           phone = utils.parse_phone(str_list[0])
           print(Style.BRIGHT + Fore.GREEN + f"Getting Members from {phone}")
           async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                   try:
                      await app.join_chat(my_group)
                      print(f'{gr}Joined Your Group')
                   except UserAlreadyParticipant:
                      time.sleep(0)
                   try:
                       my_group_entity = await app.get_chat(my_group)
                       rajloda.add(my_group_entity.id)
                   except Exception as e:
                       print('Failed to get chat entity:', e)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Scraping Your Group to Filter Common Members')
                   async for my_group_member in app.get_chat_members(chat_id=my_group_entity.id):
                       existing_members.add(my_group_member.user.id)
    asyncio.run(rajn())
    gomuhu = str(rajloda)
    chutiya = gomuhu.strip('{}')
    lodabolo = int(chutiya)
    phone = []
    with open('phone.csv', 'r') as delta_obj:
            csv_reader = reader(delta_obj)
            list_of_phone = tuple(csv_reader)
            for phone_ in list_of_phone:
                phone.append(int(phone_[0]))
            pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')
    
    stacno = 1
    endacno = 5000000
    
    From = int(stacno) - 1
    Upto = int(endacno)
    
    async def mainn():
        indexx = 0
        a = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            phone = utils.parse_phone(xd)
            async with Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone) as app:
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {cy}Starting session... ')
                try:
                   await app.join_chat(TARGET_group)
                   print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Joined Group to Scrape')
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.get_chat(TARGET_group)
                except Exception as e:
                    print('Failed to get chat entity:', e)
                    return
                
                nu = 1
                stop = 0
                flood = 0
                added = 0
                peer = 0
                userbanned = 0
                
                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- Scraping Target Group')
                async for target_member in app.get_chat_members(chat_id=target_group_entity.id):
                    if target_member.user.id not in existing_members and target_member.user.id not in addedchutiya:
                        user_id = target_member.user.id
                        first_name = target_member.user.first_name or ''
                        last_name = target_member.user.last_name or ''
                        username = target_member.user.username or ''
                        
                        if stop == maximamem:
                            print(f'{re}added {maximamem} members breaking')
                            break

                        if flood == 5:
                            print(f'{re}flood errors breaking')
                            print('total added user ===', added)
                            break

                        if peer == 5:
                            print(f'{re}peer flood errors breaking')
                            print('total added user ===', added)
                            break

                        if userbanned == 5:
                            print(f'{re}UserBannedInChannelError errors breaking')
                            print('total added user ===', added)
                            break

                        user_idd = await app.resolve_peer(int(user_id))
                        addedchutiya.add(user_id)
                        try:
                            access_hash = user_idd.access_hash
                            await app.add_chat_members(lodabolo, user_idd.user_id, access_hash)
                            #print("user added", str(first_name), str(last_name))
                            raj = str(first_name)
                            print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group}')
                            stop = stop + 1
                            added = added + 1
                            time.sleep(HackingZone_dev)
                            
                        except UserPrivacyRestricted as e:
                            await asyncio.sleep(random.randint(2,3))
                            
                        except UserChannelsTooMuch as e:
                            await asyncio.sleep(0)
                            
                        except PeerFlood as e:
                            print(f'{re}PeerFloodError on your account', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            peer = peer + 1

                        except UserBannedInChannel as e:
                            print(f'{re}User Banned In Channel Error', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            userbanned = userbanned + 1

                        except FloodWait as e:
                            print(f'{gr}FloodWait of{re} {e.value}', nu)
                            await asyncio.sleep(random.randint(2,5))
                            nu = nu + 1
                            flood = flood + 1

                        except RPCError as e:
                             status = e.__class__.__name__
                             print(f'{status}')
                            
        a += 1
    asyncio.run(mainn())

ramexadder()