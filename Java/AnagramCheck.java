import java.util.*;

class AnagramCheck {
	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

        String str1 = sc.next();
        String str2 = sc.next();

        sc.close();
		// Function call
		if (isAnagram(str1, str2))
			System.out.print("The two strings are anagram of each other.");
		else
			System.out.print("The two strings are not anagram of each other.");
	}

    public static boolean isAnagram(String a, String b)
	{
		if (a.length() != b.length()) {
			return false;
		}

		HashMap<Character, Integer> map = new HashMap<>();
		
		for (int i = 0; i < a.length(); i++) {
		
			if (map.containsKey(a.charAt(i))) {
				map.put(a.charAt(i),
						map.get(a.charAt(i)) + 1);
			}
			else {
				map.put(a.charAt(i), 1);
			}
		}

		for (int i = 0; i < b.length(); i++) {
	
			if (map.containsKey(b.charAt(i))) {
				map.put(b.charAt(i),
						map.get(b.charAt(i)) - 1);
			}
			else {
				return false;
			}
		}

        Set<Character> keys = map.keySet();

		for (Character key : keys) {
			if (map.get(key) != 0) {
				return false;
			}
		}
		return true;
	}
}
