# 6212_PROJ2
Shaik Sameer
GWID: 9 Huffman Coding 

Here's an overview of the Huffman coding process:
1.	Frequency Analysis:
•	Calculate the frequency of each symbol (character) in the input data.
2.	Priority Queue (Min-Heap):
•	Create a priority queue (min-heap) based on the frequencies of the symbols.
3.	Huffman Tree Construction:
•	Build a binary tree by repeatedly combining the two nodes with the lowest frequencies until a single node (the root) is left. Each internal node has a weight equal to the sum of its children's weights.
4.	Code Assignment:
•	Traverse the Huffman tree to assign binary codes to each symbol. Assign '0' for a left branch and '1' for a right branch.
5.	Generate Huffman Codes:
•	The binary codes for each symbol are the paths from the root to the respective leaves.
6.	Encode (Compression):
•	Replace each symbol in the original data with its corresponding Huffman code.
7.	Decode (Decompression):
•	Use the Huffman tree to decode the compressed data back to the original symbols.
The efficiency of Huffman coding lies in its ability to create a compact representation for more frequent symbols, resulting in a variable-length code. This is in contrast to fixed-length codes, where each symbol is represented by the same number of bits.
