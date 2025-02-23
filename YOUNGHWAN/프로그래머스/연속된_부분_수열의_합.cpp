#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> sequence, int k)
{
    int sPoint = 0;
    int ePoint = 0;
    int currentSum = 0;
    vector<int> answer = {-1, -1};
    int minLength = INT_MAX;

    while (ePoint < sequence.size())
    {
        currentSum += sequence[ePoint];

        while (currentSum > k && sPoint <= ePoint)
        {
            currentSum -= sequence[sPoint];
            sPoint++;
        }

        if (currentSum == k)
        {
            if (ePoint - sPoint < minLength)
            {
                minLength = ePoint - sPoint;
                answer = {sPoint, ePoint};
            }
        }

        ePoint++;
    }

    return answer;
}