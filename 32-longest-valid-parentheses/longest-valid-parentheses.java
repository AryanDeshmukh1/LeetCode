class Solution {
    public int longestValidParentheses(String s) {
        int maxLength = 0;
        Stack<Integer> stack = new Stack<>();
        
        // Base index for valid substring calculation
        stack.push(-1);

        for (int i = 0; i < s.length(); i++) {
            
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();

                // If stack becomes empty, push current index
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    // Calculate valid length
                    maxLength = Math.max(maxLength, i - stack.peek());
                }
            }
        }

        return maxLength;
    }
}