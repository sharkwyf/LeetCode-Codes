#include "LeetCode.h"


class Solution {
public:
	vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
		int height = matrix.size();
		if (!height) return {};
		int width = matrix[0].size();
		if (!width) return {};
		vector<vector<short>> status;
		vector<pair<int, int>> st;
		vector<vector<int>> res;
		int offset[4][2] = {
			{0, 1}, {1, 0}, {0, -1}, {-1, 0}
		};
		status.push_back(vector<short>(width, 1));
		for (int i = 1; i < height; i++) {
			vector<short> row(width, 0);
			row[0] = 1;
			status.push_back(row);
			st.push_back(pair<int, int>(i, 0));
		}
		for (int i = 0; i < width; i++) 
			st.push_back(pair<int, int>(0, i));
		while (!st.empty()) {
			auto item = st.back();
			st.pop_back();
			int val = matrix[item.first][item.second];
			for (auto off : offset) {
				int x = item.first + off[0], y = item.second + off[1];
				if (0 <= x && x < height && 0 <= y && y < width && status[x][y] == 0 && matrix[x][y] >= val) {
					status[x][y] = 1;
					st.push_back(pair<int, int>(x, y));
				}
			}
		}
		for (int i = 0; i < width; i++) {
			status[height - 1][i] += 2;
			st.push_back(pair<int, int>(height - 1, i));
		}
		for (int i = 0; i < height - 1; i++) {
			status[i][width - 1] += 2;
			st.push_back(pair<int, int>(i, width - 1));
		}
		while (!st.empty()) {
			auto item = st.back();
			st.pop_back();
			int val = matrix[item.first][item.second];
			for (auto off : offset) {
				int x = item.first + off[0], y = item.second + off[1];
				if (0 <= x && x < height && 0 <= y && y < width && status[x][y] < 2 && matrix[x][y] >= val) {
					status[x][y] += 2;
					st.push_back(pair<int, int>(x, y));
				}
			}
		}
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				if (status[i][j] == 3)
					res.push_back({ i, j });
			}
		}
		return res;
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 = { 
		{1}
	};
	vector<int> vv1 = {
		3,5,7
	};
	vector<int> vv2 = {
		{ 9,3,15,20,7}
	};

#pragma region ListNode Inputs
	//int size = vv1.size();
	//vector<ListNode*> nodes(size);
	//for (int i = size - 1; i >= 0; i--) {
	//	nodes{i] = new ListNode(vv1[i]);
	//	if (i < size - 1)
	//		nodes[i]->next = nodes[i + 1];
	//}
#pragma endregion

	auto res = s.pacificAtlantic(v1);
	return 0;
}

