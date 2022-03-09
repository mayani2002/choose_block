#include <iostream>
#include<vector>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<int> arr(n),freq(m+1,0);
        int ans=0,color_count=0;
        for(int i=0;i<n;i++)
            cin>>arr[i];
        int i=0,j=0;
        while(i<n)
        {
            freq[arr[i]]++;
            if(freq[arr[i]]==1)
            {
                color_count++;
            }
            if(color_count==m)
            {
                ans=max(ans,i-j);
                while(color_count==m)
                {
                    freq[arr[j]]--;
                    if(freq[arr[j]]==0)
                        color_count--;
                    j++;
                }
            }
            i++;
        }
        cout<<max(ans,i-j)<<endl;
    }
}