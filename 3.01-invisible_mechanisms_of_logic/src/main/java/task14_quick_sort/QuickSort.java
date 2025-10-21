package task14_quick_sort;

import java.util.Arrays;

public class QuickSort {
    /**
     * {P: arr.length > 0}
     * quickSort(arr)
     * {Q: arr sorted ASC}
     */
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array must not be null or empty");
        }

        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * {P: left < right}
     * quickSort(arr, left, right)
     * {Q: arr[left..right] sorted ASC}
     */
    private static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(arr, left, right);
            quickSort(arr, left, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, right);
        }
    }

    /**
     * {P: true}
     * partition(arr, left, right)
     * {Q: arr[left..pivotIndex-1] <= arr[pivotIndex] <= arr[pivotIndex+1..right]}
     *
     * Loop invariant:
     * {I: arr[left..store-1] <= pivot and arr[store..i-1] > pivot}
     */
    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int store = left;

        for (int i = left; i < right; i++) {
            if (arr[i] <= pivot) {
                swap(arr, i, store);
                store++;
            }
        }
        swap(arr, store, right);
        return store;
    }

    /**
     * {P: true}
     * swap(arr, a, b)
     * {Q: values arr[a] and arr[b] swapped}
     */
    private static void swap(int[] arr, int a, int b) {
        int t = arr[a];
        arr[a] = arr[b];
        arr[b] = t;
    }

    public static void main(String[] args) {
        int[] arr = {8, -3, 1, 7, 0, 10, 2};
        System.out.println("Before: " + Arrays.toString(arr)); // Before: [8, -3, 1, 7, 0, 10, 2]
        quickSort(arr);
        System.out.println("After:  " + Arrays.toString(arr)); // After:  [-3, 0, 1, 2, 7, 8, 10]
    }
}
