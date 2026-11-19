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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        queue<TreeNode*> roots;
        stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            TreeNode* top = st.top(); 
            st.pop();
            if (top->val == subRoot->val) roots.push(top);
            if (top->right) st.push(top->right);
            if (top->left) st.push(top->left);
        }
        while (!roots.empty()) {
            TreeNode* front = roots.front();
            roots.pop();
            bool isSub = true;
            stack<pair<TreeNode*, TreeNode*>> pr;
            pr.push({front, subRoot});
            while (!pr.empty()) {
                auto [r, s] = pr.top();
                pr.pop();
                if (!r ^ !s || r->val != s->val) {
                    isSub = false;
                    break;
                }
                if (r->left || s->left) pr.push({r->left, s->left}); 
                if (r->right || s->right) pr.push({r->right, s->right}); 
            }
            if (isSub) return true;
        }
        return false;
    }
};
