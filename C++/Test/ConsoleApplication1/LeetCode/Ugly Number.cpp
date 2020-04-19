#include <algorithm>;
#include <cmath>
#include <vector>;
using namespace std;

class Solution {
public:
	bool isUgly(int num) {
		while (num % 2 == 0) 
			num = num / 2;
		while (num % 3 == 0)
			num = num / 3;
		while (num % 5 == 0)
			num = num / 5;
		return num == 1;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};
	int res = s.isUgly(8);
	return 0;
}

