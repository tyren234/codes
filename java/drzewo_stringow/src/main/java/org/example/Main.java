package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.Math;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {
    public static List<String> findLeaves(String[] graph) {
        List<String> leaves = new ArrayList<>();
        findLeavesHelperr(graph, 0, leaves);
        return leaves;
    }


    private static void findLeavesHelperr(String[] graph, int index, List<String> leaves) {
        if (index >= graph.length || graph[index] == null) {
            return; // Base case: null node or out of bounds
        }

        int leftChildIndex = 2 * index + 1;
        int rightChildIndex = 2 * index + 2;

        boolean hasLeftChild = leftChildIndex < graph.length && graph[leftChildIndex] != null;
        boolean hasRightChild = rightChildIndex < graph.length && graph[rightChildIndex] != null;

        if (!hasLeftChild && !hasRightChild) {
            // Node is a leaf
            leaves.add(graph[index]);
        } else {
            // Recursively check left and right children
            findLeavesHelperr(graph, leftChildIndex, leaves); // Left child
            findLeavesHelperr(graph, rightChildIndex, leaves); // Right child
        }
    }

    private static String makeWordFromNode(String[] graph, String node){
        int nodeIndex = getIndexFromNodeString(node) + 1;
        String word = "";
        while (nodeIndex > 0){
            word += graph[nodeIndex - 1].charAt(0);
            nodeIndex /= 2;
        }
        return word;
    }

    public static int getIndexFromNodeString(String node){
        if (node.length() == 1){
            return 0;
        }
        int indexLitery = 2;
        int indexGrafu = 1;
        int dlugoscSlowa = node.length();

        while (indexLitery < dlugoscSlowa) {
            char litera = node.charAt(indexLitery);
            if (litera == 'L'){
                indexGrafu *= 2;
            }
            else{
                indexGrafu = (2 * indexGrafu) + 1;
            }
            indexLitery++;
        }
        return indexGrafu - 1;
    }

    public static void main(String[] args) {
        String[] slowa = null;
        int liczbaNodeow = 0;
        int maxDlugoscSlowa = 0;
        try {
            BufferedReader read = new BufferedReader(new FileReader(args[0]));
            liczbaNodeow = (int) Files.lines(Paths.get(args[0])).count();
            slowa = new String[liczbaNodeow];
            String linia = "";
            int i = 0;
            while ((linia = read.readLine()) != null) {
                slowa[i] = linia;
                i++;
                if (maxDlugoscSlowa < linia.length()){
                    maxDlugoscSlowa = linia.length();
                }
            }
            read.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        int wielkoscGrafu = (int) (Math.pow(2, (maxDlugoscSlowa - 1)) - 1);
        String[] graf = new String[wielkoscGrafu];

        for (String slowo : slowa){
            // "X LRRLRRRRRLLLRLRRRLRL"
            int indexGrafu = getIndexFromNodeString(slowo);
            graf[indexGrafu] = slowo;
        }

        List<String> leaves = findLeaves(graf);
        char najdalszaLiteraAlfabetycznie = 'A';
        for (String leaf: leaves){
            if ((int)leaf.charAt(0) > (int) najdalszaLiteraAlfabetycznie){
                najdalszaLiteraAlfabetycznie = leaf.charAt(0);
            }
        }

        ArrayList<String> worstWords = new ArrayList<String>();
        for (String leaf: leaves){
            if (leaf.charAt(0) == najdalszaLiteraAlfabetycznie){
                String word = makeWordFromNode(graf, leaf);
                worstWords.add(word);
            }
        }

        Object[] output = worstWords.toArray();
        Arrays.sort(output);

        System.out.println("Wszytskie najgorsze słowa:");
        for (Object word : output){
            System.out.println(word);
        }

        System.out.println("\nNajgorsze słowo:");
        System.out.println(output[output.length - 1]);
    }
}