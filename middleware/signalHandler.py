"""
Primatives to deal with the Signal Messenger API
"""

import time
from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

SIGNAL_API_URL = os.getenv('SIGNAL_API_URL')
mynumber = os.getenv('mynumber')


def flatten_json(y):
    """
    Turns nested JSON into flat JSON. 
    Not confined to Singal-specific use cases, so it may move to a new area later.
    """
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def get_new_messages():
    """
    Poll the Signal API for new messages to handle
    """
    newmessages = requests.get(f"{SIGNAL_API_URL}/v1/receive/{mynumber}")

    if newmessages.status_code != 200:
        # TODO: Logging
        # logging.warning('Error contacting signal API')
        pass

    return json.loads(newmessages.text)


def update_groups():
    """
    Updates a dictionary with known internal and external IDs for groups
    You could add a global var to handle the group updates all in one function
    """
    resp = requests.get(f"{SIGNAL_API_URL}/v1/groups/{mynumber}")

    if resp.status_code == 200:
        groups = json.loads(resp.text)

        groupdict = {}
        for group in groups:
            groupdict[group['internal_id']] = {'name': group['name'], 'id': group['id']}

        return groupdict


"""
TODO: Figure out a better place to put this. Does it need to be handled in the package, or at runtime?

You need to populate Groupdict once, so it knows what groups Vulcan is in.
"""
updated_groups = update_groups()
if updated_groups != None:
    groupdict = updated_groups


def send_response(target, text):
    """
    Fires off a simple response via the Signal API
    
    Args:
        target: string of number (with area code), or global group id
        text: Text to inject into the response. Supports Emojis
    """
    content = json.dumps({"message": text,
                          "number": mynumber,
                          "recipients": [target]})

    requests.post(f"{SIGNAL_API_URL}/v2/send", content)


def convert_envelope(message_json_flattened):
    """
    Convert 'envelopes' (messages, in the terminology of the Signal API) from 
    a verbose JSON to just the bits I want.
    """

    ## handle emojis and "read" messages
    # you could also add a check for syncMessage as a key before flattening?
    if 'envelope_dataMessage_message' not in message_json_flattened:
        return
    if message_json_flattened['envelope_dataMessage_message'] == None:
        return

    outdict = {}
    outdict['timestamp'] = message_json_flattened['envelope_timestamp']
    outdict['sourceNumber'] = message_json_flattened['envelope_sourceNumber']
    outdict['sourceUUID'] = message_json_flattened['envelope_sourceUuid']
    outdict['sourceName'] = message_json_flattened['envelope_sourceName']
    outdict['message'] = message_json_flattened['envelope_dataMessage_message']

    ## Handle groups vs direct messages
    if 'envelope_dataMessage_groupInfo_groupId' in message_json_flattened.keys():
        group_type = 'group'
        ## You might need to inject the group_ to this key to respond directly to groups
        outdict['thread'] = groupdict[message_json_flattened['envelope_dataMessage_groupInfo_groupId']]['id']
        outdict['thread_friendly_name'] = groupdict[message_json_flattened['envelope_dataMessage_groupInfo_groupId']][
            'name']

    else:
        group_type = 'direct'
        outdict['thread'] = message_json_flattened['envelope_sourceNumber']
        outdict['thread_friendly_name'] = message_json_flattened['envelope_sourceName']

    outdict['chatType'] = group_type

    return outdict


def get_clean_new_envelopes():
    new_envelopes = get_new_messages()
    if new_envelopes != []:
        converted_new_envelopes = [convert_envelope(flatten_json(i)) for i in new_envelopes]

        while None in converted_new_envelopes:
            converted_new_envelopes.remove(None)
        #         if converted_new_envelopes == []:
        #             pass
        return converted_new_envelopes
    else:
        return []


def filter_to_relevant_messages(messages, wakeword):
    """
    Filter messages to only the ones that would wake up your chatbot
    """
    wakeword = wakeword.lower()
    return [i for i in messages if wakeword in i['message'].lower()]


def clean_envelope_to_raw_messages(envelope_list):
    """
    Return message str only, from a cleaned envelope dict
    """
    return [message['message'] for message in envelope_list]


def save_msg_envelopes(envelopes, logfile='signal_messages.log'):
    """
    Bootleg message logging to file
    """
    if type(envelopes) == str:
        envelopes = [envelopes, ]
    with open(logfile, 'a') as f:
        [f.write(f"{x}\n") for x in envelopes]
