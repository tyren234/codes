package com.flowerishstudios;

import java.util.Map;

public class RomanToInteger {
    public static int romanToInt(String s) {
        /* Go over all characters. 
        Check:
        1. If the next character is the same. If it is, save the partial sum and move i to the next character.
        2. If the next character is larger then current one, 
        subtract partial sum from the next character and store it as the new partial sum.
            - XL - 40
        3. If the next character is smaller then add partial sum to the sum.
        */
        Map<Character, Integer> mapping = Map.of(
            'I', 1,
            'V', 5,
            'X', 10,
            'L', 50,
            'C', 100,
            'D', 500,
            'M', 1000
        );

        int i = 0;
        int sum = 0;

        while(i < s.length()) {
            // last character
            if(i == s.length()-1){
                sum += mapping.get(s.charAt(i));
                break;
            }   

            // get this and get next character
            Character thisCharacter = s.charAt(i);
            int thisValue = mapping.get(thisCharacter);
            Character nextCharacter = s.charAt(i+1);
            int nextValue = mapping.get(nextCharacter);
            
            if(thisValue >= nextValue) {
                sum += thisValue;
            }
            else{
                sum += (nextValue - thisValue);
                i++;
            }
            
            i++;
        }
        return sum;
    }

    public static void main(String[] args){
        record TestCase(String romanNumeral, int expected){};

        TestCase[] testCases = new TestCase[]{
            new TestCase("I", 1),
            new TestCase("III", 3),
            new TestCase("IX", 9),
            new TestCase("LIX", 59),
            new TestCase("LVI", 56),
            new TestCase("LVIII", 58),
            new TestCase("MCMXCIV", 1994),
            new TestCase("MDCLXVI", 1666),
            new TestCase("MMMDCCCLXXXVIII", 3888),
        };

        for(TestCase testCase: testCases){
            int output = romanToInt(testCase.romanNumeral);
            if (output == testCase.expected) {
                System.out.printf("Succeeded for %s, expected %d\n", testCase.romanNumeral, testCase.expected);        
            }
            else{
                System.out.printf("Failed for %s, expected %d, got %d\n", testCase.romanNumeral, testCase.expected, output);
            }
        }
    }
}
