import random
import unittest


from morse import Morse
from errors import MorseStringFormatingError

class TranslatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.messages = [
        'To be, or not to be, that is the question:',
        'Whether tis nobler in the mind to suffer',
        'The slings and arrows of outrageous fortune,',
        'Or to take arms against a sea of troubles',
        'And by opposing end them. To die to sleep,',
        'No more; and by a sleep to say we end',
        'The heart ache and the thousand natural shocks',
        'That flesh is heir to: tis a consummation',
        'Devoutly to be wishd. To die, to sleep;',
        'To sleep, perchance to dream ay, theres the rub:',
        'For in that sleep of death what dreams may come,',
        'When we have shuffled off this mortal coil,',
        'Must give us pause theres the respect',
        ]
        
        self.not_allowed_chars = ['!', '@', '#', '$', '%', '&', '*']
        
        self.morse_message = {
            'correct':'.--   ....   .   -   ....   .   .-.       -   ..   ...       -.   ---   -...   .-..   .   .-.       -   ---       -   ....   .       --   ..   -.   -..       -   ---       ...   ..-   ..-.   ..-.   .   .-.',
            'wrong_inter_word':'.--   ....   .   -   ....   .   .-.     -   ..   ...     -.   ---   -...   .-..   .   .-.     -   ---     -   ....   .     --   ..   -.   -..     -   ---     ...   ..-   ..-.   ..-.   .   .-.',
            'wrong_inter_letter':'.--  ....    .    -  ....  .  .-.       -  ..  ...       -.',
            'not_morse_code': 'Hello there! Im not morse code',
            'single_word':'.--   ....   .   -   ....   .   .-.'
        }
        return super().setUp()
    
    def test_text_message_formater(self):
        message = random.choice(self.messages)
        tempered_message = ''.join('%s%s' % (x, random.choice(
                    self.not_allowed_chars
        ) if random.random() > 0.5 else '') for x in message)
        
        morse = Morse()
        formated_message = morse._text_message_formater(message=tempered_message)
        formated_message = ' '.join(formated_message)
        self.assertEqual(formated_message, message.upper())

    def test_white_space_check_ok(self):
        correct_formating = self.morse_message.get('correct')
        morse = Morse()
        self.assertTrue(morse._white_space_check(correct_formating))
        
    def test_white_space_check_raises_exception(self):
        morse = Morse()
        with self.assertRaises(MorseStringFormatingError):
            morse._white_space_check(self.morse_message.get('wrong_inter_word'))
        
        with self.assertRaises(MorseStringFormatingError):
            morse._white_space_check(self.morse_message.get('wrong_inter_letter'))

    def test_is_morse(self):
        morse = Morse()
        self.assertFalse(
            morse._is_morse(self.morse_message.get('not_morse_code'))
        )
        self.assertTrue(
            morse._is_morse(self.morse_message.get('correct'))
        )

    def test_single_word(self):
        morse = Morse()
        self.assertTrue(
            morse._single_word(self.morse_message.get('single_word'))
        )
        self.assertFalse(
                    morse._single_word(self.morse_message.get('correct'))
        )

    def test_encode(self):
        morse = Morse()
        text = morse._encode('WHETHER')
        self.assertEqual(text, self.morse_message.get('single_word'))

    def test_decode(self):
        morse = Morse()
        morse_text = morse._decode(self.morse_message.get('single_word'))
        self.assertEqual(morse_text, 'WHETHER')

    def test_translate_text(self):
        morse = Morse()
        morse_code = morse.translate(self.messages[3])
        text = morse.translate(morse_code)
        self.assertEqual(self.messages[3].upper(), text)

