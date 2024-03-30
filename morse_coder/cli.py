import argparse


from morse import Morse
from sound import DitDash


def main():
    parser = argparse.ArgumentParser(
        prog='morse_coder',
        description='Simple CLI to encode text-to-morse and decode morse-to-text',
        epilog='BYE | -... -.-- .'
    )
    parser.add_argument(
        'action', choices=['translate'],
        help='Translates the input text-to-morse or morse-to-text'
    )
    parser.add_argument(
        '--play', action='store_true',
        help='Play the message in Morse code'
    )
    parser.add_argument(
        'text', nargs='+',
        help='String text to be translated'
    )
    args = parser.parse_args()

    morse = Morse()
    out = morse.translate(args.text[0])
    print(out)

    if morse._is_morse(out) and args.play:
        sound = DitDash()
        sound.play_message(out)


if __name__=='__main__':
    main()
    