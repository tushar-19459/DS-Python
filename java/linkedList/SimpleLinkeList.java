public class SimpleLinkeList {
    Node head = null;
    Node tail = null;
    int count = 0 ;
    
    public SimpleLinkeList(){

    }

    class Node{
        int data ;
        Node next = null;
        public Node(int ele){
            data = ele;
        }
    }

    public boolean isEmpty(){
        return count==0;
    }

    public void insertAtHead(int ele){
        if (!isEmpty()){
            Node newnode = new Node(ele);
            newnode.next = head;
            head = newnode;
        }else{
            head = new Node(ele);
            tail = head;
        }
        count++;
    }

    public void getAll(){
        Node temp = head;
        while (temp!=null) {
            System.out.print(temp.data+" ");
            temp = temp.next;
        }
        System.out.println();
    }

    public void insertAtTail(int ele){
        if(!isEmpty()){
            Node newnode = new Node(ele);
            tail.next = newnode;
            tail = newnode; 
        }else{
            head = new Node(ele);
            tail = head;
        }
        count++;
    }

    public void deleteAtHead(){
        if(count!=1){
            Node temp = head;
            head = head.next;
            temp.next = null;
        }else{
            head = null;
            tail = null;
        }
        count--;
    }
    
    public void deleteAtTail(){
        if(count!=1){
            Node temp = head;
            while (temp.next!=tail) {
                temp = temp.next;
            }
            temp.next = null;
        }else{
            head = null;
            tail = null;
        }
        count--;
    }
}