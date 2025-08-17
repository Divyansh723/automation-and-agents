import time
from pynput import keyboard, mouse
import threading

class BehaviorTracker:
    def __init__(self, duration=600):
        self.duration = duration
        self.keystrokes = 0
        self.backspaces = 0
        self.key_intervals = []
        self.last_key_time = None
        self.mouse_moves = 0
        self.start_time = time.time()
        self.running = True

    def on_key_press(self, key):
        now = time.time()
        self.keystrokes += 1
        if self.last_key_time:
            self.key_intervals.append(now - self.last_key_time)
        self.last_key_time = now
        if key == keyboard.Key.backspace:
            self.backspaces += 1

    def on_mouse_move(self, x, y):
        self.mouse_moves += 1

    def start_tracking(self):
        with keyboard.Listener(on_press=self.on_key_press) as kl, mouse.Listener(on_move=self.on_mouse_move) as ml:
            while self.running and (time.time() - self.start_time) < self.duration:
                time.sleep(0.1)
            self.running = False

    def get_summary(self):
        avg_key_interval = sum(self.key_intervals) / len(self.key_intervals) if self.key_intervals else 0
        return {
            'keystrokes': self.keystrokes,
            'backspaces': self.backspaces,
            'avg_key_interval_sec': avg_key_interval,
            'mouse_moves': self.mouse_moves,
            'tracking_duration_sec': time.time() - self.start_time
        }

if __name__ == "__main__":
    tracker = BehaviorTracker(duration=600)  
    tracking_thread = threading.Thread(target=tracker.start_tracking)
    tracking_thread.start()

    print("Tracking user behavior silently for 10 minutes...")

    tracking_thread.join()

    summary = tracker.get_summary()
    print("Tracking summary:", summary)
