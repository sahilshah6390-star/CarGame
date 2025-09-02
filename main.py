# main.py - Kivy Supercar Massive (placeholder assets)
# NOTE: This is a scaffold with placeholder images/sounds. Replace assets/*.png and *.ogg for higher quality.
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
import os, random, math, json

# Fullscreen on mobile
try:
    Window.fullscreen = True
except Exception:
    Window.size = (420,760)

ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")
STORE_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# Owner
OWNER_NAME = "Sahil"
TG_HANDLE = "@offx.sahil"

# Generate car list dynamically from assets folder
def discover_cars():
    cars = []
    files = sorted([f for f in os.listdir(ASSET_DIR) if f.startswith("car_") and f.endswith(".png")])
    price = 0
    for i,f in enumerate(files):
        price = int(100 * (1.5**(i/10)))  # progressive price curve
        cars.append({"id": i, "name": f"SuperCar {i+1}", "price": price, "file": f})
    return cars

CARS = discover_cars()

# maps
MAPS = [ "map_1.png", "map_2.png", "map_3.png" ]

# Storage
store = JsonStore(STORE_FILE)
def get_save():
    if not store.exists('save'):
        store.put('save', coins=2000, best_score=0, selected_car=0, owned=[0])
    return store.get('save')
def save_data(d):
    store.put('save', coins=d['coins'], best_score=d['best_score'], selected_car=d['selected_car'], owned=d['owned'])

# KV load deferred by App

def load_sound(name):
    path = os.path.join(ASSET_DIR, name)
    if os.path.exists(path):
        return SoundLoader.load(path)
    return None

class MenuScreen(Screen):
    pass

class LobbyScreen(Screen):
    pass

class GarageScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

KV = open(os.path.join(os.path.dirname(__file__), "supercar.kv")).read()

class SupercarApp(App):
    engine = ObjectProperty(None)
    drift = ObjectProperty(None)
    crash = ObjectProperty(None)
    coin = ObjectProperty(None)
    bgm = ObjectProperty(None)

    def build(self):
        Builder.load_string(KV)
        # load sounds (optional)
        self.engine = load_sound("engine_loop.ogg")
        self.drift = load_sound("drift.wav")
        self.crash = load_sound("crash.wav")
        self.coin = load_sound("coin.wav")
        self.bgm = load_sound("bgm.ogg")
        return RootWidget(transition=FadeTransition())

if __name__ == "__main__":
    SupercarApp().run()
