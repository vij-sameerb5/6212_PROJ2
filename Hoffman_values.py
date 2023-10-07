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
    """Builds a Huffman tree from a list of symbols and their frequencies.

    Args:
        symbols: A list of tuples, where each tuple contains a symbol and its frequency.

    Returns:
        The root node of the Huffman tree.
    """

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
    """Generates Huffman codes for the symbols in a Huffman tree.

    Args:
        root: The root node of the Huffman tree.

    Returns:
        A dictionary mapping symbols to their Huffman codes.
    """

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
    """Encodes a text string using Huffman coding.

    Args:
        text: The text string to encode.
        codes: A dictionary mapping symbols to their Huffman codes.

    Returns:
        The encoded text string.
    """

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

def get_algo(arr):





    

    print(arr)
    symbols = [(character, arr.count(character)) for character in set(arr)]
    root = build_huffman_tree(symbols)
    codes = generate_huffman_codes(root)

    encoded_text = encode(arr, codes)

    


if __name__ == "__main__":
    array = ['1000','2000','3000','4000','5000','6000','7000','8000']
    for arr in array:
        start=time.time_ns()
        get_algo(arr)
        end=time.time_ns()
        timeelapse =end - start
        print('n=' +str(arr)+', start :'+str(start)+',end :'+str(end))
    

