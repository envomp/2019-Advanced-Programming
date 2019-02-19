#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	int cur_input;
	while (cin >> cur_input){
		long long cur_division = 1;
		int n = 0;
		long long proxy;
		double intpart;
		if (cur_input != 0){
			while (true){
				n++;
				proxy = cur_division / cur_input;
				if(modf(proxy, &intpart) == 0.0){
					cout << n << endl;
					break;
				} else {
					cur_division += pow(10, n);
				}
			}
		} else {
			cout << 0 << endl;
		}
}
}
