#include "LeetCode.h"


 
class Solution {
public:
	vector<int> partitionLabels(string S) {
		vector<int> res;
		int len = S.length();
		int pos[26];
		for (int i = 0; i < len; i++) {
			pos[S[i] - 'a'] = i;
		}
		int last = -1, lastpos = -1;
		for (int i = 0; i < len; i++) {
			char c = S[i];
			last = max(last, pos[c - 'a']);
			if (i == last) {
				res.push_back(i - lastpos);
				lastpos = i;
			}
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3}}
	;
	vector<int> vv = {
		{3,2,5,4,6,1,7,0}
	};
	
	vector<int> res = s.partitionLabels("ababcbacadefegdehijhklij");

	return 0;
}

