#include <iostream>
using namespace std;


int main() {
	// 변수 선언 및 입력
	int n;
	cin >> n;

	// n * n 크기의 별을 출력합니다.
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++)
			cout << "*";
		cout << endl;
	}
	
	return 0;
}
