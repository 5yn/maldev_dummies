# Basic API Hooking

API hooking is a technique that allows you to modify the behaviour of Windows API calls. You can use these to enable more fine-tuned control over how your payloads interact with the API, or use it offensively to hook the API calls in a remote process to steal data or hide your tooling from defenders.

This folder contains the following code samples:
- hook.cpp | Uses the Windows Detours library to hook the MessageBox API call and modify its behaviour.
- target.cpp | Basic program that'll pop the same message box twice. 
- loader.cpp | Basic loader to inject your hook DLL into the remote process.

Compile target.cpp and loader.cpp as EXEs, and hook.cpp as a DLL. 

Detours can be easily installed within Visual Studio.

Right click your project and select "Manage NuGet Packages...":
![image](https://user-images.githubusercontent.com/25803146/197367420-6a380000-b45f-414a-8b96-2801031a0d38.png)

Select "Browse" and type "detours":
![image](https://user-images.githubusercontent.com/25803146/197367424-c5b373a5-20db-4ab0-8f67-9dc2878453f2.png)

Click on the Install button on the right side, and follow the prompt to install:
![image](https://user-images.githubusercontent.com/25803146/197367458-b85949c8-8b1b-47a2-9425-1cf34acb67a5.png)

You can now include it in your code with:
> #include <Detours.h>

When you run target.exe, take note of the number at the top of the message box; this is the process ID.

![image](https://user-images.githubusercontent.com/25803146/197367534-14d78a0e-13bc-4d63-8f56-261406a6e324.png)

Run loader.exe and specify the above PID as an argument. Another messagebox will pop to confirm that the DLL has been loaded:

![image](https://user-images.githubusercontent.com/25803146/197367563-c40dd7c5-65b8-4d0a-9c72-303fbaa5da19.png)

Click through both message boxes (make sure to click the confirmation one first, as execution is paused while the messagebox is open), and see that the next messagebox, despite the code being exactly the same as the first, has been modified with your new message:

![image](https://user-images.githubusercontent.com/25803146/197367609-08b126f1-3461-41a7-889f-42fd7a5753ad.png)
