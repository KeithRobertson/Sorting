import java.util.*;

public class BogoSort {

	private static String source;
	private static String target;

	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		if (args.length == 2) {
			source = args[0];
			target = args[1];
		} else {
			System.out.println("Expected 2 arguments: String to be sorted, String to be expected");
			System.exit(0);
		}
		for (int i = 0; i < Integer.MAX_VALUE; i++) {
			String s = randomSort(source);
			System.out.println(s);
			if (s.equals(target)) {
				break;
			}
			if (i == Integer.MAX_VALUE - 1) {
				i = 0;
			}
		}
		long endTime = System.currentTimeMillis();
		long totalSeconds = (endTime - startTime) / 1000;
		System.out.printf("BogoSort took %s seconds", totalSeconds);
	}

	public static String randomSort(String str) {
		List<Character> lettersList = new ArrayList<>();
		for(char c : str.toCharArray()) {
    		lettersList.add(c);
		}
		Collections.shuffle(lettersList);
		StringBuilder sb = new StringBuilder();	
		for (char c : lettersList) {
			sb.append(c);
		}
		return sb.toString();
	}
}
