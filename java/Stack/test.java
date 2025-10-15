import java.util.Arrays;

public class test {
    public static void main(String[] args) {
        simpleStack stack = new simpleStack(5);
        System.out.println(Arrays.toString(stack.getAll()));
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);
        stack.pop();
        stack.pop();
        stack.pop();
        System.out.println(Arrays.toString(stack.getAll()));
    }    
}