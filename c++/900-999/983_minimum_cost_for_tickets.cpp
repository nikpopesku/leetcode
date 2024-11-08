#include <vector>
#include <iostream>
#include<limits>

using namespace std;

class Solution {
public:
    int mincostTickets(vector<int> days, vector<int> costs) {
        int one = costs[0];
        int seven = costs[1];
        int thirty = costs[2];

        if (days.size() >= 1) {
            one += mincostTickets(vector<int>(days.begin() + 1, days.end()), costs);
        }

        if (days.size() >= 7) {
            seven += mincostTickets(vector<int>(days.begin() + 7, days.end()), costs);
        }

        if (days.size() >= 30) {
            thirty += mincostTickets(vector<int>(days.begin() + 30, days.end()), costs);
        }

        return min(min(one, seven), thirty);
    }
};

int main() {
    auto s = Solution();
    cout << s.mincostTickets(vector<int>{1,4,6,7,8,20}, vector<int>{2,7,15}) << endl;
}