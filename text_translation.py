from googletrans import Translator, constants
from pprint import pprint


def translate_speech(speech):
    translator = Translator()
    translation = translator.translate(speech, src='en', dest = 'es')
    print(f'{translation.origin}({translation.src})--> {translation.text} ({translation.dest})')
