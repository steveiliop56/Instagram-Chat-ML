import json

def is_unicode_escaped(text):
    try:
        decoded_text = text.encode().decode("unicode_escape")
        return decoded_text != text
    except UnicodeDecodeError:
        return False

def get_message(messages, sender_username):
    messages_list = []
    for item in messages:
        sender = item["sender_name"]
        if is_unicode_escaped(sender) == True:
            sender = sender.encode('latin-1').decode('utf-8')
        else:
            sender = sender
        if sender == sender_username:
            try:
                message = item["content"]
                if is_unicode_escaped(message) == True:
                    messages_list.append(message.encode('latin-1').decode('utf-8'))
                else:
                    messages_list.append(message)
            except:
                pass
    return messages_list

def get_usernames(json_data):
    usernames_raw = []
    for user in json_data["participants"]:
        usernames_raw.append(user["name"])

    usernames = []
    for user in usernames_raw:
        if is_unicode_escaped(user):
            usernames.append(user.encode('latin-1').decode('utf-8'))
        else:
            usernames.append(user)

    return usernames

path = "data_raw/other/gkioka.json"
dm = open(path)
dm_data = json.load(dm)

messages = dm_data.get("messages", [])
usernames = get_usernames(dm_data)

for username in usernames:
    user_messages = get_message(messages, username)
    user_file = open(f"data/{username}.txt", "x")
    for message_final in user_messages:
        user_file.write(f"{message_final}\n")
    user_file.close()

dm.close()
