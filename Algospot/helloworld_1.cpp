#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	
	cin>>n;

	if(n < 1 || n > 50)
		return 0;

	while(n--)
	{
		string name;
		cin>>name;

		cout << "Hello, " << name << "!" << endl;

	}

	return 0;
}