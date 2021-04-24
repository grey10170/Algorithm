#include <iostream>
#include <vector>
#include <time.h>
using namespace std;

int getMaxRectangle(const vector<int>& fence_arr, int left, int right){
    if(right==left){
        return fence_arr[left];
    }
    int center = (left+right)/2;
    int result =max(getMaxRectangle(fence_arr,left, center), getMaxRectangle(fence_arr,center+1, right));
    int height = min(fence_arr[center-1], fence_arr[center]);
    int l= center-1, r = center;
    while(left <l || right >r){
        if(r <right &&(l==left || fence_arr[l-1] < fence_arr[r+1])){
            ++r;
            height = min(height, fence_arr[r]);
        }else{
            --l;
            height = min(height, fence_arr[l]);
        }
        result = max(result, height*(r-l+1));
    }
    return result;
}

int main()
{
    time_t start = time(NULL);
    vector<int> fence_arr;
	int n_case;
	
	cin >> n_case;

    for(int i=0; i< n_case; i++)
	{
	    int arr_len;
        cin >> arr_len;

        for(int j = 0; j< arr_len; j++){
            int input_;
            cin >> input_;
            fence_arr.push_back(input_);
        }
        cout << getMaxRectangle(fence_arr,0, arr_len-1) <<"\n";
        fence_arr.clear();
	}
	return 0;
}