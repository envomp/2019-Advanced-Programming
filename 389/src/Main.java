import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String[] line1 = scanner.nextLine().split(" ");
            List<String> inputs = new LinkedList<>();
            for (String s : line1) {
                if (!s.equals(" ") && !s.isEmpty()) {
                    inputs.add(s);
                }

            }
            String number = inputs.get(0);
            Integer fromBase = Integer.valueOf(inputs.get(1));
            Integer toBase = Integer.valueOf(inputs.get(2));
            String output = Integer.toString(Integer.parseInt(number, fromBase), toBase).toUpperCase();
            System.out.println(output.length() < 8 ? String.format("%7s",output): "  ERROR");
        }
    }
}