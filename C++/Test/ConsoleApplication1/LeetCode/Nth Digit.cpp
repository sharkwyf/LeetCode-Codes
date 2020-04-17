#include <algorithm>;
#include <cmath>
#include <vector>;
using namespace std;

class Solution {
public:
	int findNthDigit(int n) {
		unsigned long a = pow(10, 8);
		a = a * 81;
		int i = 0;
		unsigned long count = (i + 1) * 9 * pow(10, i);
		while (n > count) {
			n -= count;
			i++;
			count = (i + 1) * 9 * pow(10, i);
		}
		int num = pow(10, i) - 1 + ceil(n / (i + 1.0));
		int pos = (i + 1 - (n % (i + 1))) % (i + 1);
		while (pos > 0) {
			num = num / 10;
			pos--;
		}
		return num % 10;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> v = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};
	int res = s.findNthDigit(1000000000);
	return 0;
}

