from googletrans import Translator, constants
from pprint import pprint

# take in mytext as a command line argument with selected language. 
#translate to language 
# return data to main

def translate_speech(speech):
    translator = Translator()
    translation = translator.translate(speech, src='en', dest = 'es')
    print(f'{translation.origin}({translation.src})--> {translation.text} ({translation.dest})')
