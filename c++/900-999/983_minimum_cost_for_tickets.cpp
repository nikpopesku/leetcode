#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int mincostTickets(const vector<int>& days, const vector<int>& costs) {
        if (days.empty()) return 0;

        vector a(days.begin() + 1, days.end());
        int one = costs[0] + mincostTickets(a, costs);
        int seven = costs[1];
        int thirty = costs[2];


        vector<int> b {};

        for (vector<int>::size_type i = 0; i < days.size(); i++) {
            if (days[i] < days[0] + 7) {
                continue;
            }

            b.push_back(days[i]);
        }

        if (!b.empty()) {
            seven += mincostTickets(b, costs);
        }


        vector<int> c {};

        for (vector<int>::size_type i = 0; i < days.size(); i++) {
            if (days[i] < days[0] + 30) {
                continue;
            }

            c.push_back(days[i]);
        }

        if (!c.empty()) {
            thirty += mincostTickets(c, costs);
        }

        return min(min(one, seven), thirty);
    }
};

int main() {
    auto s = Solution();
    cout << s.mincostTickets(vector<int> {1,2,3,4,5,6,7,8,9,10,30,31}, {2,7,15}) << endl;
}