#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int number_of_testcases, n, k, i;
    char a[20];
    cin >> number_of_testcases;
    while (number_of_testcases--) {
        cin >> n >> k;
        for (i = 0; i < n - k; i++) a[i] = '0';
        for (i = n - k; i < n; i++) a[i] = '1';
        a[n] = '\0';
        do {
            puts(a);
        } while (next_permutation(a, a + n));
        if (number_of_testcases) cout << endl;
    }
}
