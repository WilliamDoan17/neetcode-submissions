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
        Node dummy(-1);
        Node* cur = head;
        while (cur) {
            Node* newNode = new Node(cur->val);
            newNode->next = cur->next;
            cur->next = newNode;
            cur = newNode->next;
        }

        cur = head;
        while (cur) {
            cur->next->random = cur->random ? cur->random->next : nullptr;
            cur = cur->next->next;
        }

        cur = head;
        Node *c_d = &dummy;
        while (cur) {
            c_d->next = cur->next;
            c_d = c_d->next;
            cur->next = c_d->next;
            cur = cur->next;
        } 
        return dummy.next;
    }
};
