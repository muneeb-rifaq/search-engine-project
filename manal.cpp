#include<iostream>
using namespace std;

int main()
{

int value;
cout << "Please enter a positiven number(eg 6)" << endl;
cin >> value;

for(int i = value; i > 0; --i)
{
 for(int j = value ; j > 0; --j)
 {
    cout << j << " ";
 }  
 cout << endl; 
}
}