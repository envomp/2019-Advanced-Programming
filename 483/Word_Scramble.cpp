// Original python code...
//
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
	char l = 'a';
	string answer;
	string printer;

	while(scanf("%c", &c) != EOF){
		
		if (c == ' ' || c == '\n'){
			answer += c;
			printer += answer;
			answer = "";
			if(l == '\n' && c == ' '){
			answer = " ";		
			}
		} else {
			answer = c + answer;
		}		
	}
	l = c;
	cout<<printer<<endl;

	return 0;
}
