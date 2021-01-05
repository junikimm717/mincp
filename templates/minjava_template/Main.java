import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        new solver();
        out.close();
    }
    static void line() throws IOException {
        st = new StringTokenizer(in.readLine());
    }
    static class solver {
        solver() throws IOException {
            line();
        }
    }
}
