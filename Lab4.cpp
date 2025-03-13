#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     
    int num;         
    int capacity;   

public:
    Stack(int initialCapacity) {  
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

  
    void push(int x) {
        if (num == capacity - 1) {
            increaseCapacity();  
        }
        
        Node* newNode = new Node();  
        newNode->data = x;           
        newNode->next = head;        
        head = newNode;            
        num++;                       
    }

    
    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;  
        }
        
        int topValue = head->data;  
        Node* temp = head;          
        head = head->next;          
        delete temp;                
        num--;                      
        return topValue;            
    }

   
    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }

    
    bool isEmpty() {
        return num < 0;
    }

    
    void increaseCapacity() {
        capacity *= 2;  
        cout << "Capacity increased to " << capacity << endl;
    }

 
    bool deleteElement(int val) {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }
        
        Node* current = head;
        Node* prev = nullptr;
        
        
        if (current != nullptr && current->data == val) {
            head = current->next; 
            delete current;       
            num--;
            return true;
        }
        
        
        while (current != nullptr && current->data != val) {
            prev = current;
            current = current->next;
        }
        
        
        if (current == nullptr) {
            return false;
        }
        
        
        prev->next = current->next;
        delete current; 
        num--;
        return true;
    }
};

int main() {
    Stack s(5);  
    
    s.push(10);  
    s.push(20);  
    s.push(30);  
    
    cout << "Top element: " << s.peek() << endl;  
    
    cout << "Popped element: " << s.pop() << endl;  
    
    s.push(40);  
    
    s.deleteElement(20); 
    
    cout << "Top element after deletion: " << s.peek() << endl;
    
    return 0;
}
