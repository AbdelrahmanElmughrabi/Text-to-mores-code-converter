# Morse Code Converter using Trie Data Structure

A Python implementation of a Morse code encoder and decoder using a Trie (prefix tree) data structure. This project efficiently converts text to Morse code and vice versa by utilizing a binary trie where dots (.) and dashes (-) form the paths to letters.

## About the Implementation

The converter uses a binary trie (prefix tree) where:
- Each node can have up to 2 children (left and right)
- Left branches represent dots (.)
- Right branches represent dashes (-)
- Leaf nodes contain letters of the alphabet
- Efficient lookup through tree traversal

## Features

- Convert English text to Morse code
- Decode Morse code back to English text
- Supports all 26 English alphabet letters (A-Z)
- Uses efficient Trie data structure for encoding/decoding
- Word separation using forward slash (/)

## Usage Example

```python
# Create a new Morse code trie
tree = MorseCodeTree()

# Encode text to Morse code
text = "HELLO WORLD"
morse = tree.encode_text(text)
print(f"Original text: {text}")
print(f"Morse code: {morse}")

# Decode Morse code back to text
decoded = tree.decode_morse(morse)
print(f"Decoded text: {decoded}")
```

## Morse Code Representation

- Dots (.) represent short signals
- Dashes (-) represent long signals
- Forward slash (/) represents word separators
- Space ( ) separates individual letters

## Time Complexity

- Encoding: O(n) where n is the length of input text
- Decoding: O(m) where m is the length of Morse code string
- Tree construction: O(k) where k is the number of characters in the alphabet.