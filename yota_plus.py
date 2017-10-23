'''reduce yota speed = maximise use'''
import pyautogui

pyautogui.click(48, 1057)
print 'clicked on search'

pyautogui.typewrite('  chrome', interval=0.25)
print 'typed  chrome'

pyautogui.press('enter')
print 'pressed enter'

pyautogui.moveTo(215, 43, duration=10.0)
pyautogui.click(215, 43)
print 'clicked on address bar'

pyautogui.typewrite('my.yota.ru')
print 'typed my.yota.ru'

pyautogui.press('enter')
print 'pressed enter'

pyautogui.moveTo(215, 1057, duration=10.0)
print 'delayed 10s'
x, y = pyautogui.locateCenterOnScreen('parol.png')
pyautogui.click(x, y)
print 'found and clicked on parol'

pyautogui.typewrite('*******', interval=0.25)
print 'typed parol'

pyautogui.press('enter')
print 'pressed enter'

pyautogui.moveTo(215, 1057, duration=10.0)
print 'delayed 10s'
x, y = pyautogui.locateCenterOnScreen('plus.png')
pyautogui.click(x, y, clicks=12, interval=0.25)
print 'found and clicked on minus button 12 times'

x, y = pyautogui.locateCenterOnScreen('ok.png')
pyautogui.click(x, y)
print 'clicked on ok'
