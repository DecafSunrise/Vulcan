
from middleware.signalHandler import send_response, get_clean_new_envelopes, filter_to_relevant_messages
from middleware.signalHandler import update_groups

# from middleware import signalHandler
# from middleware.llmHandler import check_rude_message
# from middleware.nlp import check_nice_message
# from middleware.sampleMessages import all_samples
# from middleware.llmHandler import handle_model_interaction
# from middleware import signalHandler, llmHandler, emotionalStateMachine, nlp
# import pandas as pd
# import json
import pyfiglet
result = pyfiglet.figlet_format("Vulcan", font = "slant")
print(result,"- A Weirdly Emotional Chatbot -")
import time

import os
from dotenv import load_dotenv
load_dotenv()

"""
This is silly, but the bot is listening to a chat called "Vulcan's Bar Mitzvah"...
"""

group_barmitzvah = os.getenv('group_barmitzvah')
group_privateTest = os.getenv('group_privateTest')


from middleware.emotionalStateMachine import emotional_state, formatted_reply


## Handle group updates
updated_groups = update_groups()
if updated_groups != None:
    groupdict = updated_groups
#     del updated_groups
print(groupdict)

vulcan = emotional_state()

print(vulcan)
img_path = "./mood_graph.png"
vulcan._graph().write_png(img_path)

while True:
    new_envs = get_clean_new_envelopes()
    filtered_envs = filter_to_relevant_messages(new_envs)
    if len(filtered_envs) > 0:
        print(f"{len(filtered_envs)} new messages")
        for message in filtered_envs:
            thread = message['thread']
            message = message['message']

            # Generate response
            llm_response = formatted_reply(message, sm=vulcan)
            ## fire response
            send_response(target=thread, text=llm_response)

        print(vulcan.mood_stats())
        print("-------\n\n")
        vulcan._graph().write_png(img_path)
    time.sleep(15)