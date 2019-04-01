import java.io.InputStream;
import java.util.Scanner;

public class Main {
    private static final boolean DEBUG = true;

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        Scanner in = new Scanner(inputStream);

        while (in.hasNextInt()) {

            int n = in.nextInt();
            int[][][] parent = new int[n][n][n];
            double[][][] dist = new double[n][n][n];

            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j) {
                    dist[i][j][0] = (i != j) ? in.nextDouble() : 1.0;
                    parent[i][j][0] = i;
                }

            if (DEBUG) initValues(dist);

            // https://www.algorithmist.com/index.php/Floyd-Warshall%27s_Algorithm
            // https://www.youtube.com/watch?v=4OQeCuLYj-4

            for (int a = 1; a < n; a++)
                for (int b = 0; b < n; b++)
                    for (int u = 0; u < n; u++)
                        for (int v = 0; v < n; v++) {
                            double d = dist[u][b][a - 1] * dist[b][v][0];

                            if (dist[u][v][a] < d) {
                                dist[u][v][a] = d;
                                parent[u][v][a] = b;
                            }
                        }
            if (DEBUG) values(dist);

            boolean isProfit = false;

            if (DEBUG) System.out.println();
            for (int s = 1; s < n && !isProfit; s++)
                for (int u = 0; u < n; u++) {
                    if (DEBUG) System.out.println(u + " " + s + " " + dist[u][u][s]);
                    if (dist[u][u][s] > 1.01) {
                        isProfit = true;
                        int[] profit = new int[s + 1];
                        profit[s] = parent[u][u][s];
                        if (DEBUG) System.out.println();
                        for (int j = s - 1; j >= 0; --j) profit[j] = parent[u][profit[j + 1]][j];
                        for (int j = 0; j <= s; j++) {
                            System.out.printf("%d ", profit[j] + 1);
                        }
                        System.out.println(profit[0] + 1);
                        break;
                    }
                }

            if (!isProfit)
                System.out.println("no arbitrage sequence exists");
        }
    }

    private static void initValues(double[][][] dist) {
        System.out.println("initial values:\n");
        for (var x : dist) {
            for (var y : x) {
                System.out.print(y[0] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static void values(double[][][] dist) {
        System.out.println("values:\n");
        for (var x : dist) {
            for (var y : x) {
                for (var z : y) {
                    System.out.print(z + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
        System.out.println();
    }
}
