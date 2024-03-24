import bidict


class Translator(object):
    def __init__(self) -> None:
        self._morse_code = bidict.bidict(
            {
                'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',  '1': '.----',
                '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.', '0': '-----',
                ' ': '/'
            }
        )

    def _message_formater(self, message:str):
        message = message.upper()
        formated_message = ''.join(
            char for char in message if char in self._morse_code.keys()
        )
        import ipdb; ipdb.set_trace()
        return formated_message

    def to_morse_code(self, message:str):
        message = self._message_formater(message)
        morse_message = [
            self._morse_code.get(char) for char in message
        ]
        return ''.join(morse_message)
    
    def to_text(self, morse_message:str):
        text_message = [
            self._morse_code.inv.get(morse_char) for morse_char in morse_message
        ]
        return ''.join(text_message)
    
def main():
    translator = Translator()
    message='''    
        To be, or not to be, that is the question:
        Whether ’tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune,
        Or to take arms against a sea of troubles
        And by opposing end them. To die—to sleep,
    '''
    morse_message = '.--.....-......-.'
    import ipdb; ipdb.set_trace()
    translated_morse_message = translator.to_morse_code(
        message=message
    )
    translated_text_message = translator.to_text(morse_message=morse_message)
    
    print(translated_morse_message, end='\n')
    print(translated_text_message)


if __name__=='__main__':
    main()