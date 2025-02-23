#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> a, vector<int> b)
{
    int answer = 1234567890;
    long long sum = 0;
    for (int i = 0; i < a.size(); i++)
    {
        sum += (long long)a[i] * b[i];
    }
    answer = (int)sum;
    return answer;
}