import java.lang.*;
import java.util.*;
import java.io.*;

class twoSum{
    public static void main(String args[]){
        //abstract just like that.
    }
}

//here is the solution Class.
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        //Creating a HashMap since it's lookup time is O(1) instead of Binary Search which is O(NlogN).
        HashMap<Integer, Integer> numbers = new HashMap<>();
        List<Integer> indexes = new ArrayList<>();
        int[] solutionPair = new int[2];
        //Adding all values to HashMap instance from array.
        for(int i=0; i<nums.length; i++){
            numbers.put(nums[i], i);
        }
        
        for(int i=0;i<nums.length; i++){
            if(numbers.containsKey(target - nums[i])){
                if(i != (numbers.get(target - nums[i])).intValue()){
                    solutionPair[0] = i;
                    solutionPair[1] = (numbers.get(target - nums[i])).intValue();
                    break;
                }
            }
        }
        
        return solutionPair;
    }
}