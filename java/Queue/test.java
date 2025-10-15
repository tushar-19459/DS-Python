import java.util.Arrays;

public class test {
    public static void main(String[] args) {
        FlexQueue queue = new FlexQueue();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.enqueue(40);
        queue.enqueue(50);
        queue.enqueue(60);
        queue.enqueue(60);
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
        System.out.println(Arrays.toString(queue.getAll()));
    }
}
