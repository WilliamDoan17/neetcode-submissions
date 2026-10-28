struct Node {
    int key, val;
    Node *prev = nullptr, *next = nullptr;
    Node(int k, int v) : key(k), val(v) {}
};

class LRUCache {
    int cap;
    unordered_map<int, Node*> mp;
    Node *head, *tail;               // sentinels; LRU is head->next, MRU is tail->prev

    void unlink(Node* n) {
        n->prev->next = n->next;
        n->next->prev = n->prev;
    }
    void pushBack(Node* n) {         // insert just before tail sentinel
        n->prev = tail->prev;
        n->next = tail;
        tail->prev->next = n;
        tail->prev = n;
    }

public:
    LRUCache(int capacity) : cap(capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }
    ~LRUCache() {
        for (Node* n = head; n; ) { Node* nx = n->next; delete n; n = nx; }
    }

    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) return -1;
        Node* n = it->second;
        unlink(n);
        pushBack(n);
        return n->val;
    }

    void put(int key, int value) {
        auto it = mp.find(key);
        if (it != mp.end()) {
            Node* n = it->second;
            n->val = value;
            unlink(n);
            pushBack(n);
            return;
        }
        if ((int)mp.size() == cap) {
            Node* lru = head->next;
            unlink(lru);
            mp.erase(lru->key);
            delete lru;
        }
        Node* n = new Node(key, value);
        mp[key] = n;
        pushBack(n);
    }
};