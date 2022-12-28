#!
"""This is a program that copies often used text for email messages to the clipboard"""

messages = {'greet': "Heyoo, \nHow are you today?", "busy": "Please call me back later, I'm busy right now", 'assignment': "I'm doing my assignments right now. I'll contact you later 😊", 'class': "I'm in a class right now, I'll call you back later🙂"}

import pyperclip, sys

if len(sys.argv) < 2: # the arguments apart from python
    print("Usage: python multi_clip.py [keyphrase] - copy text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in messages:
    pyperclip.copy(messages[keyphrase]) # copy the text for that key
    print(f'Text for - {keyphrase} copied to clipboard')
else:
    print(f"There's no message for {keyphrase}") # message does not exist
    print(f"Please try again with a correct message key\nYou only have {len(messages.keys())}: ", end='')
    for key in messages.keys():
        print(key, end=' ')