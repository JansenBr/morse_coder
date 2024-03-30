import numpy as np
import sounddevice as sd


from morse import Morse


class DitDash(Morse):
    def __init__(
            self,
            duration:float=0.2,
            frequency:int=440,
            sampling_rate:int=44100
        ) -> None:

        self.duration = duration
        self.frequency = frequency
        self.sampling_rate = sampling_rate
        
        self.dit = self.generate_sine_wave(
            duration=self.duration,
            frequency=self.frequency
        )
        self.dash = self.generate_sine_wave(
            duration=self.duration*3,
            frequency=self.frequency
        )
        self.silent = self.silence(duration=self.duration)

    def generate_sine_wave(
            self,
            duration:float,
            frequency:int,
            sampling_rate:int=44100
    ):
        t = np.linspace(
            0, duration, int(duration * sampling_rate), endpoint=False
        )
        note = np.sin(2 * np.pi * frequency * t)
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        return audio

    def silence(self, duration:float, sampling_rate:int=44100):
        samples = int(duration * sampling_rate)
        silent = np.zeros((samples,), dtype=np.float32)
        return silent

    def play_message(self, message:str):
        if self._is_morse(message) and self._white_space_check(message):
            # import ipdb; ipdb.set_trace()
            for char in message:
                if char == '.':
                    sd.play(self.dit, self.sampling_rate)
                    sd.wait()
                elif char == '-':
                    sd.play(self.dash, self.sampling_rate)
                    sd.wait()
                elif char == ' ':
                    sd.play(self.silent, self.sampling_rate)
                    sd.wait()


def main():
    play_morse = DitDash()
    message = Morse().translate('Hey lets go')
    play_morse.play_message(message)


if __name__ == '__main__':
    main()
