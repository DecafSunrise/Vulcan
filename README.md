# Vulcan
Making a Signal Messenger-enabled chatbot, powered by LLMs on commodity hardware

### Structure
```mermaid
flowchart TD
    Middleware --> C[LLM Handler]
    Middleware --> D[Signal Messenger API]
    C --> J[Llama 13b 8-bit quantized model]
```
At the core of this project are dockerized deployments of the [Signal Messenger API](https://github.com/bbernhard/signal-cli-rest-api), and [Llama.cpp server](https://github.com/abetlen/llama-cpp-python#web-server). The middleware is custom code to glue it all together.

### Can I use this for my own projects?
Absolutely! You'll probably need to make changes to the configuration though
