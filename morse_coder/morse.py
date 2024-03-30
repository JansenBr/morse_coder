import re
import bidict


from collections import OrderedDict


from errors import MorseStringFormatingError


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

    def _is_morse(self, message:str):
        if not isinstance(message, str):
            raise TypeError(f'Only string messages allowed not {type(message)}')
        return bool(re.match(r'^(\.|\s|-)+$', message))

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

    def _white_space_check(self, message:str) -> bool:
        white_space_count = self._count_whitespaces(message)
        if any(x != 0 for x in white_space_count.values()):
            raise MorseStringFormatingError(
                string=message, white_spaces=white_space_count
            )
        return True
    
    def _single_word(self, message:str) -> bool:
            words = message.split('       ')
            if len(words) > 1:
                return False       
            elif message.find('   ') != -1:
                return True
            elif len(words)==1:
                return True
            else:
                raise MorseStringFormatingError(
                    string=message
                )

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
        if self._is_morse(message) and self._white_space_check(message):
            if self._single_word(message):
                decoded_message = list(map(self._decode, message.split('   ')))
                return ''.join(decoded_message)
            else:
                decoded_message = list(map(
                    self._decode, message.split('       ')
                    )
                )
                return ' '.join(decoded_message)
        message = self._text_message_formater(message)
        morse = list(map(self._encode, message))
        return '       '.join(morse)


