#include<bits/stdc++.h>
using namespace std;
int n;
int mat[2190][2190];
int ans[3]={0,0,0};i
// 모든 부분이 같은지 확인하는 메소드
bool chk(int n, int x, int y){
    for(int i= x; i < x+n; i++){
        for(int j = y; j < y+n; j++){
            if(mat[i][j] != mat[x][y]) return false;
        }
    }
    return true;
}
// divide and conquer(with recursion)
void func(int n, int x, int y){
    if(chk(n,x,y)){
        ans[mat[x][y]+1]++;
        return ;
    }
    // 이건 9분할이라 /3으로 진행
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++) func(n/3, x+i*n/3, y+j*n/3);
    }
}

int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    //constraints
    // 1<= n <= 3^7, n := 3^k
    cin >> n;
    for(int x = 0; x < n; x++){
        for(int y = 0; y < n; y++) cin >> mat[x][y];
    }
    func(n, 0, 0);
    cout << ans[0] << "\n";
    cout << ans[1] << "\n";
    cout << ans[2] << "\n";
}
