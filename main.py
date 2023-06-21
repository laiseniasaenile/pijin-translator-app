import csv
import justpy as jp
import pyttsx3


class DictionaryApp:
    def __init__(self):
        self.background_audio = jp.Audio(src='sounds/creative_minds.mp3', autoplay=True, loop=False)

    def search_word(self, msg):
        word = msg.value
        meaning = ''

        with open('dictionary.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Word'] == word:
                    meaning = row['Meaning']
                    break

        if meaning:
            self.meaning_box.text = f"In Pigin: {meaning}"
            self.meaning_box.classes = 'q-mt-lg text-white'
        else:
            self.meaning_box.text = 'Please type in any English word or sentence'
            self.meaning_box.classes = 'q-mt-lg text-white'

    def speak_word(self, msg):
        text_to_speak = self.meaning_box.text

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speaking rate (optional)
        engine.say(text_to_speak)
        engine.runAndWait()

    # reverse the web app
    def search_word_pigin(self, msg):
        word_pig = msg.value
        meaning_pig = ''

        with open('dictionary_2.csv', 'r') as csvfile_2:
            reader_2 = csv.DictReader(csvfile_2)
            for row in reader_2:
                if row['word_pig'] == word_pig:
                    meaning_pig = row['meaning_pig']
                    break

        if meaning_pig:
            self.meaning_box_pijin.text = f"In English: {meaning_pig}"
            self.meaning_box_pijin.classes = 'q-mt-lg text-white'
        else:
            self.meaning_box_pijin.text = 'Please type in any Pigin word or sentence'
            self.meaning_box_pijin.classes = 'q-mt-lg text-white'

    def speak_word_2(self, msg):
        text_to_speak_2 = self.meaning_box_pijin.text

        engine = pyttsx3.init()
        # Set the voice
        voices = engine.getProperty('voices')

        for voice in voices:
            print(voice.name)

        voices = engine.getProperty('voices')
        voice_index = 1
        engine.setProperty('rate', 150)  # Adjust the speaking rate (optional)
        engine.setProperty('voice', voices[voice_index].id)  # Adjust the speaking rate (optional)
        engine.say(text_to_speak_2)
        engine.runAndWait()

    def home(self):
        wp = jp.QuasarPage(tailwind=True)

        navbar = jp.Div(classes='bg-gradient-to-r from-blue-800 via-yellow-300 to-green-800 text-white p-2')
        navbar.style = 'position: fixed; top: 0 ;padding-top:2; left: 0; right: 0; z-index: 9999; height: 56px;font-size: 25px; font-weight: bold;'
        navbar.text = '''English to Solomon Island Pijin translator'''

        # Div for explaining the web app
        info_div = jp.Div(classes='text-white my-4 ')
        info_div.style ='font-size:15px;'
        info_div.text = '''
                       Welcome to the English to Solomon Island Pijin translator!
                       This app helps you translate English words and phrases into Pijin and vice versa.
                       Side note some pijin words are spelled to maximise the desirable pronunciation,thus 
                       the translations may be different from pijin word's used in books etc. 
                       Simply type in the English and the Pijin in the respective input fields
                       and get the corresponding Pijin/Eglish 
                       translation in the output boxes. You can also click on the "Audio in Pijin" & Audio in English
                       buttons to hear the Pijin/Eglish translation spoken out loud. Enjoy translating!'''

        main_div = jp.Div(classes='bg-gradient-to-r from-blue-800 via-yellow-300 to-green-800 min-h-screen p-8')
        main_div.style = 'margin-top: 56px; margin-left: 0px;padding-top:2; top: 0; padding-left: 10; padding-right:10; bottom: 0;position: relative; overflow-y: auto; width:100%'




        input_div = jp.Div(classes='q-mb-md flex items-center')
        search_box = jp.Input(a=input_div, placeholder='Type English here...',
                              classes='q-mb-md filled-autogrow py-2 px-4 bg-yellow-300')
        search_box.style = 'width: 15cm;'
        search_box.on('input', self.search_word)
        self.meaning_box = jp.Div(text='', classes='q-mt-lg')
        speak_button = jp.Button(style='width: 10cm; height: 2rem;',
                                 classes='q-mb-md border-4 m-2 rounded w-full text-white bg-blue w-300 h-7')

        speak_icon = jp.Icon(classes='q-mr-xs', icon='ri-volume-up-fill', style='color: white')
        speak_text = jp.Span(text='Audio in pigin')
        speak_button.add(speak_icon, speak_text)

        speak_button.on('click', self.speak_word)
        checkbox_div = jp.Div(classes='q-mt-md flex items-center')
        checkbox = jp.Input(type='checkbox', classes='mr-2')
        checkbox_text = jp.P(text='Pijin to English', classes='text-white')

        input_div2 = jp.Div(classes='q-mb-md flex items-center')
        search_box_pijin = jp.Input(a=input_div2, placeholder='Type Pijin here...',
                                    classes='q-mb-md filled-autogrow py-2 px-4 bg-yellow-300')
        search_box_pijin.style = 'width: 15cm;'
        search_box_pijin.on('input', self.search_word_pigin)
        self.meaning_box_pijin = jp.Div(text='', classes='q-mt-lg')
        speak_button_2 = jp.Button(text='Audio in English', style='width: 10cm; height: 2rem;',
                                   classes='q-mb-md border-4 m-2 rounded text-white bg-blue w-300 h-7',
                                   type="secondary")
        speak_button_2.on('click', self.speak_word_2)

        # Footer with Facebook and Instagram links
        footer = jp.Div(
            classes='bg-gradient-to-r from-blue-800 via-yellow-300 to-green-800 text-white p-2 fixed inset-x-0 bottom-0')
        facebook_icon = jp.Icon(classes='q-mr-xs', icon='ri-facebook-fill', style='color: white')
        instagram_icon = jp.Icon(classes='q-mr-xs', icon='ri-instagram-fill', style='color: white')
        facebook_link = jp.A(classes='q-mx-xs', href='https://www.facebook.com/', target='_blank',
                             rel='noopener noreferrer')
        instagram_link = jp.A(classes='q-mx-xs', href='https://www.instagram.com/', target='_blank',
                              rel='noopener noreferrer')
        facebook_link.add(facebook_icon)
        instagram_link.add(instagram_icon)
        footer.add(facebook_link, instagram_link)

        main_div.add(info_div,input_div, self.meaning_box, speak_button, input_div2, speak_button_2, self.meaning_box_pijin,
                    footer)
        wp.add(navbar, main_div)
        # input_div.add(search_box)
        # checkbox_div.add(checkbox, checkbox_text)
        #main_div.add(input_div, self.meaning_box, speak_button, input_div2, speak_button_2, self.meaning_box_pijin)
        #wp.add(navbar, main_div, self.background_audio)
        #audio_element = jp.Audio(src='//creative_minds.mp3', autoplay=True)
        #main_div.add(input_div, self.meaning_box, speak_button, input_div2, speak_button_2, self.meaning_box_pijin,
                     #audio_element)
        #wp.add(navbar, main_div)

        return wp

    def home_page(self, msg):
        jp.justpy(self.home)


app = DictionaryApp()
jp.justpy(app.home)
