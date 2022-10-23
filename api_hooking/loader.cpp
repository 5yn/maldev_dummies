#include <Windows.h>

int main(int argc, char* argv[]){
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, DWORD(atoi(argv[1])));

    WCHAR dllPath[] = L"C:\\PATH\\TO\\YOUR\\DLL.dll";
    PVOID remoteBuffer = VirtualAllocEx(hProcess, NULL, sizeof dllPath, MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(hProcess, remoteBuffer, (LPVOID)dllPath, sizeof dllPath, NULL);

    PTHREAD_START_ROUTINE threatStartRoutineAddress = (PTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle(TEXT("Kernel32")), "LoadLibraryW");
    CreateRemoteThread(hProcess, NULL, 0, threatStartRoutineAddress, remoteBuffer, 0, NULL);

    CloseHandle(hProcess);

    return TRUE;
}
