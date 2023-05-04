#include "Windows.h";
#include "SoftwareDefinitions.h";


int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow){
	WNDCLASS SoftwareMainClass = NewWindowColass((HBRUSH)COLOR_WINDOW, LoadCursor(NULL, IDC_ARROW), hInst, LoadIcon(NULL, IDI_QUESTION), L"MainWndClass", SoftwareMainProcedure);


	if (!RegisterClassW(&SoftwareMainClass)) { return -1; }
	MSG SoftwareMainMessage = { 0 };


	CreateWindow(L"MainWndClass", L"c++ window project", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100, 100, 500, 250, NULL, NULL, NULL, NULL);


	while (GetMessage(&SoftwareMainMessage, NULL, NULL, NULL)) {
		TranslateMessage(&SoftwareMainMessage);
		DispatchMessage(&SoftwareMainMessage);
	}
	return 0;
}


WNDCLASS NewWindowColass(HBRUSH BGColor, HCURSOR Cursor, HINSTANCE hInst, HICON Icon, LPCWSTR Name, WNDPROC Procedure) {
	WNDCLASS NWS = { 0 };


	NWS.hIcon = Icon;
	NWS.hCursor = Cursor;
	NWS.hInstance = hInst;
	NWS.lpszClassName = Name;
	NWS.hbrBackground = BGColor;
	NWS.lpfnWndProc = Procedure;


	return NWS;
}


LRESULT CALLBACK SoftwareMainProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp) {
	switch (msg) {
	case WM_CREATE:
		MainWndAddMenus(hWnd);
		break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default: return DefWindowProc(hWnd, msg, wp, lp);
	}
}



void MainWndAddMenus(HWND hWnd) {
	HMENU RootMenu = CreateMenu();


	AppendMenu(RootMenu, MF_STRING, NULL, L"OUR Menu");


	SetMenu(hWnd, RootMenu);
}
