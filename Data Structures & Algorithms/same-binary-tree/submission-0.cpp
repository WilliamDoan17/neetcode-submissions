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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<TreeNode*> sp, sq;
        sp.push(p);
        sq.push(q);

        while (!sp.empty() && !sq.empty()) {
            TreeNode* tp = sp.top();
            sp.pop();
            TreeNode* tq = sq.top();
            sq.pop();
            if (!tp && !tq) continue;
            if ((!tp ^ !tq) || tp->val != tq->val) return false;
            if (tp) {
                sp.push(tp->right);
                sp.push(tp->left);
            }
            if (tq) {
                sq.push(tq->right);
                sq.push(tq->left);
            }
        }

        return true;
    }
};
