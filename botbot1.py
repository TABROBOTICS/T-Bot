from telethon import TelegramClient, events, sync
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, SlowModeWaitError
import time

# Replace the values below with your own API ID, API Hash, and phone number
api_id = '26960136'
api_hash = '849563be2d2abc71dbae0add8dcfa2c0'
phone_number = '+4915214793484'

# Instantiate a new Telethon client object
client = TelegramClient('my_session', api_id, api_hash)

# Connect to the Telegram server
client.connect()

# Log in to your account
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

# Define the message to be sent
with open('message.txt', 'r') as f:
    message = f.read().strip()

# Get the group links from a file
with open('groups.txt') as f:
    for line in f:
        group_link = line.strip()
        try:
            entity = client.get_entity(group_link)
            client.send_message(entity, message)
            print(f"Successfully sent message to {group_link}")
        except Exception as e:
            print(f"Skipping {group_link}: {e}")
            continue

# Disconnect the client
client.disconnect()
