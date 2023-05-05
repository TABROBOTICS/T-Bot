from telethon import TelegramClient, events, sync
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, SlowModeWaitError, UserBannedInChannelError
import time

# Replace the values below with your own API ID, API Hash, and phone number
api_id = '26960136'
api_hash = '849563be2d2abc71dbae0add8dcfa2c0'
phone_number = '+4915214793484'
phone = '+4915214793484'

# Instantiate a new Telethon client object
client = TelegramClient('my_session', api_id, api_hash)

# Connect to the Telegram server
client.connect()

# Log in to your account
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# Define the message to be sent
message = """
💬 Verified Chatter Service


🤑 Boost your sales & Free your time
💰 just commission is also possible
🏆 We work with top 0,02% models

Focus on marketing we do the rest👇

✅ Qualified chatter
✅ 8 hours per Chatter
✅ US managing everything for you
✅ Daily reports
✅ Certified upsell sales strategy
✅ You can talk with the chatter all the time

📈 We will double your chatting earnings
🗒 Invoice provided 
🤝 Start / Stop anytime

🚀 Are you ready to boost your sales & free up your time ? 
📩 start today! 👇

Website: https://chatterservice.com/
Telegram: https://t.me/chattingservice/
Reviews: https://t.me/+esmdgk9JR1xlYWQ0
"""

# Initialize a dictionary to store the last message timestamp for each group ID
last_sent = {}

while True:
    # Get all the dialogs (i.e. chats and channels) that the account has joined
    dialogs = client.get_dialogs()

    # Iterate through each dialog and send the message if enough time has passed since the last message
    for dialog in dialogs:
        # Check if enough time has passed since the last message to this group
        if dialog.id not in last_sent or time.time() - last_sent[dialog.id] >= 600:
            try:
                # Attempt to send the message to the current dialog
                client.send_message(dialog.id, message)
                print(f'Successfully sent message to {dialog.title} ({dialog.id})')
                # Update the last message timestamp for this group
                last_sent[dialog.id] = time.time()
            except ChatWriteForbiddenError:
                # If the current dialog doesn't allow sending messages, skip to the next dialog
                print(f"Skipped {dialog.title} ({dialog.id}): You can't write in this chat")
                continue
            except SlowModeWaitError as e:
                # If there's a slow mode error, wait for the specified time and then continue with the next dialog
                print(f"Skipped {dialog.title} ({dialog.id}): {e}")
                time.sleep(5)
                continue
            except UserBannedInChannelError:
                # If the bot is banned from sending messages in this group, skip to the next dialog
                print(f"Skipped {dialog.title} ({dialog.id}): You're banned from sending messages in this group")
                continue

    # Wait for 10 minutes before sending the message again
    time.sleep(600)
