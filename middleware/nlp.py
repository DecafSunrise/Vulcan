from textblob import TextBlob

def check_nice_message(text, polarity=.2):
    """
    Checks if a message contains positive sentiment. 
    Defaults to any message >= .2 (out of -1 through +1) is positive
    """
    blob = TextBlob(text.lower().replace("vulcan", '').strip(",").strip())
    if blob.sentences[0].sentiment.polarity >= polarity:
        return True
    else:
        return False