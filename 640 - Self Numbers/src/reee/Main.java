package reee;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        boolean[] num = new boolean[1000100];
        Arrays.fill(num, true);
        for(int i = 1; i <= 1000000; i++) {
            if (num[i]) System.out.println(i);
            int n = i;
            int next = n;
            while(n != 0) {
                next += n % 10;
                n /= 10;
            }
            num[next] = false;
        }
    }
}
