#include <string>
#include <queue>
#include <iostream>
#include <sstream>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:


    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        std::queue<TreeNode*> q;
        std::string o;
        q.push(root);
        o += std::to_string(root->val);
        o += ',';
        std::cout << o << std::endl;
        while (q.size() > 0) {
            if (q.front()->left) {
                q.push(q.front()->left);
                o += std::to_string(q.front()->left->val);
                o += ',';
            } else {
                o += ('N');
                o += ',';
            }
           
            if (q.front()->right) {
                q.push(q.front()->right);
                o += std::to_string(q.front()->right->val);
                o += ',';
            } else {
                o += ('N');
                o += ',';
            }
            q.pop();
        }
        std::cout << o << std::endl;
        return o;
    }


    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.length() == 0) return nullptr;
        std::stringstream ss(data);
        std::queue<TreeNode*> q;
        std::string val;
        std::getline(ss, val, ',');
        TreeNode* root = new TreeNode(stoi(val));
        q.push(root);
        while (!q.empty()) {
            std::getline(ss, val, ','); // left, 2
            if (val != "N") {
                std::cout << val << std::endl;
                TreeNode* node = new TreeNode(stoi(val));
                q.front()->left = node;
                q.push(node);
            }
            std::getline(ss, val, ','); // right, 3
            if (val != "N") {
                std::cout << val << std::endl;
                TreeNode* node = new TreeNode(stoi(val));
                q.front()->right = node;
                q.push(node);
            }
            q.pop();
        }
        return root;
    }
};


// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
