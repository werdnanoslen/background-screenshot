import win32gui as wg  
import win32ui as wu  
import win32con

windowName = 'Calculator'
fileName = 'calculator.png'

hwnd = wg.FindWindow(None, windowName)
left, top, right, bot = wg.GetClientRect(hwnd)
x = right - left
y = bot - top
hsrccDc = wg.GetDC(hwnd)
hdestcDc = wg.CreateCompatibleDC(hsrccDc)
hdestcBm = wg.CreateCompatibleBitmap(hsrccDc, x, y)
wg.SelectObject(hdestcDc, hdestcBm.handle)
wg.BitBlt(hdestcDc, 0, 0, x, y, hsrccDc, 0, 0, win32con.SRCCOPY)
destcDc = wu.CreateDCFromHandle(hdestcDc)
bmp = wu.CreateBitmapFromHandle(hdestcBm.handle)
bmp.SaveBitmapFile(destcDc, fileName)
