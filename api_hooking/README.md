# Basic API Hooking

API hooking is a technique that allows you to modify the behaviour of Windows API calls. You can use these to enable more fine-tuned control over how your payloads interact with the API, or use it offensively to hook the API calls in a remote process to steal data or hide your tooling from defenders.

Check out the function prototype for the API call that you want to hijack: 
![image](https://user-images.githubusercontent.com/25803146/197367788-f59f3c47-3f20-468c-b377-7116c4c7fb73.png)

Create a pointer to the original function address:
![image](https://user-images.githubusercontent.com/25803146/197367925-b11c4ff5-feb2-428c-a1c1-b32fd23dbe65.png)

Recreate this API call within your code, and implement whatever modifications you want. In this case, we'll just be making all calls to MessageBox result in a "Hooked!" message to appear instead. In more complex examples, this can be used to hide your malicious payload or network connections from monitoring tools:
![image](https://user-images.githubusercontent.com/25803146/197367995-f7a26da7-6b3e-4395-b786-24f0b24bd421.png)

Use Detours to perform the hook:
![image](https://user-images.githubusercontent.com/25803146/197367986-7939fa87-155f-4e22-8d6d-eb2e167739d4.png)

# Examples

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





