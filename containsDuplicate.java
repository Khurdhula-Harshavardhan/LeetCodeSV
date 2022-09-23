/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
*/

import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
       HashMap<Integer, Integer> mapp = new HashMap<>();
        
        for(int x:nums){
            if(mapp.containsKey(x)){
                return true;
            }
            else{
                mapp.put(x,0);
            }
        }
        return false;
    }
}