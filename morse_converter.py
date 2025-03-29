
class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.left = None  # dot (.)
        self.right = None  # dash (-)

class MorseCodeTree:
    def __init__(self):
        self.root = TrieNode()
        self.morse_code = {
            'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..'
        }
        self.build_tree()
# insert each character into the tree
    def insert(self, char, code):
        node = self.root
        for symbol in code:
            if symbol == '.':
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:  # symbol == '-'
                if not node.right:
                    node.right = TrieNode()
                node = node.right
        node.char = char

# build the Morse code tree
    # This method builds the tree from the morse_code dictionary
    def build_tree(self):
        for char, code in self.morse_code.items():
            self.insert(char, code)

# Convert text to Morse code
    def encode_text(self, text):
        result = []
        for char in text.upper():
            if char == ' ':
                result.append('/')  # Word separator
            elif char in self.morse_code:
                result.append(self.morse_code[char])
        return ' '.join(result)

#Converts mores to text
    def decode_morse(self, morse_code):      
        words = morse_code.split('/')
        result = []
        
        for word in words:
            letters = word.strip().split()
            decoded_word = ''
            for letter in letters:
                for char, code in self.morse_code.items():
                    if code == letter:
                        decoded_word += char
                        break
            result.append(decoded_word)
            
        return ' '.join(result)

if __name__ == "__main__":
    tree = MorseCodeTree()
    
    # Example usage
    text = "HELLO WORLD"
    morse = tree.encode_text(text)
    print(f"Original text: {text}")
    print(f"Morse code: {morse}")
    decoded = tree.decode_morse(morse)
    print(f"Decoded text: {decoded}")