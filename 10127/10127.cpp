#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	long long int cur_input;
	while (cin >> cur_input){
		long long int cur_division = 1;
		int n = 0;
		if (cur_input != 0){
			while (cur_division) {
				n++;
				cur_division = (10 * cur_division + 1) % cur_input;
				cout << cur_division << "  " << 10 * cur_division + 1 << endl;
			}
			n++;
			cout << n << endl;
		} else {
			cout << 0 << endl;
		}
}
return 0;
}
