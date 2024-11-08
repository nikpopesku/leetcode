#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        return calc(days, costs, 0);
    }

    int calc(vector<int>& days, vector<int>& costs, int day) {
        if (days.empty()) return 0;

        int one = costs[0] + calc(days, costs, day + 1);
        int seven = costs[1];
        int thirty = costs[2];


        if (days.size() >= 7) {
            seven += calc(days, costs, day + 7);
        }

        if (days.size() >= 30) {
            thirty += calc(days, costs, day + 30);
        }

        return min(min(one, seven), thirty);
    }
};

int main() {
    auto s = Solution();
    vector a {1,4,6,7,8,20};
    vector b {2,7,15};
    cout << s.mincostTickets(a, b) << endl;
}