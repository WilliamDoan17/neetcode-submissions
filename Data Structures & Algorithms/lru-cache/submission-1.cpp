struct Node {
    int val, key;
    Node *next, *prev;
    Node(int value, int key) : val(value), key(key) {}
};

class LRUCache {
    int cap;
    Node* head;
    Node* tail;
    int size;
    unordered_map<int, Node*> mp;

public:
    void unlink(Node* it) {
        Node *p = it->prev, *n = it->next;
        p->next = n;
        if (n) n->prev = p;
        else tail = p;
    }
    void push(Node* it) {
        it->next = nullptr;
        it->prev = tail;
        tail->next = it;
        tail = it;
    }
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(-1, -1);
        tail = head;
    }
    
    int get(int key) {
        if (mp.find(key) == mp.end()) return -1;
        Node *it = mp[key];
        unlink(it);
        push(it);
        return it->val;
    }
    
    void put(int key, int value) {
        auto f = mp.find(key);
        if (f != mp.end()) {
            Node* it = f->second;
            it->val = value;
            unlink(it);
            push(it);
            return;
        }
        if ((int)mp.size() == cap) {
            Node* t = head->next;
            mp.erase(t->key);
            unlink(t);
            delete t;
        }
        Node* it = new Node(value, key);
        push(it);
        mp[key] = it;
    }
};
