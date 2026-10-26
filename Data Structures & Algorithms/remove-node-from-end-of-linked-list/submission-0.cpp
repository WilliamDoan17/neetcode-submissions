/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode *newHead = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return newHead;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *cur = new ListNode(-1);
        cur->next = reverseList(head);
        ListNode *dummy = cur;
        for (int i = 0; i < n - 1; i++) {
            cur = cur->next;
        }
        ListNode *tmp = cur->next;
        cur->next = tmp->next;
        tmp = nullptr;
        return reverseList(dummy->next); 
    }
}; 