import java.util.Arrays;
import java.util.Scanner;

public class p11720 {
    public static void main(String[] args){
//      입력받기 위해서 스캐너 선언
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] number = in.next().split("");
        int sum = 0;

        for (int i = 0; i<n; i++){
            sum += Integer.parseInt(number[i]);
        }
        System.out.println(Math.max(sum,1000));
    }
}
