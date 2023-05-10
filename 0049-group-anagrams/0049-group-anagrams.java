class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length == 0) return new ArrayList();
        Map<String, ArrayList<String>> map = new HashMap<>();
        for(String c : strs){
            char[] ca = c.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if(!map.containsKey(key)) map.put(key, new ArrayList());
            map.get(key).add(c);
        }
        return new ArrayList(map.values());
    }
}