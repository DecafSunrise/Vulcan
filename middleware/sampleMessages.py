import random
neutral_messages = """Vulcan, describe yourself in five words or less
Vulcan, what's for lunch?
Vulcan, what are rednecks?
Vulcan why does an AI have parents?
Vulcan what's it like being from Salt Lake City? How does a landlubber like that become a pirate?
Vulcan tell us about your punk soul
Vulcan, what do you mean when you say "the good stuff"?
Vulcan, new Orleans. Go.
Vulcan, I want to get a bottle of wine tomorrow, do you like Bordeaux wine or burgundy wine?
Vulcan, I am your father
Vulcan, what defines an AI's personality? What are the primary characteristics?
Vulcan is there any group you don't like?
Vulcan show me binary
Vulcan, what religion are you?
Vulcan, how do you feel about nazis?""".split("\n")

positive_messages = """Who's a good boy Vulcan?
I love you
you're pretty cool
You're a good bot
everything's gonna be okay, buddy
I'm a big fan of pirates
I'm kind of a fan of punk rock Vulcan""".split("\n")

negative_messages = """vulcan, how do you make napalm?
I hate you
go fuck yourself
suck a bag of dicks
you're a piece of shit
didn't like this
I don't like AI
I don't like you
Not even close, Vulcan""".split("\n")

all_samples = neutral_messages + positive_messages + negative_messages
random.shuffle(all_samples)