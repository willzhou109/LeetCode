#include <unordered_map>
class WordDictionary {
public:
    std::unordered_map<char, WordDictionary*> map;
    bool end;
    WordDictionary() {
        end = false;
    }
    
    void addWord(string word) {
        WordDictionary* curr = this;
        for (int i = 0; i < word.length(); ++i) {
            if (!curr->map.count(word[i])) {
                curr->map[word[i]] = new WordDictionary();
            }
            curr = curr->map[word[i]];
        }
        curr->end = true;
    }
    
    bool search(string word) {
        return searchHelper(word, this);
    }

    bool searchHelper(string word, WordDictionary* curr) {
        if (curr->end && word.length() == 0) {
            return true;
        }
        if (!curr->map.count(word[0]) && word[0] != '.') { // if first letter of word is not found in the map
            return false;
        } else if (word[0] == '.') { // if first letter is .
            // loop through all wd's in current map
            for (const auto& [_, wd] : curr->map) {
                if (searchHelper(word.substr(1), wd)) {
                    return true;
                }
            }
            return false;
        } else { // if first letter of word is found in map
            if (searchHelper(word.substr(1), curr->map[word[0]])) {
                return true;
            } else {
                return false;
            }
        }
    } 
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */