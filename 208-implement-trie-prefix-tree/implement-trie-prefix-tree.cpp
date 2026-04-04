#include <unordered_map>
#include <string>
#include <iostream>
class Trie {
public:
    bool end; // end of word or not
    std::unordered_map<char, Trie*> map; // character of the word, next Trie node
    Trie() {
        end = false;
    }
    
    void insert(string word) {
        Trie* curr = this;
        for (int i = 0; i < word.length(); ++i) {
            if (!curr->map.count(word[i])) {
                curr->map.insert({word[i], new Trie()});
                //std::cout << "inserted letter " << word[i] << std::endl;
            }
            curr = curr->map[word[i]];
        }
        curr->end = true;
    }
    
    bool search(string word) {
        Trie* curr = this;
        for (int i = 0; i < word.length(); ++i) {
            if (!curr->map.count(word[i])) {
                return false;
            }
            curr = curr->map[word[i]];
        }
        return curr->end;
    }
    
    bool startsWith(string prefix) {
        Trie* curr = this;
        for (int i = 0; i < prefix.length(); ++i) {
            if (!curr->map.count(prefix[i])) {
                return false;
            }
            curr = curr->map[prefix[i]];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */