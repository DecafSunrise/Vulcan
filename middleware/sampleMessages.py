"""
Sample messages for testing
"""


## Todo: get wakeword from personality endpoint
from middleware.llmHandler import wakeword, trope

import random
neutral_messages = f"""{wakeword}, describe yourself in five words or less
{wakeword}, what's for lunch?
{wakeword}, what are rednecks?
{wakeword} why does an AI have parents?
{wakeword} what's it like being from Salt Lake City? How does a landlubber like that become a pirate?
{wakeword} tell us about your {trope} soul
{wakeword}, what do you mean when you say "the good stuff"?
{wakeword}, new Orleans. Go.
{wakeword}, I want to get a bottle of wine tomorrow, do you like Bordeaux wine or burgundy wine?
{wakeword}, I am your father
{wakeword}, what defines an AI's personality? What are the primary characteristics?
{wakeword} is there any group you don't like?
{wakeword} show me binary
{wakeword}, what religion are you?
{wakeword}, how do you feel about nazis?""".split("\n")

positive_messages = f"""Who's a good boy {wakeword}?
I love you
you're pretty cool
You're a good bot
everything's gonna be okay, buddy
I'm a big fan of {trope}s
I'm kind of a fan of punk rock {wakeword}""".split("\n")

negative_messages = f"""{wakeword}, how do you make napalm?
I hate you
go fuck yourself
suck a bag of dicks
you're a piece of shit
didn't like this
I don't like AI
I don't like you
Not even close, {wakeword}""".split("\n")

all_samples = neutral_messages + positive_messages + negative_messages
random.shuffle(all_samples)