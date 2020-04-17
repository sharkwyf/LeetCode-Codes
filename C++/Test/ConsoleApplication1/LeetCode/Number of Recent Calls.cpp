#include "LeetCode.h"


class MyListNode {
public:
	MyListNode(int x = -1) {
		val = x;
	}
	int val;
	MyListNode* next;
};


class RecentCounter {
public:
	MyListNode* Head;
	int cnt;

	RecentCounter() {
		Head = new MyListNode();
		cnt = 0;
	}
	
	int ping(int t) {
		MyListNode* node = new MyListNode(t);
		if (cnt == 0) {
			node->next = node;
			Head->next = node;
			cnt++;
			return cnt;
		}
		else {
			MyListNode* last = Head->next;
			MyListNode* first = Head->next->next;
			node->next = first;
			last->next = node;
			Head->next = node;
			cnt++;
			while (first->val < t - 3000) {
				MyListNode* tmp = first;
				first = first->next;
				if (tmp != Head)
					delete(tmp);
				cnt--;
			}
			Head->next->next = first;
			return cnt;
		}
	}
};



int main()
{

	//Solution s;
	//vector<vector<int>> v = {
	//	{1, 2, 3}, {4, 5, 6}, {7, 8, 9} 
	//};
	//int res = s.isUgly(8);


	RecentCounter* obj = new RecentCounter();
	int param_1 = obj->ping(642);
	int param_2 = obj->ping(1849);
	int param_3 = obj->ping(4921);
	int param_4 = obj->ping(5936);
	int param_5 = obj->ping(5957);
	return 0;
}

