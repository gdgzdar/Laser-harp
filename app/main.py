import threading, time
from app.audio import Player

player = Player("Bass", "/dev/ttyACM0")
thread = threading.Thread(target=player.listen_arduino)
thread.daemon = True
thread.start()

time.sleep(600)