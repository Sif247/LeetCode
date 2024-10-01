class Solution {
    public static int findMaxConsecutiveOnes(int[] nums)
    {
        int finalRis = 0;
        int var = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                var++;  // Incremento se è 1
            } else {
                finalRis = Math.max(finalRis, var);
                var = 0;
            }
        }

        finalRis = Math.max(finalRis, var);

        return finalRis;
    }




    public static void main(String[] args)
    {
        int []nums1 = {1,1,0,1,1,1};

        int ris = findMaxConsecutiveOnes(nums1);
        System.out.println(ris);

        return;
    }
}




