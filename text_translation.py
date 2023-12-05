from googletrans import Translator, constants
from pprint import pprint


def translate_speech(speech, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(speech, src=src_lang, dest = dest_lang)
    print(f'{translation.origin}({translation.src}) translates to: {translation.text} ({translation.dest})')
    translated_speech = f'{translation.text}'
    return translation_speech
