# Text Messages Clipboard

## This is a python script that copies messages to the clipboard based on the text key the user provides
## It makes use of the pyperclip module for copying the text and sys module for accessing and storing the command line arguments, shelve module to store the newly created messages and keyphrases

### There is also a batch file that runs with the Command Line.

## How it works
- stores last copied text under a key phrase
- adds it to the default key phrases which are stored in a file created by the  shelve module
- copies the message to the clipboard when the key is passed
