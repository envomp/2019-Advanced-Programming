#include <iostream>
using namespace std;

int main() {
	char c;
	// substract 7 to get the right char
	string answer;

	while(scanf("%c", &c) != EOF){
		if (c == '\n'){
			answer += c;
		} else {
			answer += char(int(c) - 7);	
		}
	}
	cout << answer;
	return 0;
}
