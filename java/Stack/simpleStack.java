public class simpleStack {
    public int size = 0;
    public int count = 0;
    public int top = 0;
    public int data[];

    public simpleStack(int size){
        this.size  = size;
        data = new int[size];
    }
    
    public boolean isEmpty(){
        return count==0;
    }

    public boolean isFull(){
        return count==data.length;
    }

    public int[] getAll(){
        return data;
    }

    public void push(int ele){
        if(!isFull()){
            data[top] = ele;
            top++;
            count++;
            System.out.println("pushed "+ele);
        }
    }

    public void pop(){
        if(!isEmpty()){
            top--;
            data[top] = 0;
            count--;
        }
    } 

}