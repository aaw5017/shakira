import threading
import time
import pyautogui

class MouseMover(threading.Thread):
    def __init__(self):
        self._stop_event = threading.Event()
        self._sleep_interval = 2.5
        self._move_interval = .250
        self._is_moving = False
        self._is_active = False

        super().__init__(name='MouseMoverThread')

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def run(self):
        while not self._stop_event.isSet():
            if not self._is_active or self._is_moving:
                continue

            self._is_moving = True
            pyautogui.moveRel(None, 10)
            time.sleep(self._move_interval)
            pyautogui.moveRel(-10, None)
            time.sleep(self._move_interval)
            pyautogui.moveRel(None, -10)
            time.sleep(self._move_interval)
            pyautogui.moveRel(10, None)
            self._is_moving = False

            time.sleep(self._sleep_interval)

    def join(self, timeout=None):
        self._stop_event.set()
        threading.Thread.join(self, timeout)