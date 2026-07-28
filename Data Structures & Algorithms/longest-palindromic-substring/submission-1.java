class Solution {
    public String longestPalindrome(String s) {
        int longest = 0;
        String longestStr = "";

        for(int i = 0; i < s.length(); i++){
            
            
            int l = i;
            int r = i;
            while (l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                String cur = s.substring(l,r + 1);
                int curLen = r - l + 1;

                if(curLen > longest){
                    longest = curLen;
                    longestStr = cur;
                }
                l--;
                r++;
            }
            
            
            l = i;
            r = i + 1;
            while (l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                String cur = s.substring(l,r + 1);
                int curLen = r - l + 1;

                if(curLen > longest){
                    longest = curLen;
                    longestStr = cur;
                }
                l--;
                r++;
            }
            
        }
        return longestStr;
    }
}
