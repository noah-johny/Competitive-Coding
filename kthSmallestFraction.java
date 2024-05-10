import java.util.*;

class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingDouble(a -> (double)a[0] / (double)a[1]));

        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                minHeap.offer(new int[] { arr[i], arr[j] });
            }
        }

        while (k-- > 1) {
            minHeap.poll();
        }

        return minHeap.poll();
    }
}
