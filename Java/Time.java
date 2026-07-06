class Mythread extends Thread{
    public  void run(){
        try{
            int i;
            for(i=1; i<20; i=i+2){
                System.out.println("i=" +i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException ex) {
            System.getLogger(Mythread.class.getName()).log(System.Logger.Level.ERROR, (String) null, ex);
        }
    }
}
class yourthread extends Thread{
    public  void run(){
        try{
            int i;
            for(i=2; i<20; i=i+2){
                System.out.print("i=" +i);
                for(int j=0;j<20;j++){
                    System.out.print(" ");
                }
            System.out.print("Time");
            System.out.println("");
                Thread.sleep(1000);
            }
        } catch (InterruptedException ex) {
            System.getLogger(Mythread.class.getName()).log(System.Logger.Level.ERROR, (String) null, ex);
        }
    }
}
public class Time{
    public static void main(String[] args) {
        Mythread m1 = new Mythread();
        yourthread y1 =new yourthread();
        m1.start();
        y1.start();
    }
}