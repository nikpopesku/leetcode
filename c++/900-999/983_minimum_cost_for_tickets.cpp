#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        if (days.empty()) return 0;

        vector a(days.begin() + 1, days.end());
        int one = costs[0] + mincostTickets(a, costs);
        int seven = costs[1];
        int thirty = costs[2];


        vector<int> b {};

        for (vector<int>::iterator i = 0; i < days.size(); i++) {
            if (days[i] < days.begin() + 7) {
                continue;
            }

            b.push_back(days[i]);
        }
        if (days.size() >= 7) {
            vector b(days.begin() + 7, days.end());
            seven += mincostTickets(b, costs);
        }

        if (days.size() >= 30) {
            vector c(days.begin() + 30, days.end());
            thirty += mincostTickets(c, costs);
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