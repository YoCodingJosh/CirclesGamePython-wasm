#include <Windows.h>
#include <string.h>

int main(int argc, char* argv[])
{
	if (strcmp(argv[1], "SHOW") == 0)
	{
		ShowWindow(GetConsoleWindow(), SW_SHOW);
	}
	else if (strcmp(argv[1], "HIDE") == 0)
	{
		ShowWindow(GetConsoleWindow(), SW_HIDE);
	}

	return 0;
}