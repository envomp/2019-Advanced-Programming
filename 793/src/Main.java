import java.io.*;

public class Main {
    private static int[] ints;

    private static int findSet(int i) {
        return (ints[i] == i) ? i : (ints[i] = findSet(ints[i]));
    }

    private static void upgradeSet(int i, int j) {
        ints[findSet(i)] = ints[findSet(j)];
    }

    private static boolean isSameSet(int i, int j) {
        return findSet(i) == findSet(j);
    }

    private static void initSet(int _size) {
        ints = new int[_size];
        for (int i = 0; i < _size; i++)
            ints[i] = i;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        String line;
        br.readLine();
        String[] splits;
        int yes, no;
        for (int i = 0; i < t; i++) {
            yes = 0;
            no = 0;
            initSet(Integer.parseInt(br.readLine()));
            while ((line = br.readLine()) != null && !line.equals("")) {
                splits = line.split(" ");
                if (splits[0].charAt(0) == 'c') {
                    upgradeSet(Integer.parseInt(splits[1]) - 1, Integer.parseInt(splits[2]) - 1);
                } else {
                    if (isSameSet(Integer.parseInt(splits[1]) - 1, Integer.parseInt(splits[2]) - 1))
                        yes++;
                    else
                        no++;
                }
            }
            out.append(yes).append(",").append(no).append("\n");
            if (i != t - 1)
                out.append("\n");
        }
        System.out.print(out);
    }
}