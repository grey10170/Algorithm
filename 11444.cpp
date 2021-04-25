#include <iostream>
#include <vector>

using namespace std;

long long divider = 1000000007;

long long getFibo(long long idx){
    if(idx == 1) return 1;
    if(idx == 0) return 0;
    long long n= idx/2;
    if(idx % 2==1){
        long long u = getFibo(n), v = getFibo(n+1);
        return (u*u + v*v)%divider;
    }else{
        long long u = getFibo(n), v = getFibo(n-1);
        return (u*u + 2*u*v)%divider;
    }
}

int main()
{
    long long N;
    cin >> N;
    cout << getFibo(N) << endl;

	return 0;
}