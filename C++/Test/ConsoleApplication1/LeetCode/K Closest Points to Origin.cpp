#include "LeetCode.h"


class Solution {
public:
	vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
		int len = points.size();
		vector<int> distances(len);
		for (int i = 0; i < len; i++) {
			distances[i] = pow(points[i][0], 2) + pow(points[i][1], 2);
		}
		auto tree = buildHeap(distances, K);
		for (int i = K; i < len; i++) {
			insertHeap(distances, tree, i, K);
		}
		vector<vector<int>> res;
		for (int i : tree) {
			res.push_back(points[i]);
		}
		return res;
	}

	vector<int> buildHeap(vector<int> &distances, int K) {
		vector<int> tree(K, -1);
		int len = 0;
		for (int i = 0; i < K; i++) {
			tree[i] = i;
			int j = i;
			while (j > 0) {
				int parentj = (j + 1) / 2 - 1;
				if (distances[tree[parentj]] < distances[i]) {
					swap(tree[parentj], tree[j]);
					j = parentj;
				}
				else {
					break;
				}
			}
		}
		return tree;
	}

	void insertHeap(vector<int> &distances, vector<int> &tree, int v, int k) {
		int i = 0;
		while (distances[v] < distances[tree[i]]) {
			int l = i * 2 + 1, r = i * 2 + 2;
			int m = v;
			if (l < k && distances[v] < distances[tree[l]])
				m = l;
			if (r < k && distances[v] < distances[tree[r]])
				m = r;
			if (m == v) {
				tree[i] = v;
				return;
			}
			else {
				tree[i] = tree[m];
				i = m;
			}
		}
	}
};


int main()
{
	Solution s;
	vector<vector<int>> v1 =
		{{-2, 10}, {-4, -8}, {10, 7}, {-4, -7}}
	;
	vector<string> vv1 = {
		"gin", "zen", "gig", "msg"
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


	auto res = s.kClosest(v1, 3);

	return 0;
}

