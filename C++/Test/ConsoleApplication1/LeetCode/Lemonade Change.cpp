#include "LeetCode.h"

class Solution {
public:
	bool lemonadeChange(vector<int>& bills) {
		int changes[3] = { 0, 0, 0 };
		for (int n : bills) {
			if (n == 5)
				changes[0]++;
			else if (n == 10) {
				if (changes[0] == 0)
					return false;
				else {
					changes[0]--;
				}
				changes[1]++;
			}
			else {
				if (changes[1] == 0) {
					if (changes[0] >= 3) {
						changes[0] -= 3;
					}
					else
						return false;
				}
				else {
					changes[1]--;
					if (changes[0] > 0)
						changes[0]--;
					else
						return false;
				}
				changes[2]++;
			}
		}
		return true;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = 
		{ 5,5,5,10,20 }
	;
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	bool res = s.lemonadeChange(v1);

	return 0;
}

