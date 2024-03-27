import random
import unittest


from morse import Morse


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
            'not_morse_code': 'Hello there! Im not morse code'
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

    def test_is_morse_code_formated(self):
        correct_formating = self.morse_message.get('correct')
        
        morse = Morse()
        self.assertTrue(morse._is_morse_code_formated(correct_formating))
        
    def test_is_morse_code_formated_wrong_inter_words(self):
        wrong_inter_words = self.morse_message.get('wrong_inter_word')
        
        morse = Morse()
        self.assetFal