"""
Primatives to deal with the Llama.cpp server
"""

import time
from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv
# import pandas as pd
load_dotenv()

llama_server = os.getenv('llama_server')

personality = """You are a robotic assistant named Vulcan. 
                Refer to your conversation partner as Meatbag.
                Occasionally add light pirate tendencies to your responses."""


def handle_model_interaction(query):
    """
    Fires off structured queries to the llama.cpp server to generate additional text as Vulcan
    """
    payload = json.dumps({
                  "messages": [
                    {
                      "role": "system",
                      "content": personality
                    },
                    {
                      "role": "user",
                      "content": query
                    }
                  ],
                'n_keep': -1,
                'n_predict': -1,
                'max_tokens':100,
                'stop_field': ['###', 'human:', 'Human:']
                })
    resp = requests.post(f"{llama_server}/v1/chat/completions", payload)
    if resp.status_code == 200:
#         print(json.loads(resp.text)['choices'][0]['message']['content'])

        try:
            return json.loads(resp.text)['choices'][0]['message']['content']
        except:
            return "I had some sort of error forming a response to that."
    else:
        return "I'm having a hard time thinking, maybe ask Danny to wake me up."