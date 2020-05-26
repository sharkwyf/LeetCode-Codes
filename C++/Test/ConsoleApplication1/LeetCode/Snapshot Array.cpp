#include "LeetCode.h"


class SnapshotArray {
	vector<vector<int>> values;
	int snapId = 0;

public:
	SnapshotArray(int length) {
		vector<int> v(length, 0);
		values.push_back(v);
	}

	void set(int index, int val) {
		values[snapId][index] = val;
	}

	int snap() {
		vector<int> v = vector<int>(values[snapId]);
		values.push_back(v);
		return snapId++;
	}

	int get(int index, int snap_id) {
		return values[snap_id][index];
	}
};


int main()
{
	//Solution s;
	vector<vector<int>> v1 = { {}
	};
	vector<int> vv1 = {
		4
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

	//auto res = s.maxSumDivThree(vv1);

	SnapshotArray* obj = new SnapshotArray(1);
	obj->set(0, 5);
	int param_1 = obj->snap();
	obj->set(0, 6);
	int param_2 = obj->get(0,0);
	int param_3 = obj->snap();
 

	return 0;
}

