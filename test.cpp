#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);  
    int N; cin >> N;
    vector<int> a(N);
    long long tong = 0;
    for (int i=0; i<N; i++)
    {
        cin >> a[i];
        tong += a[i];
    }
    int res = 1 ;
    //uoc
    for (long long i=1; i*i <=tong; i++)
    {
        //doan con co tong la i
        if (tong % i == 0)
        {
            long long tong_temp = 0;
            int cnt = 0;
            for (int j =0; j<N; j++)
            {
                tong_temp += a[j];
                if (tong_temp == i)
                {
                    cnt ++;
                    tong_temp = 0;
                }
            }
            if (tong_temp == 0) res = max(res, cnt);
        }


        //doan con co tong la tong/i
        if (i != tong/i)
        {
            long long tong_temp = 0; 
            int cnt = 0;
            for (int j =0; j<N; j++)
            {
                tong_temp += a[j];
                if (tong_temp == tong/i)
                {
                    cnt ++ ;
                    tong_temp =0;
                }
            }
            if (tong_temp == 0) res = max(res, cnt);
        }
    }
    cout << res;
    
    return 0;
}
12221