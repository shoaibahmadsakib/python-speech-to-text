from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

# specify source language
translation = translator.translate("Wie gehts ?", src="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")