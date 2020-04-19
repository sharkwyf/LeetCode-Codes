#include <vector>;
using namespace std;

class Solution {
public:
	int minFallingPathSum(vector<vector<int>>& A) {
		int height = A.size();
		if (height == 0)
			return -1;
		int width = A[0].size();
		if (width == 0)
			return -1;
		for (int i = 1; i < height; i++) {
			for (int j = 0; j < width; j++) {
				int m = A[i - 1][j];
				if (1 <= j && A[i - 1][j - 1] < m)
					m = A[i - 1][j - 1];
				if (j < width - 1 && A[i - 1][j + 1] < m)
					m = A[i - 1][j + 1];
				A[i][j] += m;
			};
		};
		int min = INT32_MAX;
		for (int i = 0; i < width; i++) {
			if (A[height - 1][i] < min)
				min = A[height - 1][i];
		}
		return min;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};
	int res = s.minFallingPathSum(v);
	return 0;
}

