#!
"""This is a program that copies often used text for email messages to the clipboard"""

import pyperclip, pprint, sys, shelve

default_messages = {'greet': "Heyoo, \nHow are you today?", "busy": "Please call me back later, I'm busy right now", 'assignment': "I'm doing my assignments right now. I'll contact you later 😊", 'class': "I'm in a class right now, I'll call you back later🙂"}

# open messages shelf
my_shelf = shelve.open('messages')

if not('messages' in my_shelf.keys()):
    my_shelf['messages'] = default_messages

messages = my_shelf['messages']
my_shelf.close()
    

if len(sys.argv) < 2: # the arguments apart from py
    print("Usage: py multi_clip.py [keyphrase] - copy text")
    print("Usage: py multi_clip.py save [keyphrase] - save new text with a keyphrase")
    print("Usage: py multi_clip.py list - list available keys.\nCopy a list of available keys to the clipboard")
    sys.exit()

if len(sys.argv) == 2:
    keyphrase = sys.argv[1]

    if keyphrase in messages and not(keyphrase == 'list'):
        pyperclip.copy(messages[keyphrase]) # copy the text for that key
        print(f"Text for '\033[1;3m{keyphrase}'\033[0m copied to clipboard")        
    elif keyphrase == 'list': # list available keys
        print(f"You have {len(messages.keys())} message keys: ")
        for key in messages.keys():
            pyperclip.copy(str(list(messages.keys())))
            print(f"- {key}", end='\n')
    else:
        print(f"The key '{keyphrase}' does not exist. \n Enter the command '\033[1;3m'py multi_clip.py list'\033[0m' to see available keys") # message does not exist

# add save key that saves to the shelf
if len(sys.argv) == 3:
    action, keyphrase = sys.argv[1:]
    message = pyperclip.paste()

    if action == 'save':
        my_shelf = shelve.open('messages')
        default_messages[keyphrase] = message
        my_shelf['messages'] = default_messages
        print(f"Text for '\033[1;3m{keyphrase}'\033[0m added to messages")

my_shelf.close() # close the shelf file