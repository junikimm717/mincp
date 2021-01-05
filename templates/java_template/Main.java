import java.io.*;
import java.util.*;

public class Main {
    static PrintWriter out;
    static class FIO {
        BufferedReader in;
        StringTokenizer st;
        FIO() throws IOException {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }
        FIO(String name) throws IOException {
            in = new BufferedReader(new FileReader(name + ".in"));
            out = new PrintWriter(new FileWriter(name + ".out"));
        }
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int ni() {
            return Integer.parseInt(next());
        }
        long nl() {
            return Long.parseLong(next());
        }
        double nd() {
            return Double.parseDouble(next());
        }
    }
    static FIO in;
    public static void main (String[] args) throws IOException {
        in = new FIO();
        new solver();
        out.close();
    }
    static class solver {
        solver() {

        }
    }
}

