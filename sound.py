# import numpy as np
# import simpleaudio as sa

# frequency = 555  # Our played note will be 440 Hz
# fs = 44100  # 44100 samples per second
# seconds = 1  # Note duration of 3 seconds

# # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# t = np.linspace(0, seconds, seconds * fs, False)

# # Generate a 440 Hz sine wave
# note = np.sin(frequency * t * 2 * np.pi)

# # Ensure that highest value is in 16-bit range
# audio = note * (2**15 - 1) / np.max(np.abs(note))
# # Convert to 16-bit data
# audio = audio.astype(np.int16)

# # Start playback
# play_obj = sa.play_buffer(audio, 1, 2, fs)

# # Wait for playback to finish before exiting
# play_obj.wait_done()

# # class DitDash(object):
# #     def __init__(self) -> None:
# #         pass

# #     def generate_freq.

import simpleaudio as sa
import numpy as np
import time

# Define Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

# Function to generate sine wave
def generate_sine_wave(duration, frequency, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave

# Function to play Morse code
def play_morse_code(text, unit_time=1, sampling_rate=44100):
    wave_dict = {}
    for char in text:
        if char.upper() in morse_code:
            code = morse_code[char.upper()]
            for symbol in code:
                if symbol == '.':
                    if 'dot' not in wave_dict:
                        wave_dict['dot'] = generate_sine_wave(unit_time, 440, sampling_rate)
                    sa.play_buffer((wave_dict['dot'] * 32767).astype(np.int16), 1, 2, sampling_rate)
                elif symbol == '-':
                    if 'dash' not in wave_dict:
                        wave_dict['dash'] = generate_sine_wave(unit_time * 3, 440, sampling_rate)
                    sa.play_buffer((wave_dict['dash'] * 32767).astype(np.int16), 1, 2, sampling_rate)
                time.sleep(unit_time)  # Length of beep
            time.sleep(unit_time)  # Gap between characters
        else:
            time.sleep(unit_time * 3)  # Gap between words

# Example usage
text_to_encode = "SOS"
play_morse_code(text_to_encode)
