import sys
import pickle, os
from time import sleep
import webbrowser
import time
import random
import string
import pyfiglet
from pyrogram import Client
import asyncio
from pyrogram.errors import FloodWait
from pyrogram.errors import PeerFlood
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import UserNotMutualContact
from pyrogram.errors import UserPrivacyRestricted
from pyrogram.errors import UserNotParticipant, UserAlreadyParticipant
from pyrogram.errors import UserChannelsTooMuch
from pyrogram.errors import UserIdInvalid
from pyrogram.errors import UserKicked
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors import UserBannedInChannel
from pyrogram.errors import RPCError
from pyrogram.errors import PhoneNumberUnoccupied
from pyrogram.errors import PhoneNumberInvalid
from pyrogram.errors import PhoneNumberOccupied
from pyrogram.errors import PhoneNumberBanned
from pyrogram.errors import PhoneNumberFlood
from pyrogram.errors import ApiIdInvalid
import datetime
import gender_guesser.detector as gender
from pyrogram import types
from pyrogram.raw import functions, types
from pyrogram.enums import UserStatus
from pyrogram.errors import UserDeactivated, AuthKeyUnregistered, SessionExpired, UserDeactivatedBan, SessionRevoked
from pyrogram.types import ChatEventFilter, InputPhoneContact
import time
import configparser
import csv
from csv import reader
from colorama import Fore, Back, Style, init
import colorama
colorama.init(autoreset=True)
from telethon import utils
import traceback
from licensing.models import *
from licensing.methods import Key, Helpers
import requests
from geopy.geocoders import Nominatim
from ts import messagesendergroup, messagesendergrouppic, messagesendergrouppicsingle, messagesendergroupsingle, messagesendergroupmultimsg, messagesendergroupmultimsgpic, messagesendergroupmultimsgpicmultigroups, messagesendergroupmultimsgmultigroups, messagesendermultigroupsinglepic, messagesendermultigroupsingle, forward_to_channels, forward_to_channelsnotag, multi_ccraper, messagesendering, messagesenderingpic, addtocontactbyimp, addtocontactbygroup
from faker import Faker
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

def banner():
    import random
    
    b= [
    ]
    for char in b:
        print(f'{char}{w}')
    print(f'{gr}Made by @ezramain')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def login():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))
    print()
    num_accounts = int(input(f"{gr}Enter the number of accounts you want to add:{w} "))
    
    phone_numbers = []
    print()
    for i in range(num_accounts):
        phone = input(f"{gr}Enter phone number for account {i + 1}:{re} ")
        phone_numbers.append(phone)

    remove_blank_lines('phone.csv')
    with open('phone.csv', 'r') as f:
        str_lists = [row[0] for row in csv.reader(f)]
        
    phone_numbers = remove_duplicates(phone_numbers)
    
    with open('phone.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for phone in phone_numbers:
            if phone not in str_lists:
                phones = utils.parse_phone(phone)
                print(Style.BRIGHT + Fore.GREEN + f"Login {phones}")
                app = Client(f'sessions/{phones}', api_id, api_hash,phone_number=phones)
                app.start()
                app.join_chat('@The_Hacking_Zone')
                time.sleep(4.0)
                app.join_chat('@Techno_Trickop')
                app.stop()
                writer.writerow([phone])
    print()
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !')
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to Exit')
    input()


def specificaccremove():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
        
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))

    def display_phone_numbers():
        with open('phone.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            phone_numbers = [row[0] for row in reader]
            for i, phone in enumerate(phone_numbers, start=1):
                print(f"{gr}{i}. {phone}")

    remove_blank_lines('phone.csv')
    print()
    print(f"{re}All Phone Numbers:")
    display_phone_numbers()
    print()
    to_remove = input(f"{Style.BRIGHT + ye}Enter the numbers of the accounts to remove (comma-separated):{re} ").split(',')
    to_remove = [int(num) for num in to_remove]

    with open('phone.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        phone_numbers = [row[0] for row in reader]

    removed_accounts = []
    for i in sorted(to_remove, reverse=True):  # Iterate in reverse to avoid index issues
        if i >= 1 and i <= len(phone_numbers):
           removed_accounts.append(phone_numbers.pop(i - 1))

    with open('phone.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for phone in phone_numbers:
            writer.writerow([phone])
    print()
    print(f"{re}Removed Accounts:")
    for account in removed_accounts:
        print(f"{gr}{account}")

    print(Style.BRIGHT + Fore.RESET + 'Accounts Removed!')
    print()
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to exit')
    input()

def BanFilter():

    if not os.path.exists(f'BanNumbers.csv'):
        fp = open('BanNumbers.csv', 'x')
        fp.close()
        
    MadeByHackingZone = []

    done = False
    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]

        po = 0
        for unparsed_phone in str_list:
            po += 1

            phone = utils.parse_phone(unparsed_phone)

            print(f"{gr}Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            # client.start(phone)
            try:
                    app.start()
                    continue

            except AuthKeyUnregistered:
                    print(f'{re}Maybe you or someone Terminated this Session')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")
                         writer.writerows(MadeByHackingZone)

            except UserDeactivatedBan:
                    print(f'{re}This account is banned')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except SessionExpired:
                    print(f'{re}This Session was Expired')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except SessionRevoked:
                    print(f'{re}The authorization has been invalidated, because of the user terminating all sessions')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)
                         
            except UserDeactivated:
                    print(f'{re} Account User Deactivated or Account Banned')
                    HackingZone = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByHackingZone.append(Nero_op)
                    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
                         writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

                         writer.writerows(MadeByHackingZone)

                    continue

            # client.disconnect()
        done = True
        print(f'{gr}List Of Banned Numbers')
        print(*MadeByHackingZone, sep='\n')
        print(f'{gr}Saved In BanNumbers.csv')


    def autoremove():


        collection = []
        nc = []
        collection1 = []
        nc1 = []
        maind = []

        with open("phone.csv", "r") as infile:
            for line in infile:
                collection.append(line)

        for x in collection:
            mod_x = str(x).replace("\n", "")
            nc.append(mod_x)

        with open("BanNumbers.csv") as infile, open("outfile.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        with open("outfile.csv", "r") as outfile:
            for line1 in outfile:
                rrr = line1.replace("\n", "")
                os.remove(f'sessions/{rrr}.session')
                collection1.append(line1)

        for i in collection1:
            mod_i = str(i).replace("\n", "")
            nc1.append(mod_i)

        unique = set(nc)
        unique1 = set(nc1)

        itd = unique.intersection(unique1)

        for x in nc:
            if x not in itd:
                maind.append(x)

        with open('unban.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(maind)

        with open("unban.csv") as last, open("phone.csv", "w") as final:
            for line3 in last:
                mod_i = str(line3).replace("\n", "")
                final.write(mod_i)

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")
        print("Done,All Banned Number Have Been Removed")


    def dellst():
        import csv
        import os

        with open("phone.csv") as infile, open("unban.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")

        print("complete")


    autoremove()
    dellst()

    input("Done!" if done else "Error!")


def ramexadder():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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

def hiddenadder():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    print(Style.BRIGHT + Fore.GREEN + f'This option scrape messages of group after scraping message it print sender id, sender username, everything of message in data.csv, this is how this option scrape hidden members of Group No fill below information if you understand this.')
    
    scrlimit = int(input(f'{cy}Enter how many message you want to scrape to get hidden members{r}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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

def ramexdaily():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    
    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        status = None

                        # Check if the member is online or seen recently before saving
                        try:
                            entity = await app.get_users(target_member.user.id)
                            if entity.status:
                                if entity.status == UserStatus.ONLINE:
                                    status = 'Online'
                                elif entity.status == UserStatus.RECENTLY:
                                    status = 'Recently Seen'
                                elif entity.status == UserStatus.OFFLINE:
                                    d = entity.last_online_date
                                    today_user = d.day == today.day and d.month == today.month and d.year == today.year
                                    yesterday_user = d.day == yesterday.day and d.month == yesterday.month and d.year == yesterday.year
                                    if today_user or yesterday_user:
                                        status = d or type(entity.last_online_date).__name__
                        except Exception as e:
                            print('Failed to get entity or status:', e)
                            

                        if status:
                        
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
                                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group} {re}Status: {gr}{status}')
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

def ramexweekly():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    
    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        status = None

                        # Check if the member is online or seen recently before saving
                        try:
                            entity = await app.get_users(target_member.user.id)
                            if entity.status:
                                if entity.status == UserStatus.ONLINE:
                                    status = 'Online'
                                elif entity.status == UserStatus.RECENTLY:
                                    status = 'Recently Seen'
                                elif entity.status == UserStatus.LAST_WEEK:
                                    status = 'Last Week'
                                elif entity.status == UserStatus.OFFLINE:
                                    d = entity.last_online_date
                                    for i in range(0,7):
                                        current_day = today - datetime.timedelta(days=i)
                                        correct_user = d.day == current_day.day and d.month == current_day.month and d.year == current_day.year
                                        if correct_user:
                                            status = d or type(entity.last_online_date).__name__
                        except Exception as e:
                            print('Failed to get entity or status:', e)
                            

                        if status:
                        
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
                                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group} {re}Status: {gr}{status}')
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

def ramexmonthly():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    
    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        status = None

                        # Check if the member is online or seen recently before saving
                        try:
                            entity = await app.get_users(target_member.user.id)
                            if entity.status:
                                if entity.status == UserStatus.ONLINE:
                                    status = 'Online'
                                elif entity.status == UserStatus.RECENTLY:
                                    status = 'Recently Seen'
                                elif entity.status == UserStatus.LAST_WEEK:
                                    status = 'Last Week'
                                elif entity.status == UserStatus.LAST_MONTH:
                                    status = 'Last Month'
                                elif entity.status == UserStatus.OFFLINE:
                                    d = entity.last_online_date
                                    for i in range(0,30):
                                        current_day = today - datetime.timedelta(days=i)
                                        correct_user = d.day == current_day.day and d.month == current_day.month and d.year == current_day.year
                                        if correct_user:
                                            status = d or type(entity.last_online_date).__name__

                        except Exception as e:
                            print('Failed to get entity or status:', e)
                            

                        if status:
                        
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
                                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group} {re}Status: {gr}{status}')
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


def ramexonline():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    
    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        status = None

                        # Check if the member is online or seen recently before saving
                        try:
                            entity = await app.get_users(target_member.user.id)
                            if entity.status:
                                if entity.status == UserStatus.ONLINE:
                                    status = 'Online'

                        except Exception as e:
                            print('Failed to get entity or status:', e)
                            

                        if status:
                        
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
                                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group} {re}Status: {gr}{status}')
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


def ramexnonactive():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    
    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        status = None

                        # Check if the member is online or seen recently before saving
                        try:
                            entity = await app.get_users(target_member.user.id)
                            if entity.status:
                                if entity.status == UserStatus.LONG_AGO:
                                    status = 'Long Ago'
                                if entity.status == UserStatus.OFFLINE:
                                    d = entity.last_online_date.timestamp()
                                    last_active_date = datetime.datetime.fromtimestamp(d)
                                    thirty_days_ago_timestamp = (today - datetime.timedelta(days=30)).timestamp()

                                    if last_active_date.timestamp() <= thirty_days_ago_timestamp:
                                         status = 'Non-Active' or f'Last Seen on {last_active_date}'

                        except Exception as e:
                            print('Failed to get entity or status:', e)
                            

                        if status:
                        
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
                                print(f'{re} User: {Style.BRIGHT + cy}{phone}{gr} -- {Style.BRIGHT + cy}{raj} {gr}--> {Style.BRIGHT + cy}{my_group} {re}Status: {gr}{status}')
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


def otpviewer():

   with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]
    for pphone in str_list:
        phone = utils.parse_phone(pphone)
        app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
        app.start()
        print(f"{re}Getting Telegram message OTP for {phone}")
        try:
            # Get the latest message from the chat
            for message in app.get_chat_history(777000, limit=1):
                print(f"{Style.BRIGHT + ye}{message.text}")
            else:
                print("No messages found in chat history.")
        except RPCError as e:
            print(f"An error occurred: {e}.")
        app.stop()
        print()
        print(f"{wi}Enter to go to next account")
        input()
    print(f"{gr}Press Enter to Exit")
    input()


def reactionincreaser():

    print(f'{gr}Enter Group/Channel Username: {re}')
    usernamehh = str(input())
    msgid = int(input(f'{gr}Enter Message/Post ID: {re}'))
    reactionty = str(input(f'{gr}Enter Reaction: {re}'))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.join_chat(usernamehh)
            except UserAlreadyParticipant:
                time.sleep(0)
            app.send_reaction(usernamehh, msgid, reactionty)
            print(f'{wi}Successfull Reaction from {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Reaction Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to Exit')
    input()

def sharesincreaser():

    print(f'{gr}Enter Group/Channel Username: {re}')
    usernamehh = str(input())
    msgid = int(input(f'{gr}Enter Message/Post ID: {re}'))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.join_chat(usernamehh)
            except UserAlreadyParticipant:
                time.sleep(0)
            try:
                my_id = app.get_chat(usernamehh)
            except Exception as e:
                print('Failed to get chat entity:', e)
                
            app.forward_messages(chat_id="me", from_chat_id=my_id.id, message_ids=msgid)
            print(f'{wi}Successfull shares from {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def changeraccount():

    print(f'{gr}Send First Name:  ')
    firstname = str(input())
    print(f'{gr}Send Last Name:  ')
    lastname = str(input())
    print(f'{gr}Send Bio Text:  ')
    bio = str(input())
    print(f'{gr}Enter Delay Time Per Request 0 For None: ')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            app.update_profile(first_name=firstname, last_name=lastname, bio=bio)
            print(f'{wi}Successfull Set First, Last & Bio from {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def changerusername():

     def send_usernames_from_csv(phone_csv_path, usernames_csv_path):
          with open(phone_csv_path, 'r') as phone_file, open(usernames_csv_path, 'r') as usernames_file:
              phone_reader = csv.reader(phone_file)
              usernames_reader = csv.reader(usernames_file)
        
              phone_rows = list(phone_reader)
              usernames_rows = list(usernames_reader)

              if len(phone_rows) != len(usernames_rows):
                  print("Error: The number of rows in 'phone.csv' and 'username.csv' is not equal.")
                  return

              for phone_row, usernames_row in zip(phone_rows, usernames_rows):
                  phone_number = utils.parse_phone(phone_row[0])
                  username = usernames_row[0]

                  print(Style.BRIGHT + Fore.GREEN + f"Changing username from {phone_number}")
                  app = Client(f'sessions/{phone_number}', api_id, api_hash,phone_number=phone_number)
                  app.start()

                  time.sleep(0)
                  

                  try:
                     app.set_username(username)
                  except Exception as e:
                      print(f"Error in Clone: {str(e)}")

                  app.stop()
                  print()

          print(Style.BRIGHT + Fore.RESET + 'All Username Done!')

     send_usernames_from_csv('phone.csv', 'username.csv')

def twostepverification():

    print('Enter What 2 Step Password you Want to Set:  ')
    usernamehh = str(input())
    print('Enter Delay Time Per Request 0 For None: ')
    Rocky_200_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.enable_cloud_password(usernamehh)
               print('Your 2 Step Setup Successful')
               app.stop()
            except Exception as e:
               #print('error',e)
               try:
                  print("This Account have already 2 Step Verification so Please Enter your Current 2 Step Password: ")
                  rss = str(input())
                  app.remove_cloud_password(rss)
                  app.enable_cloud_password(usernamehh)
                  print('Your 2 Step Setup Successful')
               except Exception as e:
                  print('error',e)
            time.sleep(Rocky_200_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def ScamTag():

    msg = str(input(f'{gr}Enter Message to Report: {re}'))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.send_message(scam,msg)
               print(f'{wi}Successfull Report from {phone}')
            except Exception as e:
                print('Failed to Send Report:', e)
                time.sleep(0)
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()


def ramexsender():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    msg = str(input(f'{gr}Enter Message You want to Send: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to Send per account (Maximum 50): {re}'))
    addedchutiya = set()
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
                    if target_member.user.id not in addedchutiya:
                        user_id = target_member.user.id
                        first_name = target_member.user.first_name or ''
                        last_name = target_member.user.last_name or ''
                        username = target_member.user.username or ''
                        
                        if stop == maximamem:
                            print(f'{re}Sended {maximamem} members breaking')
                            break

                        if flood == 5:
                            print(f'{re}flood errors breaking')
                            print('total Send user ===', added)
                            break

                        if peer == 5:
                            print(f'{re}peer flood errors breaking')
                            print('total Send user ===', added)
                            break

                        if userbanned == 5:
                            print(f'{re}UserBannedInChannelError errors breaking')
                            print('total Send user ===', added)
                            break

                        user_idd = int(user_id)
                        addedchutiya.add(user_id)
                        try:
                            #await app.add_chat_members(lodabolo, user_idd.user_id, access_hash)
                            await app.send_message(user_idd,msg)
                            print(f"{gr}Message Sended to", f'{wi}{str(first_name)} {str(last_name)}')
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



def setprofilepic():
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    HackingZone_dev = int(input())
    print(f'{gr}Make Sure you replace ramexfour.jpg file')
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            app.invoke(functions.photos.UploadProfilePhoto(file=app.save_file(f'ramexfour.jpg')))
            print(f'{wi}Successfull Set Profile Pic from {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def removeprofilepic():
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            photos = [p for p in app.get_chat_photos("me")]
            if photos:
               app.delete_profile_photos(photos[0].file_id)
               app.delete_profile_photos([p.file_id for p in photos[1:]])
            else:
               time.sleep(0)
            print(f'{wi}Successfull Removed Profile Pic from {phone}')
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()


def reportspamuser():
    
    username = str(input(f'{gr}Give That Person or Account Username: {re}'))
    msg = str(input(f'{gr}Enter Message to Report: {re}'))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               peer = app.resolve_peer(username)
               result = app.invoke(
                    functions.account.ReportPeer(
                    peer=peer,
                    reason=types.InputReportReasonSpam(),
                    message=msg
               ))
               print(result)
               print(f'{wi}Successfull Report from {phone}')
            except Exception as e:
                print('Failed to Send Report:', e)
                time.sleep(0)
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def pmspamdm():
    
    username = str(input(f'{gr}Give That Person or Account Username: {re}'))
    msg = str(input(f'{gr}Enter Message to Spam PM/DM: {re}'))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.send_message(username,msg)
               print(f'{wi}Successfull Send Message from {phone}')
            except Exception as e:
                print('Failed to Send Message:', e)
                time.sleep(0)
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Send Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()


def groupjoiner():

    print(f'{gr}Enter Group/Channel Username:  ')
    usernamehh = str(input())
    print(f'{gr}Enter Delay Time Per Request 0 For None: ')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.join_chat(usernamehh)
               print(f'{wi}Join Successful')
               app.stop()
            except UserAlreadyParticipant:
                time.sleep(0)
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Channel Join Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def grouplefter():

    print(f'{gr}Enter Group/Channel Username:  ')
    usernamehh = str(input())
    print(f'{gr}Enter Delay Time Per Request 0 For None: ')
    HackingZone_dev = int(input())
    lowercase_input = usernamehh.lower()

    restricted_channels = ['the_hacking_zone', '@the_hacking_zone', '@techno_trickop', '@teamtrickyabhi', '@the_hacking_zone_group', 'techno_trickop', 'teamtrickyabhi', 'the_hacking_zone_group', '1561952101', '-1001561952101', '1001561952101', 'https://t.me/the_hacking_zone_group', 'https://t.me/the_hacking_zone', '1705557435', '-1001705557435', '1001705557435', 'https://t.me/teamtrickyabhi', '1717626647', '-1001717626647', '1001717626647', 'https://t.me/techno_trickop', '1366063062', '1001366063062', '-1001366063062']

    if lowercase_input in restricted_channels:
         print('Sorry, you cannot report this channel')
         exit()
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.leave_chat(usernamehh)
               print(f'{wi}Left Successful')
               app.stop()
            except UserNotParticipant:
                time.sleep(0)
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def loginbycsv():

    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            app.join_chat('@The_Hacking_Zone')
            time.sleep(4.0)
            app.join_chat('@Techno_Trickop')
            app.stop()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def nearbyadderlatlong():

    latitude = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Latitude: {re}'))
    longitude = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Longitude: {re}'))
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyaddercity():

    cityname = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter City or Village Name: {re}'))
    try:
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(cityname)
        latitude = str(location.latitude)
        longitude = str(location.longitude)
    except Exception as e:
        print('Maybe Village or City Name Wrong:',e)
        exit()
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def opthree():

    file_path = "opthree.py"
    if os.path.exists(file_path):
        print(f"{re}OPThree file detected Executing {gr}{file_path} ...")
        time.sleep(2)
        os.system(f"{sys.executable} {file_path}")
    else:
        print(f"{re}File {gr}{file_path} missing. Download and extract again.")

def extractvcftonumb():
    import vobject
    file_path = str(input("Enter File name with extension: "))
    if os.path.exists(f'numbers.csv'):
       os.remove(f'numbers.csv')
       
    if os.path.exists(f'done.csv'):
       os.remove(f'done.csv')
    if not os.path.exists(f'done.csv'):
        fp = open('done.csv', 'x')
        fp.close()
                  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    vcards = vobject.readComponents(data)

    phone_numbers = []

    for vcard in vcards:
        if 'tel' in vcard.contents:
            for phone in vcard.tel_list:
                phone_numbers.append(phone.value)

    with open('numbers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["numbers"])
        writer.writerows([[number] for number in phone_numbers])
    print("Successful")



def checknumb():

    HackingZone_devinput = int(1)
    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = HackingZone_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]
        
    phonee = value
    if phonee:
            phone = utils.parse_phone(phonee)
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            try:
               if os.path.exists(f'filternumbers.csv'):
                  os.remove(f'filternumbers.csv')
               with open('numbers.csv', 'r', encoding='utf-8')as f:
                  str_list = [row[0] for row in csv.reader(f)]
                  po = 0
                  for numb in str_list:
                      lund = utils.parse_phone(numb)
                      po += 1
                      time.sleep(3)
                      print(Style.BRIGHT + Fore.BLUE + f"Checking {lund}")
                      try:
                          userinfo = app.invoke(functions.contacts.ResolvePhone(phone=f'{lund}'))
                          print(userinfo)
                          print(userinfo.users)
                          for user in userinfo.users:
                              print(user.id)
                              user_id = user.id
                              user_idd = app.resolve_peer(int(user_id))
                              access_hash = user_idd.access_hash
                              #app.add_chat_members("justtestog", user_idd.user_id, access_hash)
                              
                          print(Style.BRIGHT + Fore.YELLOW + 'Number Valid')
                          with open('filternumbers.csv', 'a', newline='', encoding='utf-8') as filter_file:
                            writer = csv.writer(filter_file)
                            writer.writerow([numb])
                      except PhoneNumberUnoccupied:
                          print("This Number is Not Occupied by Anyone")
                      except PhoneNumberInvalid:
                          print("This Number is Invalid")
                      except PhoneNumberBanned:
                          print("This Number is Banned")
                      except PhoneNumberOccupied:
                          print("This Number is Occupied")
                      except PhoneNumberFlood:
                          print("This Number is Flooded")
                      except Exception as e:
                          print(e)
                      print()
            except Exception as e:
                print(e)
            app.stop()
    else:
       print("no phone")
    print(Style.BRIGHT + Fore.YELLOW + 'Check Done saved in filternumbers.csv')


def nearbyadderautoindia():

    fake = Faker('en_IN')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyadderautousa():

    fake = Faker('en_US')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautobangladesh():

    fake = Faker('bn_BD')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautorussia():

    fake = Faker('ru_RU')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautorussia():

    fake = Faker('ru_RU')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyadderautoukraine():

    fake = Faker('uk_UA')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautouk():

    fake = Faker('en_GB')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyadderautojapan():

    fake = Faker('ja_JP')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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



def nearbyadderautogermany():

    fake = Faker('de_DE')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautoswitzerland():

    fake = Faker('de_CH')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautobrazil():

    fake = Faker('pt_BR')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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



def nearbyadderautoindonesia():

    fake = Faker('id_ID')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautobelgium():

    fake = Faker('nl_BE')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautoturkey():

    fake = Faker('tr_TR')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautopakistan():


    print(f"{re}Note: {gr}Pakistan is not available in our Database so we used Pakistan nearest Islam Country Iran. Soon we will add database for Pakistan also.")
    print()
    fake = Faker('fa_IR')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyadderautobhutan():

    print(f"{re}Note: {gr}Bhutan is not available in our Database so we used Bhutan nearest Country China. Soon we will add database for Bhutan also.")
    print()
    
    fake = Faker('zh_CN')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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


def nearbyadderautouzbekistan():

     print(f"{re}Sorry: {gr}Uzbekistan is not available in our Database so we can't help you to add members in your Uzbekistan group. But if you want you can add from other country. Press Enter to open menu again.")
     input()
     nearbyadderauto()


def nearbyadderautocombodia():

    print(f"{re}Note: {gr}Cambodia is not available in our Database so we used Combodia nearest Country Thailand. Soon we will add database for Cambodia also.")
    print()
    
    fake = Faker('th_TH')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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

def nearbyadderautoethiopia():

     print(f"{re}Sorry: {gr}Ethiopia is not available in our Database so we can't help you to add members in your Ethiopia group. But if you want you can add from other country. Press Enter to open menu again.")
     input()
     nearbyadderauto()

def nearbyadderautonigera():

     print(f"{re}Sorry: {gr}Nigeria is not available in our Database so we can't help you to add members in your Nigeria group. But if you want you can add from other country. Press Enter to open menu again.")
     input()
     nearbyadderauto()



def nearbyadderautoisrael():

    fake = Faker('he_IL')
    
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
    existing_members = set()
    locationstore = set()
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
                   await app.join_chat(my_group)
                except UserAlreadyParticipant:
                   time.sleep(0)
                
                location = None
                while location is None:
                    random_city_name = fake.city()

                    if random_city_name not in locationstore:
                       try:
                           geolocator = Nominatim(user_agent="MyApp")
                           location = geolocator.geocode(random_city_name)
                           if location:
                              latitude = str(location.latitude)
                              longitude = str(location.longitude)
                              locationstore.add(random_city_name)
                              print(random_city_name, latitude, longitude)
                           else:
                              print('Invalid city.')
                              location = None  # Regenerate location for a new city
                       except Exception as e:
                           print('Invalid city or error:', e)
                           location = None  # Regenerate location for a new city
                    else:
                       print("City already generated, trying another")
                       location = None

                try:
                    target_group_entity = await app.invoke(functions.contacts.GetLocated(geo_point=types.InputGeoPoint(lat=float(latitude), long=float(longitude))))
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
                for target_member in target_group_entity.users:
                    if target_member.id not in existing_members and target_member.id not in addedchutiya:
                        user_id = target_member.id
                        first_name = target_member.first_name or ''
                        last_name = target_member.last_name or ''
                        username = target_member.username or ''
                        
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



def maleadderh():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        
                        def predict_gender(name):
                            d = gender.Detector(case_sensitive=False)
                            gender_prediction = d.get_gender(name)
                            return gender_prediction
                        predicted_gender = predict_gender(first_name)
                        if predicted_gender == 'male':
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

def femaleadderh():

    TARGET_group = input(f'{INPUT}{Style.BRIGHT + cy} Enter Public Target Group username or Private Group Link to Scrape members: {re}')
    my_group = str(input(f'{INPUT}{Style.BRIGHT + cy} Enter Your Public Group username or Private Group Link to Add Members: {re}'))
    HackingZone_dev = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter delay time per request{w}[{lg}0 for None{wi}]: {re}'))
    maximamem = int(input(f'{INPUT}{Style.BRIGHT + cy} Enter How many members you want to add per account (Maximum 50): {re}'))
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
                        
                        def predict_gender(name):
                            d = gender.Detector(case_sensitive=False)
                            gender_prediction = d.get_gender(name)
                            return gender_prediction
                        predicted_gender = predict_gender(first_name)
                        if predicted_gender == 'female':
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

def logintypetwo():
    if os.stat('api.csv').st_size == 0:
        print("--------------------------------------------")
        print("api.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    if os.stat('devicelist.csv').st_size == 0:
        print("--------------------------------------------")
        print("devicelist.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    delaybolte = int(input(f"{gr}Enter Delay Per Second You Want To Use: {re}"))
    with open('api.csv', 'r', encoding='utf-8') as f:
        Apiis = csv.reader(f)
        api = [i for i in Apiis]

    with open('devicelist.csv', 'r', encoding='utf-8') as f:
        devicee = csv.reader(f)
        device = [i for i in devicee]

    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]
        total_phones = len(str_list)
        po = 0
        capi = 0
        dovi = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(f"API ID: {gr}{api[capi][0]}, API Hash: {cy}{api[capi][1]}, Device Name: {re}{device[dovi][0]}")
            print(Style.BRIGHT + Fore.GREEN + f"{cy}Login {gr}{phone} ({po}/{total_phones})")
            app = Client(f"sessions/{phone}", api_id=int(api[capi][0]), api_hash=api[capi][1], phone_number=phone, device_model=device[dovi][0])
            app.start()
            app.join_chat('@The_Hacking_Zone')
            time.sleep(delaybolte)
            app.join_chat('@Techno_Trickop')
            app.stop()
            capi += 1
            dovi += 1
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input() 


def logintypeone():

    if os.stat('api.csv').st_size == 0:
        print("--------------------------------------------")
        print("api.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    if os.stat('devicelist.csv').st_size == 0:
        print("--------------------------------------------")
        print("devicelist.csv is empty. Cannot proceed with login.")
        print("--------------------------------------------")
        return
    delaybolte = int(input(f"{gr}Enter Delay Per Second You Want To Use: {re}"))
    with open('api.csv', 'r', encoding='utf-8') as f:
        Apiis = csv.reader(f)
        api = [i for i in Apiis]

    with open('devicelist.csv', 'r', encoding='utf-8') as f:
        devicee = csv.reader(f)
        device = [i for i in devicee]

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    def remove_duplicates(lst):
        return list(set(lst))
    print()
    num_accounts = int(input(f"{gr}Enter the number of accounts you want to add:{w} "))
    
    phone_numbers = []
    print()
    for i in range(num_accounts):
        phone = input(f"{gr}Enter phone number for account {i + 1}:{re} ")
        phone_numbers.append(phone)

    remove_blank_lines('phone.csv')
    with open('phone.csv', 'r') as f:
        str_lists = [row[0] for row in csv.reader(f)]
        
    phone_numbers = remove_duplicates(phone_numbers)
    
    with open('phone.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        dovi = 0
        capi = 0
        for phone in phone_numbers:
            if phone not in str_lists:
                phones = utils.parse_phone(phone)
                print(f"API ID: {gr}{api[capi][0]}, API Hash: {cy}{api[capi][1]}, Device Name: {re}{device[dovi][0]}")
                print(Style.BRIGHT + Fore.GREEN + f"{cy}Login {gr}{phone}")
                app = Client(f"sessions/{phones}", api_id=int(api[capi][0]), api_hash=api[capi][1], phone_number=phones, device_model=device[dovi][0])
                app.start()
                app.join_chat('@The_Hacking_Zone')
                time.sleep(delaybolte)
                app.join_chat('@Techno_Trickop')
                app.stop()
                dovi += 1
                capi += 1
                writer.writerow([phone])
    print()
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !')
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to Exit')
    input()


def csvblankremover():

    if not os.path.exists(f'phone.csv'):
        fp = open('phone.csv', 'x')
        fp.close()
    with open('phone.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([])
         
    def remove_blank_lines(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            f.writelines(line for line in lines if line.strip())

    remove_blank_lines('phone.csv')
    print(f"{gr}Extra Line Removed Successfully")

def viewsincrement():

    print(f'{gr}Enter Group/Channel Username:  {re}')
    usernamehh = str(input())
    postid = int(input(f"{gr}Enter Post ID: {re}"))
    print(f'{gr}Enter Delay Time Per Request 0 For None: {re}')
    HackingZone_dev = int(input())
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            try:
               app.join_chat(usernamehh)
            except UserAlreadyParticipant:
                time.sleep(0)
            try:
               my_group_entity = app.get_chat(usernamehh)
               peer = app.resolve_peer(my_group_entity.id)
               test = app.invoke(functions.messages.GetMessagesViews(peer=peer, id=[postid], increment=True))
               #print(test)
               print(f'{wi}Views Successfully')
            except Exception as e:
               print(e)
            app.stop()
            time.sleep(HackingZone_dev)
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number views Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()


def autogroupmaker():

    phone_numbers = []

    with open('phone.csv', 'r') as f:
        csv_reader = csv.reader(f)
        phone_numbers = [row[0] for row in csv_reader]

    def create_groups(client, phone):
        while True:
            username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
            try:
                print(f"Creating Group {username} with account: {phone}")
                client.create_supergroup(username)
            except FloodWait as e:
                print(f'Flood detected on account: {phone}. Switching to the next account.')
                return
            except Exception as e:
                print(f'Error: {e}')
                return

    for phone_number in phone_numbers:
        client = Client(f'sessions/{phone_number}', api_id, api_hash, phone_number=phone_number)

        print(f"Login with account: {phone_number}")
        client.start()

        create_groups(client, phone_number)

        client.stop()

    print('All tasks completed or encountered an error.')
    print('Press Enter to exit.')
    input()

def groupchatcloner():


    if os.path.exists(f'scrmessage.csv'):
        os.remove(f'scrmessage.csv')
    if not os.path.exists(f'scrmessage.csv'):
        fp = open('scrmessage.csv', 'x')
        fp.close()
        
    groupsc = str(input(f"{gr}Enter Target Group Username or Private Link: {re}"))
    groupyour = str(input(f"{gr}Enter Your Group Link: {re}"))
    groupmsg = int(input(f"{gr}Enter Number of messages you want to scrape: {re}"))
    delayper = int(input(f"{gr}Enter Delay Per Second between per Message: {re}"))
    def save_messages(message):
        with open('scrmessage.csv', 'a') as file:
           file.write(f"{message.id}\n")
        
    with open('phone.csv', 'r')as f:
        first_number = f.readline().strip()
        pphone = first_number
        if pphone:
            phone = utils.parse_phone(pphone)
            print(Style.BRIGHT + Fore.GREEN + f"Getting {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            try:
               app.join_chat(groupsc)
            except UserAlreadyParticipant:
               pass
            try:
               sc_entity = app.get_chat(groupsc)
            except Exception as e:
               print(e)
            for messagee in app.get_chat_history(sc_entity.id, limit=1):
                rare = messagee.id - groupmsg
                messages = app.get_chat_history(sc_entity.id, limit=groupmsg,offset_id=rare)
                messages = sorted(messages, key=lambda x: x.id)
                for message in messages:
                     save_messages(message)
            app.stop()
            print()

    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Joining {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            try:
               app.start()
               app.join_chat(groupsc)
               time.sleep(2)
               app.join_chat(groupyour)
               print(f'{wi}Join Successful')
            except UserAlreadyParticipant:
                time.sleep(0)
            try:
               your_entity = app.get_chat(groupyour)
            except Exception as e:
               print(e)
            app.stop()
            print()
    
    with open('scrmessage.csv', 'r', encoding='utf-8') as f:
        message_ids = [int(line.strip()) for line in f]

    with open('phone.csv', 'r') as f:
        phone_numbers = [row[0] for row in csv.reader(f)]

    message_index = 0
    while message_index < len(message_ids):
        for pphone in phone_numbers:
            phone = utils.parse_phone(pphone)
            print(Style.BRIGHT + Fore.GREEN + f"Using {phone}")
        
            app = Client(f'sessions/{phone}', api_id, api_hash, phone_number=phone)
            app.start()
            time.sleep(delayper)
        # Copy and send the message to "justtestog"
            app.copy_message(your_entity.id, sc_entity.id, message_ids[message_index])
        
            app.stop()
            print(f"Message with ID {message_ids[message_index]} sent using {phone}")
        
            message_index += 1  # Move to the next message

            if message_index >= len(message_ids):
                break  # Stop the loop if all messages are sent

    print("All messages sent using available phone numbers.")


def accountinfogetter():

    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            me = app.get_me()
            print(f"{re}-------------- {gr}Account Info {re}--------------")
            print(f'{re}ID: {gr}{me.id}')
            print(f'{re}Self: {gr}{me.is_self}')
            print(f'{re}Contact: {gr}{me.is_contact}')
            print(f'{re}Mutual Contact: {gr}{me.is_mutual_contact}')
            print(f'{re}Deleted: {gr}{me.is_deleted}')
            print(f'{re}Verified: {gr}{me.is_verified}')
            print(f'{re}Scam: {gr}{me.is_scam}')
            print(f'{re}Fake: {gr}{me.is_fake}')
            print(f'{re}Support: {gr}{me.is_support}')
            print(f'{re}Premium: {gr}{me.is_premium}')
            print(f'{re}First Name: {gr}{me.first_name}')
            print(f'{re}Last Name: {gr}{me.last_name if me.last_name else None}')
            print(f'{re}Status: {gr}{me.status}')
            print(f'{re}Last Online Date: {gr}{me.last_online_date}')
            print(f'{re}Phone Number: {gr}{phone}')
            app.stop()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Info Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()

def limicheckandrem():
    textfor = '''First, please confirm that you will never send this to strangers:
- Unsolicited advertising of any kind
- Promotional messages
- Shocking materials
Were you going to do anything like that?'''
    
    url = 'https://pastebin.com/raw/YKbeUazQ' # url of paste
    r = requests.get(url) # response will be stored from url
    content = r.text
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            app = Client(f'sessions/{phone}', api_id, api_hash,phone_number=phone)
            app.start()
            raj = app.get_me()
            textly = f'''Hello {raj.first_name}!

I’m very sorry that you had to contact me. Unfortunately, some actions can trigger a harsh response from our anti-spam systems. If you think your account was limited by mistake, you can submit a complaint to our moderators.

While the account is limited, you will not be able to send messages to people who do not have your number in their phone contacts or add them to groups and channels. Of course, when people contact you first, you can always reply to them.'''
            input_peer = "spambot"
            app.send_message(input_peer, "/start")
            time.sleep(0.5)
            for message in app.get_chat_history(input_peer, limit=1):
                print(f"{re}Bot Message: {gr}{message.text}")
            if message.text == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
                app.send_message(input_peer, "Cool, thanks")
                print(f"{re}User Message: {gr}Cool, thanks")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                    print(f"{Style.BRIGHT + ye}Conclusion: {re}No limit on your Account")
            elif message.text == 'Unfortunately, some phone numbers may trigger a harsh response from our anti-spam systems. If you think this is the case with you, you can submit a complaint to our moderators or subscribe to Telegram Premium to get less strict limits.':
                print(f"{Style.BRIGHT + ye}Review: {gr}No Limit on Account, It will cause no Problem but it can be fixed. So trying...")
                app.send_message(input_peer, "Submit a complaint")
                print(f"{re}User Message: {gr}Submit a complaint")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                if messagee.text == textfor:
                    app.send_message(input_peer, "No, I’ll never do any of this!")
                    print(f"{re}User Message: {gr}No, I’ll never do any of this!")
                    time.sleep(1)
                    for messageee in app.get_chat_history(input_peer, limit=1):
                        print(f"{re}Bot Message: {gr}{messageee.text}")
                        print()
                        app.send_message(input_peer, content)
                        print(f"{re}User Message: {gr}{content}")
                        time.sleep(1)
                        for messageeee in app.get_chat_history(input_peer, limit=1):
                            print(f"{re}Bot Message: {gr}{messageeee.text}")
                            print()
                            print(f"{Style.BRIGHT + ye}Conclusion: {re}No limit on account but Account have harsh problem, this will not cause any problem to send message and adding members, but still a message has been sent to telegram to fix this.")
                elif messagee.text == "You've already submitted a complaint recently. Our team’s supervisors will check it as soon as possible. Thank you for your patience.":
                        print(f"{Style.BRIGHT + ye}Conclusion: {re}No limit on account but Account have harsh problem, this will not cause any problem to send message and adding members, complaint was already submitted.")
            elif message.text == textly:
                print(f"{Style.BRIGHT + ye}Review: {gr}Account Limited, Let's try to fix this.")
                app.send_message(input_peer, "This is a mistake")
                print(f"{re}User Message: {gr}This is a mistake")
                time.sleep(1)
                for messagee in app.get_chat_history(input_peer, limit=1):
                    print(f"{re}Bot Message: {gr}{messagee.text}")
                    print()
                if messagee.text == 'If you think the limitations on your account were applied by mistake, you can submit a complaint. All complaints will be reviewed by the team’s supervisor. Please note that this will have no effect on limitations that were applied with a good reason. Would you like to submit a complaint?':
                    app.send_message(input_peer, "Yes")
                    print(f"{re}User Message: {gr}Yes")
                    time.sleep(1)
                    for messageee in app.get_chat_history(input_peer, limit=1):
                        print(f"{re}Bot Message: {gr}{messageee.text}")
                        print()
                        app.send_message(input_peer, "No! Never did that!")
                        print(f"{re}User Message: {gr}No! Never did that!")
                        for messageeee in app.get_chat_history(input_peer, limit=1):
                            print(f"{re}Bot Message: {gr}{messageeee.text}")
                            print()
                            app.send_message(input_peer, content)
                            print(f"{re}User Message: {gr}{content}")
                            time.sleep(1)
                            for messageeeee in app.get_chat_history(input_peer, limit=1):
                                print(f"{re}Bot Message: {gr}{messageeeee.text}")
                                print()
                                print(f"{Style.BRIGHT + ye}Conclusion: {re}Account is Limited, We sent a message to spambot to fix this, Let's wait untill it get fixed.")
                elif messagee.text == "You've already submitted a complaint recently. Our team’s supervisors will check it as soon as possible. Thank you for your patience.":
                        print(f"{Style.BRIGHT + ye}Conclusion: {re}Account is Limited, but complaint was already submitted.")
            else:
                print(f"{wi}Account have another limti. This limit can't be removed by spambot, Please Check it.")
            app.stop()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number limitations will remove soon' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()



def main_menu():
    clr()
    banner()
    print(Style.BRIGHT + ye+'Choose a Option:'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [1] Add new accounts'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [2] Filter all banned accounts'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [3] Remove specific accounts'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [4] Subscribe to TrickyAbhi'+n)
    print(Style.BRIGHT + Fore.CYAN+f'            [5] Member Adding {re}(Public & Private Both)'+n)
    print(Style.BRIGHT + ye+'OverPowered Like Options:'+n)
    print(Style.BRIGHT + Fore.CYAN+f'            [6] Hidden Member Adder {re}(Advanved + Fast)'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [7] Daily/Active Member Adder'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [8] Weekly Member Adder'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [9] Monthly Member Adder'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [10] Online Member Adder'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [11] Non Active Member Adder'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [12] OTP Viewer'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [13] Reaction Increaser'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [14] Shares Increaser'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [15] Change First Name, Last Name & Bio'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [16] Set Username'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [17] Set 2 Step'+n)
    print(Style.BRIGHT + Fore.CYAN+f'            [18] Scam Tag {re}[Special]'+n)
    print(Style.BRIGHT + Fore.CYAN+f'            [19] Bulk Message Sender {re}[special]'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [20] Set Profile Pic'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [21] Remove Profile Pic'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [22] Report Spam A User'+n)
    print(Style.BRIGHT + ye+'Additional Options:'+n)
    print(Style.BRIGHT + Fore.CYAN+f'            [23] Send DM {re}[pm spam]'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [24] Join channel/group '+n)
    print(Style.BRIGHT + Fore.CYAN+'            [25] Leave channel/group'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [26] Login by phone.csv'+n)
    print(Style.BRIGHT + ye+'Sub Menus/Advanced Features:'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[27] Nearby People Adder'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[28] OverPowered 3 Operations'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[29] vcf File Adder'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[30] Login Using Security - Safe Login'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[31] Telegram Sender'+n)
    print('            '+Style.BRIGHT + Fore.GREEN + Back.RED+'[32] Add by Gender'+n)
    print(Style.BRIGHT + ye+'Extra Options:'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [33] Extra Line Remover (csv)'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [34] Views Incrementor'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [35] Auto Group Creator'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [36] Group Chat Cloner'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [37] Limit Checker/Limit Remover v3'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [38] Account Info Checker'+n)
    print(Style.BRIGHT + ye+'Exit:'+n)
    print(Style.BRIGHT + Fore.CYAN+'            [0]  Exit'+n)
    a = int(input('\nEnter your choice: '))
    if a == 1:
        login()
    elif a == 2:
        BanFilter()
    elif a == 3:
        specificaccremove()
    elif a == 4:
        url = 'https://youtube.com/@TrickyAbhi2.0'
        brw = 'am start --user 0 -a android.intent.action.VIEW -d %s'
        cmd = brw % url
        os.system(cmd)
        print('opened by command:', repr(cmd), end='\n\n')
    elif a == 5:
        ramexadder()
    elif a == 6:
        hiddenadder()
    elif a == 7:
        ramexdaily()
    elif a == 8:
        ramexweekly()
    elif a == 9:
        ramexmonthly()
    elif a == 10:
        ramexonline()
    elif a == 11:
        ramexnonactive()
    elif a == 12:
        otpviewer()
    elif a == 13:
        reactionincreaser()
    elif a == 14:
        sharesincreaser()
    elif a == 15:
        changeraccount()
    elif a == 16:
        changerusername()
    elif a == 17:
        twostepverification()
    elif a == 18:
        ScamTag()
    elif a == 19:
        ramexsender()
    elif a == 20:
        setprofilepic()
    elif a == 21:
        removeprofilepic()
    elif a == 22:
        reportspamuser()
    elif a == 23:
        pmspamdm()
    elif a == 24:
        groupjoiner()
    elif a == 25:
        grouplefter()
    elif a == 26:
        loginbycsv()
    elif a == 27:
        nearbyadder()
    elif a == 28:
        opthree()
    elif a == 29:
        vcffiled()
    elif a == 30:
        loginusingsecurity()
    elif a == 31:
        tsender()
    elif a == 32:
        addusinggendert()
    elif a == 33:
        csvblankremover()
    elif a == 34:
        viewsincrement()
    elif a == 35:
        autogroupmaker()
    elif a == 36:
        groupchatcloner()
    elif a == 37:
        limicheckandrem()
    elif a == 38:
        accountinfogetter()
    elif a == 0:
        exit()
        

def nearbyadder():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Nearby Adding Options:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Add by Latitude & Longitude'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Add by City or Village Name'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] AutoAdder'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Exit'+n)
    b = int(input('\nEnter your choice: '))
    if b == 1:
        nearbyadderlatlong()
    elif b == 2:
        nearbyaddercity()
    elif b == 3:
        nearbyadderauto()
    elif b == 0:
        main_menu()
    elif b == 4:
        exit()


def nearbyadderauto():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Which Country Members you want to Add:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] India'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] USA'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Bangladesh'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Russia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[5] Ukraine'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[6] Pakistan or Iran'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[7] Bhutan or China'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[8] UK'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[9] Japan'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[10] Germany'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[11] Switzerland'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[12] Brazil'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[13] Indonesia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[14] Uzbekistan'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[15] Belgium'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[16] Cambodia or ThaiLand'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[17] Ethiopia'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[18] Nigeria'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[19] Turkey'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[20] Israel'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[21] Exit'+n)
    c = int(input('\nEnter your choice: '))
    if c == 1:
        nearbyadderautoindia()
    elif c == 2:
        nearbyadderautousa()
    elif c == 3:
        nearbyadderautobangladesh()
    elif c == 4:
        nearbyadderautorussia()
    elif c == 5:
        nearbyadderautoukraine()
    elif c == 6:
        nearbyadderautopakistan()
    elif c == 7:
        nearbyadderautobhutan()
    elif c == 8:
        nearbyadderautouk()
    elif c == 9:
        nearbyadderautojapan()
    elif c == 10:
        nearbyadderautogermany()
    elif c == 11:
        nearbyadderautoswitzerland()
    elif c == 12:
        nearbyadderautobrazil()
    elif c == 13:
        nearbyadderautoindonesia()
    elif c == 14:
        nearbyadderautouzbekistan()
    elif c == 15:
        nearbyadderautobelgium()
    elif c == 16:
        nearbyadderautocombodia()
    elif c == 17:
        nearbyadderautoethiopia()
    elif c == 18:
        nearbyadderautonigera()
    elif c == 19:
        nearbyadderautoturkey()
    elif c == 20:
        nearbyadderautoisrael()
    elif c == 0:
        nearbyadder()
    elif c == 21:
        exit()

def vcffiled():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Options For VCF File:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Extract VCF File number'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Add to Group'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Import Contact (Just Import Not Add to Contact)'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Exit'+n)
    d = int(input('\nEnter your choice: '))
    if d == 1:
        extractvcftonumb()
    elif d == 2:
        addtocontactbygroup()
    elif d == 3:
        addtocontactbyimp()
    elif d == 0:
        main_menu()
    elif d == 4:
        exit()

def tsender():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Group Message Sender:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Group Sender with - Multi Accounts (Threading)'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Group Sender wiith image - Multi Accounts (Threading)'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Group Sender with image - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[4] Group Sender with only Message - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[5] Group Sender - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[6] Group Sender with image - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Multi Group Message Sender:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[7] Multi Group Sender with image - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[8] Multi Group Sender - Multi Messages'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[9] Multi Group Sender with single image & message - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[10] Multi Group Sender with only message - Single Account'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Channel Post Forwarder:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[11] Auto Forwarder'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[12] Auto Forwarder (No Tag)'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Inbox Sender:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[13] Scraper'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[14] Send PM'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[15] Send PM with Image'+n)
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[16] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[17] Exit'+n)
    e = int(input('\nEnter your choice: '))
    if e==1:
        messagesendergroup()
    elif e==2:
        messagesendergrouppic()
    elif e==3:
        messagesendergrouppicsingle()
    elif e==4:
        messagesendergroupsingle()
    elif e==5:
        messagesendergroupmultimsg()
    elif e==6:
        messagesendergroupmultimsgpic()
    elif e==7:
        messagesendergroupmultimsgpicmultigroups()
    elif e==8:
        messagesendergroupmultimsgmultigroups()
    elif e==9:
        messagesendermultigroupsinglepic()
    elif e==10:
        messagesendermultigroupsingle()
    elif e==11:
        forward_to_channels()
    elif e==12:
        forward_to_channelsnotag()
    elif e==13:
        multi_ccraper()
    elif e==14:
        messagesendering()
    elif e==15:
        messagesenderingpic()
    elif e==16:
        main_menu()
    elif e==17:
        quit()

def addusinggendert():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Options For Adding With Gender Filter:'+n)
    print(f"{re}Note: {gr}This feature is still in Development so this will work only in big Chatting/Study Group")
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Male/Boy Adder'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Female/Girl Adder'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Exit'+n)
    f = int(input('\nEnter your choice: '))
    if f == 1:
        maleadderh()
    elif f == 2:
        femaleadderh()
    elif f == 0:
        main_menu()
    elif f == 3:
        exit()


def loginusingsecurity():
    clr()
    banner()
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Login Using Multiple Api and Hash with Device spoof:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[1] Login Type 1'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[2] Login by CSV'+n)
    print()
    print(f'{Style.BRIGHT + Fore.YELLOW + Back.RED}[+] Exit Option:'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[0] Go Back'+n)
    print(f'{Style.BRIGHT + Fore.CYAN}[3] Exit'+n)
    f = int(input('\nEnter your choice: '))
    if f == 1:
        logintypeone()
    elif f == 2:
        logintypetwo()
    elif f == 0:
        main_menu()
    elif f == 3:
        exit()

main_menu()