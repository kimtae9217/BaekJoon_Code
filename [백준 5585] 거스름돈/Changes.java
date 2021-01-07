import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
            
        int changes = 1000 - sc.nextInt();
        int[] coins = {500, 100, 50, 10, 5, 1};
       
        int result = 0;
        
        for(int i = 0; i < coins.length; i++){
            if(changes / coins[i] != 0){
                result += changes / coins[i];
                changes %= coins[i];
            }
        }
        
        System.out.println(result);
        
        sc.close();
        return;
	}
}