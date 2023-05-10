class Solution {
 public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(!map.containsKey(nums[i])) map.put(nums[i], 1);
            else map.put(nums[i], map.get(nums[i]) + 1);
        }
        // now we have a map of the elements and their frequency
        // we need to traverse tha map and get an array out of it 
        // which we can sort and return top k elements from

        // we can create an object that has 2 attributes
        // one being the key which is the number itself and the other being its frequency

        // lets name the object Element
        Element[] res = new Element[map.size()];
        int count = 0;
        // we need to know how to iterate over a map 
        // for (Map.Entry<String,Integer> mapElement : hm.entrySet()) {
            // String key = mapElement.getKey();
        for(Map.Entry<Integer, Integer> mapElement : map.entrySet()){
            int key = mapElement.getKey();
            int value = mapElement.getValue();
            Element temp = new Element(key, value);
            res[count] = temp;
            count++;
        }
        // we got the array of integer and integer frequencies
        // we should be able to sort it and iterate over it now
        Arrays.sort(res, (a,b) -> b.value - a.value);
        int[] ans = new int[k];
        for(int i = 0; i < k; i++){
            ans[i] = res[i].key;
        }
        return ans;
    }
}

class Element {

    public int key;
    public int value;

    public Element(int a, int b){
        key = a;
        value = b;
    }
}