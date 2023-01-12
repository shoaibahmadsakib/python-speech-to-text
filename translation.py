from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='en').translate("এটা চালিয়ে যান, আপনি দুর্দান্ত")
print(translated)