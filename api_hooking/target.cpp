#include <Windows.h>
#include <string>

int main() {
	DWORD pid = GetCurrentProcessId();

	WCHAR msg[10] = {0};
	wsprintf(msg, L"%d", pid);

	MessageBox(0, L"Hello, world!", msg, 0);
	MessageBox(0, L"Hello, world!", msg, 0);
}

