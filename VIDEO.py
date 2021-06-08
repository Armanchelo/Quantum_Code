import cv2
import numpy as np
import pyautogui
from tkinter.filedialog import asksaveasfilename
from keyboard import is_pressed as key
from tqdm import tqdm
from time import sleep

SCREEN_SIZE = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("c:/users/usuario/desktop/output.avi", fourcc, 20.0, (SCREEN_SIZE))
frames = []
start = True
for x in reversed(range(5)):
    print(x)
    sleep(1)
while True:
    if start:
        print('Recording...')
        start = False
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if key('q'): break

cv2.destroyAllWindows()
out.release()