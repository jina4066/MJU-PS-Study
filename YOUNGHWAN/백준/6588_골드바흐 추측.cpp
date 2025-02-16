#include <bits/stdc++.h>
#define MAX 1000000
using namespace std;
int n, l, r;
int arr[MAX + 4] = {
    1,
    1,
    1,
    0,
};
bool check;
int main()
{
    for (int i = 2; i * i < MAX; i++)
    {
        if (arr[i] == 0)
        {
            for (int j = i * i; j < MAX; j += i)
            {
                arr[j] = 1;
            }
        }
    }

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while (1)
    {
        cin >> n;
        vector<int> v;
        if (n == 0)
        {
            break;
        }
        l = 3;
        r = n - 3;
        while (l <= r)
        {
            if (!arr[l] && !arr[r])
            {
                if ((l + r) == n)
                {
                    break;
                }
            }
            l += 2;
            r -= 2;
        }
        if (l > r)
            cout << "Goldbach's conjecture is wrong.";
        else
            cout << n << " = " << l << " + " << r << '\n';
    }
}
// 소수 찾는 알고리즘은 에라토스테네스의 체를 사용했다.
// 두 소수를 찾을 때까지 반복한다.
// 자세한건 PR에 적어둔다.