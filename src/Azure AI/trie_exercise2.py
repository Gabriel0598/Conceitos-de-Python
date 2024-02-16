class TrieNode:

    # Constructor method
    def __init__(self):
        # dicionary mapping each element
        self.nodes = {}
        self.end_of_word = False
        self.freq = 0

    # Append char
    def add_char(c: chr) -> TrieNode:
        if c not in self.nodes:
            self.nodes[c] = TrieNode()
        return self.nodes[c]

