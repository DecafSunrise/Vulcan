# Vulcan
Making a Signal Messenger-enabled chatbot, powered by LLMs on commodity hardware  

### Structure:
```mermaid
flowchart TD
    Middleware --> C[LLM Handler]
    Middleware --> D[Signal Messenger API]
    Middleware --> E[Emotional State Machine]
    Middleware --> F[NLP]
    Middleware --> G[sampleMessages]
    C --> J[Llama 13b 8-bit quantized model]
```
At the core of this project are dockerized deployments of the [Signal Messenger API](https://github.com/bbernhard/signal-cli-rest-api), and [Llama.cpp server](https://github.com/abetlen/llama-cpp-python#web-server). The middleware is custom code to glue it all together.

### Chatbot Personality:
The "personality" is defined by prompt injection in the LLM handler file. Currently Vulcan is set to act as a robotic pirate.  
![image](https://github.com/DecafSunrise/Vulcan/assets/36832027/68265ad0-ba9b-4952-bfd5-a4413de3e895)

### Emotional State:
The emotional state is managed by a state machine (defined below). 
- If he gets a rude message, it'll have a chance to get 'Angry' or 'Sad'.
- If he recieves a compliment, his mood improves.
- If he gets too many boring messages in a row, he gets "bored" and asks a question.
![image](https://github.com/DecafSunrise/Vulcan/assets/36832027/fc815b57-37b7-4007-96f0-990021980607)

### Can I use this for my own projects?:
Absolutely! You'll probably need to make changes to the configuration though

### Sample Messages:
![image](https://github.com/DecafSunrise/Vulcan/assets/36832027/fd9a4184-68f5-4b84-8d34-589ebd019726)
![image](https://github.com/DecafSunrise/Vulcan/assets/36832027/5871a84a-75f2-4668-a209-e8c3a22bb44f)
![image](https://github.com/DecafSunrise/Vulcan/assets/36832027/edd4723c-12a3-4e13-9723-27574763c39f)


### Next steps:
- ~~State machine to simulate "moods"~~
- Personality tuning
    - Allow high reputation conversational partners to influence the personality
- ~~Proper logging of messages~~
- Fine-grained control of which Signal chats to respond to
    - ~~Reply to new chats by default, on wakeword~~
- Memory
    - Short term/conversational memory
    - Long term/database memory
