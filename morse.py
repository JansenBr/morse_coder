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

# todo make it a CLI and add sound to encoded messages.
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

    def _count_whitespaces(self, text: str) -> dict:
        counts = {i: 0 for i in [1,2,4,5,6,8]}
        i = 0
        while i < len(text):
            if text[i].isspace():
                count = 0
                while i < len(text) and text[i].isspace():
                    count += 1
                    i += 1
                if count in counts:
                    counts[count] += 1
            else:
                    i += 1
        return counts

    def _check_morse_string_format(self, message:str):
        if not isinstance(message, str):
            raise TypeError(f'Only string messages allowed not {type(message)}')
        white_space_count = self._count_whitespaces(message)
        if any(x != 0 for x in white_space_count.values()):
            raise MorseStringFormatingError(word=message)
        words = message.split('       ')
        if len(words) > 1:
            return True       
        elif message.find('   ') != -1:
            return False
        else:
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
        is_morse = bool(re.match(r'^(\.|\s|-)+$', message))
        if is_morse:
            multiple_words = self._check_morse_string_format(message)
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
    message='.--  ....    .    -  ....  .  .-.       -  ..  ...       -.'
    translated_text_message = translator.translate(message=message)
    print('     '.join(translated_text_message))


if __name__=='__main__':
    main()