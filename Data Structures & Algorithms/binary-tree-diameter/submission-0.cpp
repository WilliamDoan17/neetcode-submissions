/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        unordered_map<TreeNode*, vector<TreeNode*>> adj;
        stack<TreeNode*> st;
        st.push(root);
        vector<TreeNode*> nodes;
        while (!st.empty()) {
            TreeNode *top = st.top();
            nodes.push_back(top);
            st.pop();
            if (top->left) {
                adj[top].push_back(top->left);
                adj[top->left].push_back(top);
                st.push(top->left);
            }
            if (top->right) {
                adj[top].push_back(top->right);
                adj[top->right].push_back(top);
                st.push(top->right);
            }
        }
        int res = 0; 
        TreeNode dummy = TreeNode(-1);
        for (TreeNode *n : nodes) {
            stack<tuple<TreeNode*, TreeNode*, int>> st1;
            st1.push({&dummy, n, 0});
            while (!st1.empty()) {
                auto [parent, node, level] = st1.top();
                st1.pop();
                res = max(res, level);
                for (auto a : adj[node]) {
                    if (a != parent) {
                        st1.push({node, a, level + 1});
                    }
                }  
            }
        }        
        return res;
    }
};
