#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    try {
        string jeebus;
        string temp;
        while (cin >> jeebus) {
            if(jeebus == "#") break;
            temp = jeebus;
            bool isGay = false;
            bool isSuperGay = false;

            do {
                if(isGay){
                    isSuperGay = true;
                    cout << temp << endl;
                    break;
                }

                if(jeebus == temp) {
                    isGay = true;
                }

            } while (next_permutation(temp.begin(),temp.end()));
            if (!isSuperGay) cout << "No Successor" << endl;
        }
    } catch (const exception& e) {
        cout << endl;
    }
}