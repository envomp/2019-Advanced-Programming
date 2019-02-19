// Original python code..
//
// I am ashamed to turn something so elegant to this monstrosity..
//
// Reading input was helped by timo loomets
// 
// import itertools
// 
// a = """1 2 3 4 5 6 7 8 9
// 5 10 5 20 10 5 10 20 10"""
//
//
// lines = a.split("\n")
// for line in lines:
//     sisend = line.split(" ")
//     dict = {
//         "B": (sisend[0], sisend[3], sisend[6]),
//         "G": (sisend[1], sisend[4], sisend[7]),
//
//         "C": (sisend[2], sisend[5], sisend[8])
//     }
// 
//     results = []
// 
//     for element in list(itertools.permutations(["B", "G", "C"])):
//         combination = "".join(element)
//         result = 0
//         for i, char in enumerate(element):
//            for j, place in enumerate(dict[char]):
//                 if j != i:
//                     result += int(place)
//         results.append([combination, result])
//     print(" ".join(map(lambda x: str(x), sorted(sorted(results, key=lambda x: x[0]), key=lambda x: x[1])[0])))


#include <cstdio>
#include <climits>
#include <cstring>
using namespace std;

int main() {
	int B[3], G[3], C[3];

	while (scanf("%d %d %d %d %d %d %d %d %d", &B[0], &G[0], &C[0], &B[1],
			&G[1], &C[1], &B[2], &G[2], &C[2]) != EOF) {
		int min = INT_MAX, temp;
		char ans[4];
		//BCG
		temp = C[0] + G[0] + B[1] + G[1] + B[2] + C[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "BCG");
		}
		//BGC
		temp = C[0] + G[0] + B[1] + C[1] + B[2] + G[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "BGC");
		}
		//CBG
		temp = B[0] + G[0] + C[1] + G[1] + B[2] + C[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "CBG");
		}
		//CGB
		temp = B[0] + G[0] + B[1] + C[1] + G[2] + C[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "CGB");
		}
		//GBC
		temp = C[0] + B[0] + C[1] + G[1] + B[2] + G[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "GBC");
		}
		//GCB
		temp = C[0] + B[0] + B[1] + G[1] + G[2] + C[2];
		if (temp < min) {
			min = temp;
			strcpy(ans, "GCB");
		}

		printf("%s %d\n",ans,min);
	}

	return 0;
}