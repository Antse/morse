# morse.py
# pylint: disable=missing-docstring

class Morse:
    def decode(self, message):
        pass # TODO: implement the behavior!


class Morse:
    ALPHABET = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    def decode(self, message):
        if message == "":
            return ""

        symbols = message.split(" ")
        letters = [self.ALPHABET[s] for s in symbols]
        return ''.join(letters)
