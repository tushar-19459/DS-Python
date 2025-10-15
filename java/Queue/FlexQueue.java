public class FlexQueue {
    public int[] data = new int[5];
    public int count;
    public int frount=0;
    public int rear=0;

    public FlexQueue(){

    }

    public boolean isEmpty(){
        return count==0;
    }

    public void enqueue(int ele){
        if (count==data.length){
            resize(data.length*2);
        }
        data[rear] = ele;
        count++;
        rear = (rear+1)%data.length;
    }
    
    public void dequeue(){
        if(!isEmpty()){
            if(count<=(int)(data.length/2)){
                resize((int)(data.length/2));
            }
        }
        data[frount] = 0;
        frount++;
        count--;
    }

    public void resize(int size){
        int [] newdata = new int[size];
        for(int i=0 ;i<count;i++){
            newdata[i] = data[((frount+i)%data.length)];
        }
        frount=0;
        rear = count;
        data = newdata;
    }

    public int[] getAll(){
        return data;
    }

}
