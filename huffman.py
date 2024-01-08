from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(root):
    def traverse(node, current_code):
        if node:
            if node.char:
                codes[node.char] = current_code
            traverse(node.left, current_code + '0')
            traverse(node.right, current_code + '1')

    codes = {}
    traverse(root, '')
    return codes

def encode(text, codes):
    encoded_text = ''
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode(encoded_text, root):
    decoded_text = ''
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# Example text
text = "hello"

# Build Huffman tree and generate codes
huffman_tree = build_huffman_tree(text)
huffman_codes = generate_huffman_codes(huffman_tree)

# Encode the text using Huffman codes
encoded_text = encode(text, huffman_codes)
print("Encoded text:", encoded_text)

# Decode the encoded text using the Huffman tree
decoded_text = decode(encoded_text, huffman_tree)
print("Decoded text:", decoded_text)
