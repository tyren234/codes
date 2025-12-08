package com.flowerishstudios;
import java.util.Arrays;
/*
Given an array of integers nums and an integer target,return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,and you may not use the same element twice.

You can return the answer in any order.

Idea:
1. Sort the array (NlogN)
2. Cover edgecases
    - Array is smaller than two elements
- Store the nubmers and their indeces in hashmap so we know where they were after the sort - problem we have a prolem if there are two same numbers
- another idea, make a record that will store number and it's index and sort it based on it's number
3. Now elements are increasing. Get first and last number. Since the last number is the biggest and the first is the smallest
if target is larger we can just move the pointer on the smallest number forwards. If target is smaller then current sum we can move
the pointer on the biggest number to the left untill we find correct sum.
*/

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        // We don't need to worry about it being less then 2, because it's a given in the task.
        if(nums.length == 2){
            return new int[]{0, 1};
        }

        record Item(int number, int index){};
        Item[] items = new Item[nums.length];
        for(int i = 0; i < nums.length; i++){
            items[i] = new Item(nums[i], i);
        }

        Arrays.sort(items, (item1, item2) -> Integer.compare(item1.number, item2.number));
        int first_index = 0;
        int last_index = nums.length - 1;

        int sum;
        int maxIter = 100000;
        int i = 0;
        // System.out.println("Sorted Items (number, index):");
        // for(Item item: items){
        //     System.out.printf("%d: %d\n", item.number, item.index);
        // }
        while(first_index < last_index){
            // System.out.printf("First index %d\n", first_index);
            // System.out.printf("Last index %d\n", last_index);
            sum = items[first_index].number + items[last_index].number;
            // System.out.printf("Sum %d\n", sum);
            if(sum > target){
                last_index--;
            } 
            else if(sum < target) {
                first_index++;
            }
            else{
                return(new int[]{items[first_index].index, items[last_index].index});
            }
            i++;
            if(i>maxIter){
                System.out.println("Something went terribly wrong");
                return(new int[]{-1});
            }
        }
        return (new int[] { -2 });
    }

    record TestCase( int[] nums, int target, int[] output){};

    private static TestCase[] testCases= new TestCase[] {
        new TestCase(new int[]{2,7,11,15}, 9, new int[]{0,1}),
        new TestCase(new int[]{3,2,4}, 6, new int[]{1,2}),
        new TestCase(new int[]{3,3}, 6, new int[]{0,1}),
        new TestCase(new int[] { 2, 1, 7, 8, 8, 3, 3 }, 6, new int[] { 5, 6 }),
    };
    
    public static void main(String[] args) {
        for(TestCase testCase: testCases)
        {
            int[] result = twoSum(testCase.nums, testCase.target);
            System.out.println( Arrays.equals(result, testCase.output) ? "=== Success! ===" : "=== Failure! ===");
            System.out.println("Nums: " + Arrays.toString(testCase.nums));
            System.out.println("Target: " + testCase.target);
            System.out.println("Expected: " + Arrays.toString(testCase.output));
            System.out.println("Got: " + Arrays.toString(result));
            System.out.println("===========================");
        }
    }
}