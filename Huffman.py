from heapq import heappush, heappop, heapify

# Creating tree nodes
class NodeTree(object):
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


# Main function implementing Huffman coding
def huffman_code_tree(frequencies):
    heap = [NodeTree(char, freq) for char, freq in frequencies]
    heapify(heap)

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        parent = NodeTree(freq=left.freq + right.freq, left=left, right=right)
        heappush(heap, parent)

    return heap[0]


# Traversing the Huffman tree to get codes
def traverse_tree(node, code='', huffman_codes={}):
    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = code
        traverse_tree(node.left, code + '0', huffman_codes)
        traverse_tree(node.right, code + '1', huffman_codes)
    return huffman_codes


def main():
    string = 'BCAADDDCCACACAC'
    
    # Calculating frequency
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1

    frequencies = [(char, freq) for char, freq in freq.items()]
    frequencies.sort(key=lambda x: x[1])

    huffman_tree = huffman_code_tree(frequencies)
    huffman_codes = traverse_tree(huffman_tree)

    print(' Char | Huffman code ')
    print('----------------------')
    for char, frequency in frequencies:
        print(f' {char:<5}| {huffman_codes[char]}')

if __name__ == "__main__":
    main()
