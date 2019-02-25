try:
    case = 0
    while True:
        case += 1
        rule = list(input())
        print(f"Case {case}:")
        nr = int(input())
        for _ in range(nr):
            testcase = list(map(int, input().split()))
            series = rule[min(testcase): max(testcase) + 1]
            if all(series) or not any(series):
                print("Yes")
            else:
                print("No")
except Exception:
    exit()

#
# include <iostream>
#
# using namespace std;
#
# int main() {
#     string rule;
#     int cur_case = 1;
#     while (getline(cin, rule)) {
#         int n, i, j, mn, mx;
#         cin >> n;
#         cout << "Case " << cur_case << ":" << endl;
#         for (int m = 1; m <= n; m++) {
#             cin >> i >> j;
#             int l = 0, o = 0;
#             mn = min(i, j), mx = max(i, j);
#             for (int k = mn; k <= mx; k++) {
#                 if (rule[k] == '0')o++;
#                 else l++;
#             }
#             if (o == 0 || l == 0)cout << "Yes" << endl;
#             else cout << "No" << endl;
#         }
#         cur_case++;
#     }
#     return 0;
# }
#
