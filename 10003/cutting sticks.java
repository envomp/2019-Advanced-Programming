import java.util.Arrays;
import java.util.Scanner;

//10003
public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        long time = 0;

        while (scanner.hasNextLine()) {

            long start = System.nanoTime();
            int l = Integer.parseInt(scanner.nextLine());
            if (l == 0) {
                break;
            }
            scanner.nextLine();

            int[] cutLocs;
            String thirdLine = scanner.nextLine();
            if (thirdLine.length() == 0){
                System.out.println("The minimum cutting is 0.");
                continue;
            } else {
                cutLocs = Arrays.stream(thirdLine.split(" ")).mapToInt(Integer::parseInt).toArray();
            }

            int[][] table = new int[cutLocs.length + 1][cutLocs.length + 1];

            for (int x = 1; x <= cutLocs.length; x++) {
                for (int y = x - 1; y >= 0; y--) {
                    int min = Integer.MAX_VALUE;
                    for (int x_temp = y; x_temp < x; x_temp++)
                        min = Math.min(min, table[y][x_temp] + table[x_temp + 1][x]);
                    table[y][x] = min + (x < cutLocs.length ? cutLocs[x] : l) - (y > 0 ? cutLocs[y - 1] : 0);
                }
            }
            System.out.format("The minimum cutting is %d.\n", table[0][cutLocs.length]);
            time += System.nanoTime() - start;
        }

//        System.out.println(time / 1000000d);
    }
}
