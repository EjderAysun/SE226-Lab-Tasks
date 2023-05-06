#include <iostream>
using namespace std;

struct QNode {
    int data;
    struct QNode* next;
    QNode(int d) {
        data = d;
        next = NULL;
    }
};

struct Queue {
    QNode *front, *rear;
    Queue() { front = rear = NULL; }

    void enQueue(int x) {
        // Create a new LL node.
        QNode* temp = new QNode(x);

        // If queue is empty, then new node is front and rear both.
        if( rear == NULL ) {
            front = rear = temp;
            return;
        }

        // Add the new node at the end of queue and change rear.
        rear->next = temp;
        rear = temp;
    }

    // Function to remove a key from given qeueue q.
    void deQueue() {
        // If queue is empty, return NULL.
        if(front == NULL) return;

        // Store previous front and move front one node ahead.
        QNode* temp = front;
        front = front->next;

        // If front becomes NULL, then change rear also as NULL.
        if(front == NULL) rear = NULL;

        delete(temp);
    }

    int top() {
        // If the queue is empty throw out of range exception.
        if(isEmpty()) throw out_of_range("The queue is empty.");
        // If the queue is not empty, return the data of the front.
        return front->data;
    }

    bool isEmpty() {
        // If the queue is empty return true, if not return false.
        if(front == NULL && rear == NULL) return true;
        else return false;
    }

    int size() {
        int size = 0;
        QNode* temp = front;
        while (temp != NULL) {  // If queue is empty, size is 0.
            // If the queue is not empty, 1 is added to \
            the size variable for each data until the temp is NULL.
            size ++;  
            temp = temp->next;
        }
        return size;
    }

    // LAB 3.5 CPP start//
    void reverse() {
        if (front == NULL) return; // do not process for empty queue
        QNode* current = front;
        QNode* prev = NULL;
        QNode* next = NULL;
        rear = front; // The rear node becomes a front node.
        while (current != NULL) {
            // Save next node.
            next = current->next;
            // Set the next value of the current node as the previous node.
            current->next = prev;
            // Move previous and current nodes to the next step.
            prev = current;
            current = next;
        }
        front = prev; // Let the front node point to the last node.
    }
    // LAB 3.5 CPP end //
    
    // *******************************
    // non-task but helper methods: //
    
    void Display() {
        QNode* temp = front;
        if ((front == NULL) && (rear == NULL)) {
            cout<<"Queue is empty"<<endl;
            return;
        }
        cout<<"Queue elements are: ";
        while (temp != NULL) {
            cout<<temp->data<<" ";
            temp = temp->next;
        }
        cout<<endl;
    }

    void check(Queue q) {
        cout<<"is empty: "<<boolalpha<<q.isEmpty()<<endl;
        cout<<"size: "<<q.size()<<endl;
        cout<<"top element: "<<q.top()<<endl;
        cout<<"*****"<<endl;
    }
};

// Test area //
int main() {
    cout<<"*****"<<endl;
    Queue q;
    q.Display();
    cout<<"is empty: "<<boolalpha<<q.isEmpty()<<endl;
    cout<<"size: "<<q.size()<<endl;
    cout<<"*****"<<endl;
    
    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.deQueue();
    q.deQueue();
    q.Display();
    q.check(q);

    q.deQueue();
    q.deQueue();
    q.enQueue(18);
    q.enQueue(35);
    q.enQueue(5);
    q.Display();
    q.check(q);

    q.reverse();
    q.Display();
    q.check(q);

    return 0;
}