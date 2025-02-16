#include <bits/stdc++.h>

using namespace std;
long long cnt = 0;
long long solution(int r1, int r2)
{
    for (int x = 1; x <= r1; x++)
    {
        long long y_max = floor(sqrt(pow(r2, 2) - pow(x, 2)));
        long long y_min = ceil(sqrt(pow(r1, 2) - pow(x, 2)));

        cnt += (y_max - y_min + 1);
    }

    for (int x = r1 + 1; x <= r2; x++)
    {
        long long y_max = floor(sqrt(pow(r2, 2) - pow(x, 2)));
        cnt += (y_max + 1);
    }
    long long answer = cnt * 4;
    return answer;
}