/*
 * main.cpp
 * Created by Josh Kennedy on 2 August 2014
 *
 * Circles Game Python
 *
 * Description: Handles the Python process that runs the game,
 *	prevents running multiple instances, and hides the console
 *	that Python creates and the one this program creates. It's
 *	pretty darn cool!
 *
 * Note: This code only works on Windows, so it won't even
 *	begin to compile on other OS's! :P
 */

// Windows API
#include <Windows.h>

// C++ Standard Library
#include <string>
#include <fstream>

// C Standard Library
#include <stdarg.h>
#include <stdio.h>
#include <signal.h>

// Backup mutex descriptor
// Global\\CirclesGame{2017cafa-78ab-4040-99e5-b3bd20b14729}

// Global variables.
bool debug = false;
SHELLEXECUTEINFOA executionInfo = { 0 };

// Attempts to make a mutex, if it can't make a mutex then the process is already running.
// Returns true if it can't make a mutex, false if it can.
bool IsInstanceRunningAlready()
{
	// For handling Single Instance of Application
	HANDLE hSingleInstance = NULL;
	hSingleInstance = CreateMutex(NULL, FALSE, TEXT("Global\\CirclesGame{e60c6fad-4ec4-4807-9d7e-df7cafeaf4cd}"));
	DWORD dwLastError = GetLastError();

	if (dwLastError == ERROR_ALREADY_EXISTS)
	{
		CloseHandle(hSingleInstance);
		return true;
	}

	return false;
}

// Gets the current executable path (without the file).
std::string getExePath()
{
	char buffer[MAX_PATH];
	GetModuleFileNameA(NULL, buffer, MAX_PATH);
	std::string::size_type pos = std::string(buffer).find_last_of("\\/");
	return std::string(buffer).substr(0, pos);
}

// Gets the current working directory.
std::string getCurrentPath()
{
	char path[MAX_PATH];
	GetCurrentDirectoryA(MAX_PATH, path);

	return path;
}

// Sorta like printf...
// ...except it prints to the debugger if the game is running without the debug argument.
void debugf(const char* format, ...)
{
	char buffer[512];
	va_list args;

	va_start(args, format);

	vsnprintf_s(buffer, 512, format, args);

	if (debug)
		vprintf_s(buffer, args);
	else
		OutputDebugStringA(buffer);

	va_end(args);
}

// Shutdown logic.
// Which is showing the console window, uninitializing COM, killing Python (if necessary).
void exitLogic()
{
	debugf("\nShutting down...");
	ShowWindow(GetConsoleWindow(), SW_SHOW);
	CoUninitialize();
	if (executionInfo.hInstApp != NULL)
	{
		DWORD pid = GetProcessId(executionInfo.hProcess);
		debugf("\n\tKilling Python process with PID %u...", pid);
		TerminateProcess(executionInfo.hProcess, 0);
		executionInfo.hInstApp = NULL;
	}
	debugf("\n");
}

// The callback that handles the signals that Windows detects.
BOOL WINAPI processSignal(DWORD event)
{
	switch (event)
	{
	case CTRL_C_EVENT:
		debugf("\nReceived Ctrl+C signal!\n");
		exitLogic();
		break;
	case CTRL_BREAK_EVENT:
		debugf("\nReceived Ctrl+Break signal!\n");
		exitLogic();
		break;
	case CTRL_CLOSE_EVENT:
		debugf("\nReceived program close signal!\n");
		exitLogic();
		break;
	case CTRL_LOGOFF_EVENT:
		debugf("\nReceived user log off signal!\n");
		exitLogic();
		break;
	case CTRL_SHUTDOWN_EVENT:
		debugf("\nReceived user shutdown signal!\n");
		exitLogic();
		break;
	}

	return TRUE;
}

// The entry point to the program.
int main(int argc, char* argv[])
{
	// See if we have a debug parameter.
	if (argc > 1)
	{
		if (strcmp(argv[1], "-debug") == 0)
		{
			// We do! So we set the global debug variable.
			debug = true;
		}
	}

	debugf("Starting up...\n");

	// Install the control handler for the console.
	if (SetConsoleCtrlHandler((PHANDLER_ROUTINE)processSignal, TRUE) == FALSE)
	{
		debugf("Unable to install signal handler!\n");
		return 1;
	}

	// Initialize COM and set up exit logic callback.
	debugf("Setting up COM...");
	CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
	atexit(exitLogic);
	debugf("\n");

	// Are we already running?
	if (IsInstanceRunningAlready())
	{
		debugf("Detected existing instance of game... WHOA!!\n");

		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_HIDE);

		MessageBoxEx(GetConsoleWindow(), TEXT("Another instance is running.\n\nPlease close it and try again."), TEXT("CirclesGame"),
			MB_OK | MB_ICONHAND, MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL));

		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_SHOW);

		return -1;
	}

	// Set up the paths to Python and our game.
	debugf("Setting up the path...");
	std::string pythonDirectory = getExePath();
	pythonDirectory += "/Python/python.exe";

	// Check to see if the program installed correctly by checking if Python is where we think it is.
	std::ifstream pythonExe = std::ifstream(pythonDirectory);

	if (!pythonExe)
	{
		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_HIDE);

		debugf("\n\nPython couldn't be found at:\n%s", pythonDirectory.c_str());

		MessageBoxEx(GetConsoleWindow(), TEXT("Python couldn't be found!\n\nPlease re-install the game."), TEXT("CirclesGame"),
			MB_OK | MB_ICONHAND, MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL));

		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_SHOW);

		return -2;
	}

	std::string workingDirectory = getExePath();
	workingDirectory += "/Game/";

	std::string parameters = "\"../Game/PythonCirclesGame.pyc\"";

	// The same logic here, check to see if our main program in Python exists.
	std::string pythonCodeFile = getExePath();
	pythonCodeFile += "./Game/PythonCirclesGame.pyc";
	std::ifstream pythonCode = std::ifstream(pythonCodeFile);

	if (!pythonCode)
	{
		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_HIDE);

		debugf("\n\nEntry point code file couldn't be found at:\n%s", pythonCodeFile.c_str());

		MessageBoxEx(GetConsoleWindow(), TEXT("The Game files are incomplete!!\n\nPlease re-install the game."), TEXT("CirclesGame"),
			MB_OK | MB_ICONHAND, MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL));

		if (!debug)
			ShowWindow(GetConsoleWindow(), SW_SHOW);

		return -2;
	}

	// Set up the execution info data structure.
	debugf("\nSetting up the execution data structure...");

	executionInfo.hwnd = NULL;
	executionInfo.cbSize = sizeof(SHELLEXECUTEINFOA);
	executionInfo.lpFile = pythonDirectory.c_str();
	executionInfo.lpVerb = "open";
	executionInfo.nShow = (debug ? SW_SHOW : SW_HIDE);
	executionInfo.lpParameters = parameters.c_str();
	executionInfo.lpDirectory = workingDirectory.c_str();
	executionInfo.hInstApp = NULL;
	executionInfo.fMask = SEE_MASK_NOCLOSEPROCESS;

	// Execute Python.
	debugf("\n\nExecuting Python...");

	ShellExecuteExA(&executionInfo);
	
	if (!debug)
		ShowWindow(GetConsoleWindow(), SW_HIDE);

	// Wait for the user to exit the game.
	debugf("\n\nWaiting for user...");
	WaitForSingleObject(executionInfo.hProcess, INFINITE);

	if (!debug)
		ShowWindow(GetConsoleWindow(), SW_SHOW);

	debugf("\n");

	return 0;
}
