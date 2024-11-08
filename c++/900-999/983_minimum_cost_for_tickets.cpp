#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int mincostTickets(vector<int> &days, vector<int> &costs) {
        return calc(days, costs, 0);
    }

    int calc(vector<int> &days, vector<int> &costs, int day) {
        if (days.empty()) return 0;

        vector<int> a{days.begin() + 1, days.end()};
        const int one = costs[0] + calc(a, costs, day + 1);

        const int seven = costs[1] + calc(days, costs, day + 7);
        const int thirty = costs[2] + calc(days, costs, day + 30);

        return min(min(one, seven), thirty);
    }
};

int main() {
    auto s = Solution();
    vector a{1, 4, 6, 7, 8, 20};
    vector b{2, 7, 15};
    cout << s.mincostTickets(a, b) << endl;
}
