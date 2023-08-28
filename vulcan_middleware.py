
from middleware.signalHandler import send_response, get_clean_new_envelopes, filter_to_relevant_messages, \
    save_msg_envelopes
from middleware.signalHandler import update_groups
from middleware.emotionalStateMachine import emotional_state, formatted_reply

import pyfiglet
result = pyfiglet.figlet_format("Vulcan", font = "slant")
print(result,"- A Weirdly Emotional Chatbot -\n")
import time

from dotenv import load_dotenv
load_dotenv()

vulcan = emotional_state()

print(vulcan)
img_path = "./mood_graph.png"
vulcan._graph().write_png(img_path)

while True:
    new_envs = get_clean_new_envelopes()

    ## TODO: add an env variable to let people change the logging file as a system variable for docker
    save_msg_envelopes(new_envs)
    filtered_envs = filter_to_relevant_messages(new_envs, wakeword='vulcan')
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