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
unordered_map<TreeNode*, int> height;
private:
    void computeHeight(TreeNode *root) {
        if (!root) {
            return;
        }
        if (root->left && height.find(root->left) == height.end()) computeHeight(root->left);
        if (root->right && height.find(root->right) == height.end()) computeHeight(root->right);
        int l = root->left ? height[root->left] : 0;
        int r = root->right ? height[root->right] : 0;
        height[root] = 1 + max(l, r);
    }
public:
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        computeHeight(root);
        stack<TreeNode*> st;
        st.push(root);

        while (!st.empty()) {
            TreeNode* top = st.top();
            st.pop();
            int l = top->right ? height[top->right] : 0;
            int r = top->left ? height[top->left] : 0;
            if (abs(l - r) > 1) return false;
            if (top->right) st.push(top->right);
            if (top->left) st.push(top->left);
        }

        return true;
    }
};
