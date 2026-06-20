from trie_node import TrieNode
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        word = word.lower()
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def dfs_search(self, prefix):
        if not self.starts_with(prefix):
            return []
        node = self.root
        for char in prefix:
            node = node.children[char]
        return self.dfs(node, prefix)
    
    def dfs(self, node, prefix):
        words = []
        if node.end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self.dfs(child, prefix + char ))
        return words
    
    def delete(self, word):
        node = self.root
        stack = []
        for char in word:
            if char not in node.children:
                return False
            stack.append((node, char))
            node = node.children[char]
        if not node.end_of_word:
            return False
        node.end_of_word = False
        for parent, char in reversed(stack):
            child = parent.children[char]
            if not child.children and not child.end_of_word:
                del parent.children[char]
            else: 
                break



    




    
            
    

