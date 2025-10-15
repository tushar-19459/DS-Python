public class test {
    public static void main(String[] args) {
        SimpleLinkeList list = new SimpleLinkeList();
        list.insertAtHead(10);
        list.insertAtHead(20);
        list.insertAtHead(30);
        list.insertAtHead(40);
        list.insertAtHead(50);
        list.getAll();
        list.insertAtTail(10);
        list.insertAtTail(20);
        list.insertAtTail(30);
        list.insertAtTail(40);
        list.insertAtTail(50);
        list.getAll();
        list.deleteAtHead();
        list.getAll();
        list.deleteAtTail();
        list.getAll();
    }
}