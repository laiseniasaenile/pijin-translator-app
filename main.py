import csv
import justpy as jp
import pyttsx3


class DictionaryApp:
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
        else:
            self.meaning_box.text = 'Getting the translation'

    def speak_word(self, msg):
        text_to_speak = self.meaning_box.text

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speaking rate (optional)
        engine.say(text_to_speak)
        engine.runAndWait()

    def home(self):
        wp = jp.QuasarPage(tailwind=True)

        navbar = jp.Div(classes='bg-primary text-white p-2')
        navbar.text = '''English to Solomon Island Pijin translator'''

        main_div = jp.Div(classes='q-ma-md bg-green-700 min-h-screen p-8')
        input_div = jp.Div(classes='q-mb-md flex items-center')
        search_box = jp.Input(a=input_div, placeholder='Type here...', classes='q-mb-md filled-autogrow py-2 px-4')
        search_box.on('input', self.search_word)
        self.meaning_box = jp.Div(text='', classes='q-mt-lg')
        speak_button = jp.Button(text='Audio', classes='q-mb-md border-2 m-2 rounded w-full', type="secondary")
        speak_button.on('click', self.speak_word)
        checkbox_div = jp.Div(classes='q-mt-md flex items-center')
        checkbox = jp.Input(type='checkbox', classes='mr-2')
        checkbox_text = jp.P(text='Pijin to English', classes='text-white')

       # input_div.add(search_box)
        checkbox_div.add(checkbox, checkbox_text)
        main_div.add(input_div, self.meaning_box, speak_button, checkbox_div)
        wp.add(navbar, main_div)

        return wp

    def home_page(self, msg):
        jp.justpy(self.home)


app = DictionaryApp()
jp.justpy(app.home)
