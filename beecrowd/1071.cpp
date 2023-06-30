#include <iostream>
 
using namespace std;
 
int main() {
	int x, y, sum = 0;
	
	cin >> x;
	cin >> y;

	if(x > y){
		int temp = x;
		x = y;
		y = temp;
	}
	for(int i = x+1; i < y; i++){
		if(i % 2 != 0){
			sum += i;
		}
	}

	cout << sum << "\n";
	
  return 0;
}