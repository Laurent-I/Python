from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('test2.txt', mode='r') as my_file:
        text = my_file.read
        translation = translator.translate(text)
        print(translation)

        with open('test-ja.txt', mode='r') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('Check your file path')
