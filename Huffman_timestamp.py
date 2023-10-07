import time
class Node:
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(symbols):
    queue = []
    for symbol, frequency in symbols:
        queue.append(Node(symbol, frequency))

    while len(queue) > 1:
        left = queue.pop(0)
        right = queue.pop(0)
        root = Node(None, left.frequency + right.frequency, left, right)
        queue.append(root)

    return queue[0]

def generate_huffman_codes(root):
    codes = {}
    def generate_code(node, code=""):
        if node is None:
            return

        if node.symbol is not None:
            codes[node.symbol] = code

        generate_code(node.left, code + "0")
        generate_code(node.right, code + "1")

    generate_code(root)
    return codes

def encode(text, codes):
    encoded_text = ""
    for character in text:
        encoded_text += codes[character]

    return encoded_text

def decode(encoded_text, codes):
    decoded_text = ""
    current_node = build_huffman_tree(codes.items())
    current_code = ""

    for bit in encoded_text:
        current_code += bit

        for symbol, code in codes.items():
            if code == current_code:
                decoded_text += symbol
                current_code = ""
                break

    return decoded_text

if __name__ == "__main__":

    text = "1000"
    start= time.time_ns()
    symbols = [(character, text.count(character)) for character in set(text)]
    root = build_huffman_tree(symbols)
    codes = generate_huffman_codes(root)

    encoded_text = encode(text, codes)
    decoded_text = decode(encoded_text, codes)

    print(text)
    print(encoded_text)
    print(decoded_text)
    end=time.time_ns()
    #print("The start time is: ", start)
    print("The running time is: ", end - start)
    print(end)