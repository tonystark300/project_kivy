import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder



class Main_Screen(Screen):
    pass

class Second_Screen(Screen):
    pass

class Third_Screen(Screen):
    pass

class Screen_Manager(ScreenManager):
    pass

class Loading(Screen):
    pass


kv = Builder.load_file('kivy.kv')

class App(App):
    def build(self):
          return kv

if __name__ == '__main__':
    App().run()

