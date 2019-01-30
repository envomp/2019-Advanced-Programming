// Original python code...
// Removed redundent cout << endl;
// from sys import stdin
//
// sisend = """I love you.
// You love me.
// We're a happy family."""
//
// line = input().split("\n")
// 
// print("\n".join([str("".join((reversed(x)))) for x in line]))


#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	char c;
	string answer;

	while(scanf("%c", &c) != EOF){
		
		if (c == ' ' || c == '\n'){
			cout<<answer<<c;
			answer = "";
			
		} else {
			answer = c + answer;
		}		
	}
	return 0;
}