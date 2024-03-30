# `morse_coder` is a CLI  to encode text-to-morse and decode morse-to-text 
## It has built in morse code audio generation for CW trainning

There are hunderts of solutions that do the same available in different languages, check them out to see the one that suits your needs the most, here are just a few:
- [ggmorse](https://github.com/ggerganov/ggmorse) (C++)
- [morse-talk](https://github.com/morse-talk/morse-talk) (python)
- [morse](https://github.com/alwindoss/morse) (goLang)
#

## Install

Since it uses `sounddevice` it will require  `libportaudio2`

```
sudo apt install libportaudio2 
```

 ## Usage

**Encoding Text to Morse Code:**

To translate a text message into Morse code, use the following command:

```
morse_coder translate <text_message>
```

* Replace `<text_message>` with the text you want to encode.

**Decoding Morse Code to Text:**

To decode a Morse code message back into text, use the same command structure:

```
morse_coder translate <morse_message>
```

* Replace `<morse_message>` with the Morse code sequence you want to decode.

**Important Note:**

* Morse code messages must be formatted with **three spaces between letters** and **seven spaces between words**.

**Playing Morse Code Sound:**

To play the Morse code sound of a text message, use the `--play` flag:

```
morse_coder translate --play <text_message>
```

**Important Note:**

* The `--play` flag **only works with text messages** as input. It cannot play decoded Morse code output.

**Examples:**

* Encode "Hello world" to Morse code:

```
morse_coder translate "Hello world"
```

* Decode "....   .   .-..   .-..   ---" to text:

```
morse_coder translate ".... . .-.. .-.. ---"
```

* Encode "SOS" and play the Morse code sound:

```
morse_coder translate --play "SOS"
```



# Contributing
We welcome contributions from the community to enhance the functionality and usability of this repository. Feel free to submit issues, feature requests, or pull requests to help improve this repo!

