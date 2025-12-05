public class pattern{
    public static void main(String[] args) {
        int n = 7;
        System.err.println(n/2);
        for (int i=0;i<=n;i++){
            if(i<=n/2+1){
                for (int j=1;j<i;j++){
                    System.out.print(i*j+" ");
                }
            }else{
                for (int j=n;j>i;j--){
                    System.out.print(i*j+" ");
                }
            }
            System.out.println();
        }
    }
}