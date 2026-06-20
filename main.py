from trie import Trie

def main():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("Heaven")
    trie.insert("heavy")

    print(trie.search("hello")) 
    print(trie.search("hell"))   

    print(trie.starts_with("he"))

    words = trie.dfs_search("he")
    for word in words:
        print(word)

    trie.delete("hell")
    print(trie.search("hell"))

    words = trie.dfs_search("he")
    for word in words:
        print(word)

if __name__ == "__main__":
    main()