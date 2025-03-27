#include <iostream>
using namespace std;


int recursive_function(int n) {
    if (n == 0) {
        return 0;
    } else {
        return n + recursive_function(n - 1);
    }
}
int recursive_function(){
    int n;
    cout<<"Enter a value of n: ";
    cin>>n;
    
    if(n==0){
        return 0;
    }else{
        return n +recursive_function(n-1);
    }
}

int main() {
    int n;

    cout << "Enter a value for n: ";
    cin >> n;

 
    cout << "Function result using parameter (n = " << n << "): " << harmonic(n) << endl;

   
    cout << "Function result using no parameter: " << harmonic() << endl;

    return 0;
}

