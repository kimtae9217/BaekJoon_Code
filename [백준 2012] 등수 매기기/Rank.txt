import java.io.*;
import java.util.*;
import java.math.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int arr[] = new int[n+1];
        
        for(int i=1; i<=n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        
        long ans = 0;
        Arrays.sort(arr);
        
        for(int i=1; i<=n; i++) {
            ans += Math.abs(arr[i]-i);
        }
        
        System.out.println(ans);
    }
}