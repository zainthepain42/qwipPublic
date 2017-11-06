##Zain Hussain A-Level Computer Science Programming Project
##Smart Shopping Assistant app + protype for mobile self-checkout

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

class qwipRoot(BoxLayout):
    
    def __init(self, **kwargs):
        super(qwipRoot, self).__init__(**kwargs)

    def changeScreen(self, next_screen):

        if next_screen == "start the tour":
            self.ids.kivy_screen_manager.current = "tour_screen"
        
        


class qwipApp(App):

    def __init__(self, **kwargs):
        super(qwipApp, self).__init__(**kwargs)
        
    def build(self):
        return qwipRoot() ##return instance, which is basically a box layout

if __name__ == "__main__":
    qwipApp().run()
    
#This is the base of any Kivy application
