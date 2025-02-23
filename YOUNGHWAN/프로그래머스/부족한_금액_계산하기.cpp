#include <bits/stdc++.h>
using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long totalPrice = (long long)(price + (price * count)) * count / 2;
    answer = totalPrice - money;
    return answer > 0 ? answer : 0;
}