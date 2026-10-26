/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> copy;
        for (Node *p = head; p; p = p->next)
            copy[p] = new Node(p->val);
    
        for (Node *p = head; p; p = p->next) {
            copy[p]->next   = p->next   ? copy[p->next]   : nullptr;
            copy[p]->random = p->random ? copy[p->random] : nullptr;
        }
        return head ? copy[head] : nullptr;
    }
};
