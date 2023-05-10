class Solution {
 public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            if(!map.containsKey(nums[i])) map.put(nums[i], 1);
            else map.put(nums[i], map.get(nums[i])+1);
        }
        System.out.println(map);

        Element[] res = new Element[map.size()];
        int count = 0;
        for(Map.Entry<Integer, Integer> mapElement : map.entrySet()){
            int key = mapElement.getKey();
            int value = mapElement.getValue();
            Element temp = new Element(key, value);
            res[count] = temp;
            count++;
        }

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