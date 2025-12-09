package com.flowerishstudios;

public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        String text = Integer.toString(x);
        if(text.length() < 2){
            return true;
        }
        int start = 0;
        int end = text.length() - 1;
        while(start < end){
            if(text.charAt(start) != text.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }

    public static void main(String[] args){
        System.out.println(isPalindrome(121) == true ? "Success" : "Failure" );
        System.out.println(isPalindrome(-121) == false ? "Success" : "Failure");
        System.out.println(isPalindrome(10) == false ? "Success" : "Failure");
        System.out.println(isPalindrome(1025910) == false ? "Success" : "Failure");
        System.out.println(isPalindrome(345676543) == true ? "Success" : "Failure");
    }
}
