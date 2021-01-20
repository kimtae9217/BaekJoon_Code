import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				
		int[] arr = new int[26];
		
		for(int i = 0; i <  arr.length; i++) {
			arr[i] = -1;
		}
		
		String S = br.readLine();
		
		for(int i = 0; i < S.length(); i++) {
			char alpha = S.charAt(i);
			
			if(arr[alpha - 'a'] == -1) {
				arr[alpha - 'a'] = i;
			}
		}
		
		for(int val : arr) {
			System.out.print(val + " ");
		}
	}
}