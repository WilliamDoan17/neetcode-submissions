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
    ListNode* reverse(ListNode *head, ListNode *end) {
        if (head->next == end) {
            return head;
        }
        ListNode *newHead = reverse(head->next, end);
        head->next->next = head;
        head->next = end;
        return newHead;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0, head);
        ListNode *cur = head, *tail = head, *prev = &dummy;
        while (tail) {
            for (int i = 0; i < k; i++) {
                if (!tail) {
                    return dummy.next;
                }
                tail = tail->next; 
            }
            prev->next = reverse(cur, tail);
            prev = cur;
            cur = tail;
        }
        return dummy.next;
    }
};
