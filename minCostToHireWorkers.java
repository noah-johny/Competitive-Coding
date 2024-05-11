import java.util.*;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        PriorityQueue<Integer> maxQualityHeap = new PriorityQueue<>(Collections.reverseOrder());
        List<AbstractMap.SimpleEntry<Double, Integer>> ratio = new ArrayList<>();
        int size = quality.length, qualitySum = 0;
        double minCost = Double.MAX_VALUE, maxRatio = 0.0;

        for(int i=0; i<size; i++) {
            ratio.add(new AbstractMap.SimpleEntry<>((double) wage[i] / quality[i], i));
        }

        ratio.sort(Comparator.comparingDouble(a -> a.getKey()));

        for(int i=0; i<k; i++) {
            int currQuality = quality[ratio.get(i).getValue()];

            qualitySum += currQuality;
            maxQualityHeap.offer(currQuality);
            maxRatio = Math.max(maxRatio, ratio.get(i).getKey());
        }

        minCost = maxRatio * qualitySum;

        for(int i=k; i<size; i++) {
            int currQuality = quality[ratio.get(i).getValue()];

            qualitySum -= maxQualityHeap.poll();
            qualitySum += currQuality;

            maxQualityHeap.offer(currQuality);
            maxRatio = Math.max(maxRatio, ratio.get(i).getKey());

            minCost = Math.min(minCost, maxRatio * qualitySum);
        }

        return minCost;
    }
}