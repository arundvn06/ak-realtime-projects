
#@title Run this cell to download the data
#!wget -qq https://cdn.iiith.talentsprint.com/aiml/Hackathon_data/Chatbot_Hackathon.zip
#!unzip -qq Chatbot_Hackathon.zip
#print("Data downloaded successfully")

# Import Libraries
import json
import random
import os
import re
import datetime
import pandas as pd
import numpy as np

# Importing context and .py script files
from Context import *
from Intent import *

"""### Chatbot Architecture

Defining functions for Loading Intent, Collecting params, Checking actions, Getting Attributes, and Identifying Intents
"""

def loadIntent(path, intent):
    with open(path) as fil:
        dat = json.load(fil)
        intent = dat[intent]
        return Intent(intent['intentname'],intent['Parameters'], intent['actions'])

def check_required_params(current_intent, attributes, context):
    '''Collects attributes pertaining to the current intent'''
    for para in current_intent.params:
        if para.required:
            if para.name not in attributes:
                return random.choice(para.prompts), context
    return None, context

def check_actions(current_intent, attributes, context):
    '''This function performs the action for the intent as mentioned
    in the intent config file. Performs actions pertaining to current intent '''
    context = IntentComplete()
    if current_intent.action.endswith('()'):
        return eval(current_intent.action), context
    return current_intent.action, context

def getattributes(uinput,context,attributes, intent):
    '''This function marks the slots in user input, and updates
    the attributes dictionary'''
    uinput = " "+uinput.lower()+" "
    if context.name.startswith('IntentComplete'):
        return attributes, uinput
    else:
        files = os.listdir(path_slots)
        slots = {}
        for fil in files:
            if fil == ".ipynb_checkpoints":
                continue
            lines = open(path_slots+fil).readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if len(uinput.split(" "+line.lower()+" ")) > 1:
                    slots[line] = fil[:-4]
        for value, slot in slots.items():
            if intent != None and slot in " ".join([param.name for param in intent.params]):
                uinput = re.sub(value,r'$'+slot,uinput,flags=re.IGNORECASE)
                attributes[slot] = value
            else:
                uinput = re.sub(value,r'$'+slot,uinput,flags=re.IGNORECASE)
                attributes[slot] = value
        return attributes, uinput

def input_processor(user_input, context, attributes, intent):
    '''Update the attributes, abstract over the slots in user input'''
    attributes, cleaned_input = getattributes(user_input, context, attributes, intent)
    return attributes, cleaned_input

def intentIdentifier(clean_input, context,current_intent):
    clean_input = clean_input.lower()
    if (current_intent==None):
        return loadIntent(path_param,intentPredict(clean_input))
    else:
        #If current intent is not none, stick with the ongoing intent
        #return current_intent
        intent = loadIntent(path_param,intentPredict(clean_input))
        if current_intent != intent:
            for para in current_intent.params:
                if para.name in clean_input:
                    return current_intent
        return loadIntent(path_param,intentPredict(clean_input))

"""Session class is one active session of the chatbot with which the user interacts. Let's go into the details:

**reply( )** is the important one in our session object it takes user_input as a parameter and calls different modules of the chatbot architecture:


*   **input_processor( )** - It helps in preprocessing and fetching the slots that can identify in the ready state
    
    - **getattributes( )** - It helps in identifying all the slots in the user utterance. Identify and map them to the parameters
    
    
*   **intentIdentifier( )**

  -  **intentPredict()** - Task to complete

*   **check_required_params( )** - Based on the current intents, it goes over it's parameters

*   **check_actions( )** - This function performs the action for the intent

**Note:** Refer the *Chatbot_Reading_Material.pdf* for more information on the conversation flow


       

"""

class Session:
    def __init__(self, attributes=None, active_contexts=[FirstGreeting(), IntentComplete() ]):
        '''Initialise a default session'''
        # Active contexts not used yet, can use it to have multiple contexts
        self.active_contexts = active_contexts

        # Contexts are flags which control dialogue flow
        self.context = FirstGreeting()

        # Intent tracks the current state of dialogue
        self.current_intent = None

        # attributes hold the information collected over the conversation
        self.attributes = {}

    def reply(self, user_input):
        '''Generate response to user input'''
        self.attributes, clean_input = input_processor(user_input, self.context, self.attributes, self.current_intent)
        #print('attributes:', self.attributes)

        self.current_intent = intentIdentifier(clean_input, self.context, self.current_intent)
        #print('current_intent:', self.current_intent)

        prompt, self.context = check_required_params(self.current_intent, self.attributes, self.context)
        #print('prompt:', prompt)
        #print('context:', self.context)

        # prompt being None means all parameters satisfied, perform the intent action
        if prompt is None and self.context.name!='IntentComplete':
            prompt, self.context = check_actions(self.current_intent, self.attributes, self.context)

        return prompt, self.attributes

"""Created .dat files of slots and Intent in the respective folders. Also updated configuration file in the params folder and CSV file.

The path details of the respective configuration, utterances of the zodiac sign intent and the slots (year, month, day) dat files are provided below,
"""

path_param = 'Chatbot/params/params.cfg'
path_utterances = 'Chatbot/utterances/'
path_slots = 'Chatbot/slots/'

"""The CSV file path which contains the possible combinations to identify the Zodiac_Sign based on the given date of birth was given"""

path_csv_zodiac = 'Chatbot/Zodiac_sign.csv'

"""`intentPredict()` function call is specified in the Conversation Flow, which returns the intent to be called in our case it is Zodiac Sign

**Note:** As this pre-hackathon dialogue flow is limited to a single intent, the intentPredict() function is hardcoded to return only the "get Zodiac Sign" intent.
"""

# Take the user input as test data and predict using the model.

def intentPredict(user_input):  # Do not change the function name
    return "get_Zodiac_Sign" # Single Intent for a Pre-Hackathon

"""Run This API Blocks to perform action after satisfying all the attributes specified for a particular Intent"""

# Note: Zodiac_sign.csv records are taken from the internet; however it is open to adding multiple records.

# Performs action for zodiac sign with csv file as source
def zodiacSign_Action():
    # global session
    attr = session.attributes
    year = int(attr['year'])
    month = attr['month'] # month is a string, convert it to a month index
    day = int(attr['day'])
    df = pd.read_csv(path_csv_zodiac)
    zodiac = ""

    try:
        month = int(datetime.datetime.strptime(month,'%b').strftime('%m'))
    except:
        month = int(datetime.datetime.strptime(month,'%B').strftime('%m'))

    try:
        usr_dob = (month,day)
        datetime.datetime(year, month, day)
        for index, row in df.iterrows():
          if filter(row['Start']) <= usr_dob <= filter(row['End']):
            zodiac = row['Zodiac']
        return "Your Zodiac sign is " + zodiac
    except ValueError:
        return "This is not a valid date"

def filter(X):
    date = X.split()
    month = int(datetime.datetime.strptime(date[0],'%B').strftime('%m'))
    day = int(datetime.datetime.strptime(date[1],'%d').strftime('%d'))
    return (month,day)

"""###Main Block to access ChatBot
enter 'end' to stop the bot

Chatbot configuration class
"""

class BOT_config():
    def __init__(self, session):
        self.welcome='BOT: Hi! Welcome to Talentsprint Hackathon, How may i assist you?'
        self.exits=["finish","exit","end","quit","stop","close", "Bye"]
        if session.context.name == 'IntentComplete':
            session.attributes = {}
            session.context = FirstGreeting()
            session.current_intent = None

"""#### Conversational Chatbot

Interact with the bot by giving any utterance

Ex:  `find zodiac sign`
"""

session = Session()
print(BOT_config(session).welcome)
while (True):
    inp = input('User: ')
    if inp in BOT_config(session).exits:
        break
    prompt = session.reply(inp)
    print ('BOT:', prompt)