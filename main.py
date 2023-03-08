from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.lang import Builder

class UI(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_pallete = 'Teal'
        Builder.load_file('design.kv')
        return UI()

if __name__ == '__main__':
    MainApp.run()