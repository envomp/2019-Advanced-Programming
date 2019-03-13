try:

    while True:
        summa = int(input())
        array = [1] + [0] * summa
        numbers = [1, 5, 10, 25, 50]
        for coin in numbers:
            for i in range(summa + 1 - coin):
                array[i + coin] += array[i]
        print(array[summa])

except EOFError:
    print()
    exit()



'''
    #include<bits/stdc++.h>
    using namespace std;
    int main() {
        int n;
        int coins[] = {1, 5, 10, 25, 50};

        while(scanf("%d",&n)!=EOF){

                int new_arr[n + 1];
                memset( new_arr, 0, (n + 1)*sizeof(int) );
                new_arr[0] = 1;

                for (int coin : coins) {
                    for (int i = 0; i < n + 1 - coin; i++) {
                        new_arr[i + coin] += new_arr[i];
                    }
                }

                cout << new_arr[n] << endl;

        }

        return 0;
    }

'''
