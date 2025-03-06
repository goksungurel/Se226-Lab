#include <iostream>
using namespace std;

class Queue {
private:

    class Node {
    public:
        int data;
        Node* next;

        Node(int val) {
            data = val;
            next = nullptr;
        }
    };

    Node* head;
    Node* tail;
    int count; 

public:

    Queue() {
       head = nullptr;
        tail = nullptr;
        count = 0;
    }
   
    void enqueue(int val) {
        Node* newNode = new Node(val);
        if (tail == nullptr) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return;
        }
        Node* temp = head;
        head= head->next;
        delete temp;
        count--;
        if (head == nullptr) {
            tail = nullptr;
        }
    }
    
    int top() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1; 
        }
        return head->data;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    
    int size() {
        return count;
    }
};

int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Front element: " << q.top() << endl;  
    cout << "Queue size: " << q.size() << endl;   

    q.dequeue(); 
    cout << "Front element after dequeue: " << q.top() << endl;  /

    q.dequeue();
    q.dequeue();
    cout << "Is queue empty? " << (q.isEmpty() ? "Yes" : "No") << endl; 
    return 0;
}


    
  
