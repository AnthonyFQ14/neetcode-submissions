class Solution {
    public String longestPalindrome(String s) {
        int longest = 0;
        int longestIdx = 0;

        for(int i = 0; i < s.length(); i++){
            
            
            int l = i;
            int r = i;
            while (l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                
                if (r - l + 1 > longest){
                    longest = r - l + 1;
                    longestIdx = l;
                }
                l--;
                r++;
            }
            
            
            l = i;
            r = i + 1;
            while (l >=0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                if (r - l + 1 > longest){
                    longest = r - l + 1;
                    longestIdx = l;
                }
                l--;
                r++;
            }
            
        }
        return s.substring(longestIdx, longestIdx + longest);
    }
}
