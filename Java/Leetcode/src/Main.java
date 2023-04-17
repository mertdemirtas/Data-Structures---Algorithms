import java.util.*;

public class Main {

    static int lengthOfLastWord(String s) {
        String[] splittedArray = s.split(" ");
        return splittedArray[splittedArray.length - 1].length();
    }

    static int longestOnesOlmadi(int[] nums, int k) {
        int max = 0;

        for (int i = 0; i < nums.length; i++) {
            int tempK = k;
            int windowSum = 0;
            int index = i;
            while (tempK > 0 || nums[index] == 1) {
                if (nums[index] == 0)
                    tempK--;
                windowSum++;
                index++;
                if(index == nums.length)
                    break;
            }
            max = Math.max(windowSum, max);
        }
        return max;
    }

    static int longestOnes(int[] nums, int k) {
        int max = 0;
        int windowSum = 0;
        int tempK = k;
        int index = 0;

        while(index < nums.length) {
            if(nums[index] == 0 && tempK > 0)
                tempK--;

            else if(nums[index] != 1) {
                index = index - windowSum + 1;
                windowSum = 0;
                tempK = k;
                continue;
            }
            windowSum++;
            index++;
            max = Math.max(windowSum, max);
        }
        return max;
    }

    static boolean checkString(String s) {
        boolean containsB = false;
        for(var ch: s.toCharArray()) {
            if(ch == 'b') {
                containsB = true;
            }
            if(containsB && ch == 'a')
                return false;
        }
        return true;
    }

    static int minInsertions(String s) {
        Stack<Character> stack = new Stack<>();

        for(var ch: s.toCharArray()) {
            if(ch == '(') {
                stack.add(ch);
            }
            else if(!stack.isEmpty()) {

            }
        }

        return 0;
    }

    static int minimumDifference(int[] nums, int k) {
        if(nums.length == 1 || k == 1)
            return 0;
        Arrays.sort(nums);
        int windowMin = 0;
        int tempK = k;
        int min = Integer.MAX_VALUE;

        for(int i = 0; i < nums.length - k + 1; i++) {
            windowMin = 0;
            tempK = k;

            for(int j = i; tempK > 0; j++, tempK--) {
                windowMin += Math.abs(nums[j] - nums[j + 1]);
            }
            min = Math.min(min, windowMin);
        }
        return min;
    }

    static String[] divideString(String s, int k, char fill) {
        int temp = s.length() % k;
        if(temp== 0)
            return s.split("(?<=\\G.{" + k + "})");


        for(int i = 0; i < (k - temp); i++)
            s += fill;
        return s.split("(?<=\\G.{" + k + "})");
    }

    static String removeDigit(String number, char digit) {
        String tempNumber = "";
        for(int i = 0; i < number.length(); i++) {
            if(number.charAt(i) == digit) {
                String result = number.substring(0,i) + number.substring(i + 1);
                if(result.compareTo(tempNumber) > 0) {
                    tempNumber = result;
                }
            }
        }
        return tempNumber;
    }

    static int numJewelsInStones(String jewels, String stones) {
        int temp = 0;
        char[] stonesChs = stones.toCharArray();
        Arrays.sort(stonesChs);
        String sortedStones = new String(stonesChs);
        for(var ch: jewels.toCharArray()) {
            temp += binarySearchnumJewelsInStones(sortedStones, ch);
        }
        return temp;
    }

    static boolean isPowerOfTwo(int n) {
        if(n < 1) return false;
        while(n % 2 == 0) n /= 2;
        return (n == 1);
    }

    static int maxProduct(String[] words) {
        int temp = 0;


        return temp;
    }

    static int searchInsert(int[] nums, int target) {
        Arrays.sort(nums);
        return binaryFind(nums, target);
    }

    static int binaryFind(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while(left <= right) {
            int mid = (right + left) / 2;
            if(nums[mid] < target) left = mid + 1;
            else if(nums[mid] > target) right = mid - 1;
            else if (nums[mid] == target) return mid;
        }
        return left;
    }

    static int binarySearchnumJewelsInStones(String stones, char searchChar) {
        int right = stones.length() - 1;
        int left = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if(stones.charAt(mid) < searchChar) {
                left = mid + 1;
            }
            else if(stones.charAt(mid) > searchChar) {
                right = mid - 1;
            }
            else if(mid - 1 >= 0 && stones.charAt(mid - 1) == searchChar) {
                right = mid - 1;
            }
            else {
                left = mid;
                break;
            }
        }

        right = stones.length() - 1;
        int tempLeft = left;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if(stones.charAt(mid) < searchChar) {
                left = mid + 1;
            }
            else if(stones.charAt(mid) > searchChar) {
                right = mid - 1;
            }
            else if(mid + 1 <= stones.length() - 1 && stones.charAt(mid + 1) == searchChar) {
                left = mid + 1;
            }
            else {
                right = mid;
                break;
            }
        }
        return right - tempLeft + 1;
    }

    static int coinChange(int[] coins, int amount) {
        if(amount == 0) return 0;
        Arrays.sort(coins);

        for(int i = coins.length - 1; i >= 0; i--) {

        }

        return -1;
    }

    static int convertTime(String current, String correct) {
        int currentTime = Integer.parseInt(current.substring(0,2)) * 60 + Integer.parseInt(current.substring(3,5));
        int correctTime = Integer.parseInt(correct.substring(0,2)) * 60 + Integer.parseInt(correct.substring(3,5));
        int[] minutes = {60, 15, 5, 1};
        int temp = 0;
        if(correctTime < currentTime) correctTime += 1440;
        int diff = correctTime - currentTime;
        for(var element: minutes) {
            temp += diff / element;
            diff %= element;
            if(diff == 0) return temp;
        }
        return temp;
    }

    static int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        int max = 0;
        int firstMax = 0;
        int secondMax = 0;

        for(int i = 0; i < firstLen; i++) firstMax += nums[i];

        max = firstMax + secondMax;
        int windowMax = max;
        return max;
    }

    static long makeIntegerBeautiful(long n, int target) {
        long digitSum = findDigitSum(n);
        long added = 0;
        long temp = 1;
        while (digitSum > target) {
            long lastDigit = n % 10;
            if(lastDigit == 0) {
                n /= 10;
                temp *= 10;
                continue;
            }
            else {
                added += (10 - lastDigit) * temp;
                n += (10 - lastDigit);
            }
            digitSum = findDigitSum(n);
        }
        return added;
    }

    static long findDigitSum(long num) {
        long digitSum = 0;
        while(num >= 1) {
            long lastDigit = num % 10;
            digitSum += lastDigit;
            num /= 10;
        }
        return digitSum;
    }

    static boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        String firstSum = "";
        String secondSum = "";
        String targetSum = "";
        for(var ch: firstWord.toCharArray()) firstSum += ch - 97;
        for(var ch: secondWord.toCharArray()) secondSum += ch - 97;
        for(var ch: targetWord.toCharArray()) targetSum += ch - 97;
        return (Integer.parseInt(firstSum) + Integer.parseInt(secondSum) == Integer.parseInt(targetSum));
    }

    static List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> list = new LinkedList<>();
        double number = 0;
        double temp = Math.pow(10, num.length - 1);

        for(var digit : num) {
            number += digit * temp;
            temp /= 10;
        }
        number += k;

        while(number >= 1) {
            long lastDigit = (long)number % 10;
            list.add((int) lastDigit);
            number /= 10;
        }
        Collections.reverse(list);
        return list;
    }

    static int maximumUnits(int[][] boxTypes, int truckSize) {
        int max = 0;
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1],a[1]));
        int index = 0;
        while(truckSize > 0) {
            int boxCount = boxTypes[index][0];
            if(truckSize > boxCount) {
                truckSize -= boxCount;
                max += boxCount * boxTypes[index][1];
                index++;
            }
            else {
                max += truckSize * boxTypes[index][1];
                truckSize = 0;
            }
        }
        return max;
    }

    static String reverseVowels(String s) {
        Queue<Character> queue = new LinkedList<>();
        for(var ch : s.toCharArray())
            if(ch == 'a' || ch == 'A' || ch == 'e' || ch == 'E' || ch == 'i' || ch == 'I' || ch == 'o' || ch == 'O' || ch == 'u' || ch == 'U') queue.add(ch);

        StringBuilder string = new StringBuilder(s);

        for(int i = s.length() - 1; i >= 0; i--) {
            int ch = s.charAt(i);
            if(ch == 'a' || ch == 'A' || ch == 'e' || ch == 'E' || ch == 'i' || ch == 'I' || ch == 'o' || ch == 'O' || ch == 'u' || ch == 'U') string.setCharAt(i, queue.poll());
        }
        return String.valueOf(string);
    }

    static boolean isUgly(int n) {
        while(n > 0) {
            if(n % 2 == 0) n /= 2;
            else if(n % 3 == 0) n /= 3;
            else if(n % 5 == 0) n /= 5;
            else return false;
        }
        return true;
    }

    static List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> list = new ArrayList<>();
        Set<Integer> set = new HashSet<>();

        for(var element : nums)
            set.add(element);

        for(int i = 1; i <= set.size(); i++)
            if(!set.contains(i))
                list.add(i);
        return list;
    }

    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int min = nums[0];
        if(nums.length == 1) return min;
        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(nums[mid] > min) left = mid + 1;
            else if(nums[mid] <= min && nums[mid] < nums[right]) {
                right = mid - 1;
                min = nums[mid];
            }
            else if(nums[mid] <= min) {
                left = mid + 1;
                min = nums[mid];
            }
        }
        return min;
    }

    static int[] evenFirst(int[] nums) {
        int left = 0, right = nums.length - 1;
        while(left < right) {
            if(nums[left] % 2 == 0) left++;
            else {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right--] = temp;
            }
        }
        return nums;
    }


    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }


    static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergedList = new ListNode();
        ListNode current = mergedList;

        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            }
            else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        current.next = list1 != null ? list1 : list2;
        return mergedList.next;
    }

    static ListNode deleteDuplicates(ListNode head) {
        ListNode temp = head;

        while(temp != null) {
            ListNode next = temp.next;
            while(next != null && temp.val == next.val) {
                next = next.next;
            }
            temp.next = next;
            temp = next;
        }
        return head;
    }

    static ListNode reverseList(ListNode head) {
        ListNode reversed = new ListNode();

        while(head.next != null) {
            reversed.val = head.val;
            head = head.next;
            reversed.next = new ListNode();
        }
        return reversed;
    }

    public static void main(String[] args) {
        String str = "23:00";
        String str2 = "00:01";
        int[] nums = {0};
        int[][] nums2D = {{5,10},{2,5},{4,7},{3,9}};
        int temp = 516;

        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(3))));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        int x = 2;
        for(int i = 1; i < 2; i++) {
            for(int j = 1; j < 2;j++) {
                x *= 2;
            }
        }
        System.out.println(x);
        System.out.println(deleteDuplicates(list1));
    }
}