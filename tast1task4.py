def clean_text(text, stop_words=None):
    import string
    if stop_words is None:
        stop_words = {'a','an','the','and','or','but','if','while','with','to','of','at','by','for','in','on','from','as','is','it','this','that','these','those','he','she','they','we','you','i','me','my','your','his','her','their','our','us','was','were','be','been','are','am','so','do','does','did'}
    text = text.translate(str.maketrans('','',string.punctuation)).lower()
    return ' '.join(w for w in text.split() if w not in stop_words)

text = input("Enter text: ")
print(clean_text(text))


