public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int minRadius = 0;

        for (int i = 0; i < houses.length; i++) {
            int house = houses[i];
            int localMinRadius = Math.abs(getClosestHeater(heaters, house) - house);

            minRadius = localMinRadius > minRadius ? localMinRadius : minRadius;
        }

        return minRadius;
    }

    private int getClosestHeater(int[] heaters, int house) {
        Arrays.sort(heaters);

        int candidateHeaterIndex = binarySearch(heaters, house);

        if (candidateHeaterIndex > 0 && Math.abs(heaters[candidateHeaterIndex - 1] - house) < Math.abs(heaters[candidateHeaterIndex] - house)) {
            return heaters[candidateHeaterIndex - 1];
        }

        return heaters[candidateHeaterIndex];
    }

    private int binarySearch(int[] a, int key) {
        int lo = 0;
        int hi = a.length - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;

            if (a[mid] < key) {
                lo = mid + 1;
            }
            else {
                hi = mid;
            }
        }

        return lo;
    }
}
