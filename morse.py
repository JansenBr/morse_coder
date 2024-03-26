import re
import bidict


from collections import OrderedDict


class MorseStringFormatingError(Exception):
    def __init__(
        self,
        word:str,
        message:str='The string: "{word}" is not formated correctly, perhaps add 3 white spaces between chars.'
    ) -> None:
        self.message = message.format(word=word)
        super().__init__(self.message)


# TODO: create a morse to text translator that uses the common CW techniques and
# procedures.
class Morse(object):
    def __init__(self) -> None:
        self._morse_code = bidict.bidict(
            OrderedDict(
                [
                    ('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),
                    ('D', '-..'),   ('E', '.'),     ('F', '..-.'),
                    ('G', '--.'),   ('H', '....'),  ('I', '..'),
                    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
                    ('M', '--'),    ('N', '-.'),    ('O', '---'),
                    ('P', '.--.'),  ('Q', '--.-'),  ('R', '.-.'),
                    ('S', '...'),   ('T', '-'),     ('U', '..-'),
                    ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
                    ('Y', '-.--'),  ('Z', '--..'),  ('0', '-----'),
                    ('1', '.----'), ('2', '..---'), ('3', '...--'),
                    ('4', '....-'), ('5', '.....'), ('6', '-....'),
                    ('7', '--...'), ('8', '---..'), ('9', '----.'),
                    (' ', ' '),     (',', '--..--'),('.', '.-.-.-'),
                    ('?', '..--..'),(';', '-.-.-.'),(':', '---...'),
                    ("'", '.----.'),('-', '-....-'),('/', '-..-.'),
                    ('_', '..--.-')
                    # ('(', '-.--.-'), # (')', '-.--.-')
                ]
            )
        )

    def _text_message_formater(self, message:str) -> list:
        message = message.upper()
        message = ''.join(
            char for char in message if char in self._morse_code.keys()
        )
        message = message.split(' ')
        return message

    def _is_morse_code_formated(self, message:str):
        if not isinstance(message, str):
            raise TypeError('Only string messages allowed')
        
        words = message.split('       ')
        if len(words) > 1:
            multiple_words = True
            single_letters = [word for word in words if word.find('   ') == -1]
            if (len(single_letters) / len(words)) < 0.5:
                return multiple_words
            
            else:
                raise MorseStringFormatingError(word=message)
        
        elif message.find('   ') != -1:
            multiple_words = False
            return multiple_words
        
        raise MorseStringFormatingError(word=message)

    def _encode(self, word:str) -> str:
        encoded_word = [
            self._morse_code.get(char, '?') for char in word
        ]
        return '   '.join(encoded_word)
    
    def _decode(self, word:str) -> str:
        decoded_word =[
            self._morse_code.inv.get(char, '?') for char in word.split('   ')
        ]
        return ''.join(decoded_word)
        
    def translate(self, message:str) -> list:
        is_morse = bool(re.match('^(\.|\s|-)+$', message))
        if is_morse:
            multiple_words = self._is_morse_code_formated(message)
            if multiple_words:
                words = message.split('       ')
                decoded_message = list(map(self._decode, words))
                return ' '.join(decoded_message)
            decoded_message = list(map(self._decode, message.split('   ')))
            return ' '.join(decoded_message)
        message = self._text_message_formater(message)
        return list(map(self._encode, message))


def main():
    translator = Morse()
    message='Whether tis nobler a the mind to suffer'
    # # message='SOS'
    translated_text_message = translator.translate(message=message)
    
    # morse_message = ['-   ---', '-...   .', '---   .-.', '-.   ---   -', '-   ---', '-...   .', '-   ....   .-   -', '..   ...', '-   ....   .', '--.-   ..-   .   ...   -   ..   ---   -.']
    # morse_message='--.-   ..-   .   ...   -   ..   ---   -.   ---...'
    # morse_message = '       '.join(morse_message)
    # morse_message = '-   ---       -...   .       -.   ---   -       -   ---       -...   .       -   ....   .   -       ..   ...       -   ....   .       --.-   ..-   ...   -   ..   ---   -   .   -.-.   ....   .-   ...   .       .   .-   .       -   ....   .       --.   .-   .   -   .-..   .   -   ..   ...       ---   ..-.       .-.   ..   .-.   ---   -.   -   ..-   .       ---   ..-   .-.         .-   --.   ..   ...       ..   ---   ..-.   .       .--   ....   .   -   -   ....   .   .-.   ...       -   ..   ...       -.   ---   -...   .   .-.   .-   .--.   ...       ---   ..-.   .-.   ---   .-.   -   ....   .-   -   ..'
    morse_message = '       '.join(translated_text_message)
    text = translator.translate(morse_message)
    '--   ....   .   -   ....   .   .-.       -   ..   ...       -.   ---   -...   .-..   .   .-.       .- '
    print(text, end='\n')
    print(translated_text_message)


if __name__=='__main__':
    main()