#include "LeetCode.h"


class Solution {
public:
	vector<int> addNegabinary(vector<int>& arr1, vector<int>& arr2) {
		vector<int> buff;
		int len1 = arr1.size(), len2 = arr2.size();
		int i = 0, c = 0;
		while (i < len1 || i < len2 || c != 0) {
			int r = (i < len1 ? arr1[len1 - 1 - i] : 0) + (i < len2 ? arr2[len2 - 1 - i] : 0) - c;
			buff.push_back((r + 2) % 2);
			c = floor(r / 2.0);
			i++;
		}
		vector<int> res;
		bool ishead = true;
		while (!buff.empty()) {
			int item = buff.back();
			buff.pop_back();
			if (item != 0)
				ishead = false;
			if (item > 0 || !ishead)
				res.push_back(item);
		}
		if (res.empty())
			res.push_back(0);
		return res;
	}
};


int main()
{
	Solution s;
	vector<int> v1 = {
		{ 1 }
	};
	vector<int> v2 = {
		 { 1 }
	};
	vector<vector<int>> vv = {
		{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	};

	vector<int> res = s.addNegabinary(v1, v2);

	return 0;
}

