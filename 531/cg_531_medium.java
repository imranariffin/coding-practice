public class Solution {
    public int findLonelyPixel(char[][] picture) {
      int lonelyBlackPixel = 0;

      for (int i = 0; i < picture.length; i++) {
        for (int j = 0; j < picture[i].length; j ++) {
          if (picture[i][j] == 'B' && isLonelyBlack(picture, i, j)) lonelyBlackPixel++;
        }
      }

      return lonelyBlackPixel;
    }

    private boolean isLonelyBlack(char[][] picture, int row, int col) {
      if (getBlackInRow(picture, row) > 1 || getBlackInColumn(picture, col) > 1) return false;

      return true;
    }

    private int getBlackInColumn(char[][] picture, int col) {
        int blackCount = 0;

        for (int i = 0; i < picture.length; i++) {
            if (picture[i][col] == 'B') {
              blackCount += 1;
            }
        }

        return blackCount;
    }

    private int getBlackInRow(char[][] picture, int row) {
        int blackCount = 0;

        for (int i = 0; i < picture[row].length; i++) {
            if (picture[row][i] == 'B') {
              blackCount += 1;
            }
        }

        return blackCount;
    }
}
