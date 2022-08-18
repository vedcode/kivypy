from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager












Main ="""
MDScreen:
    name: "Main"
    MDBottomNavigation:
        pannel_colour: '0,1,0,1'
        MDBottomNavigationItem:
            name: 'screen 1'
            text: "Home"
            icon: 'earth'
            MDFloatLayout:
                MDBoxLayout:
                    MDFloatingActionButtonSpeedDial:
                        data: app.data
                        hint_animation: True
                        bg_hint_color: app.theme_cls.primary_light

        MDBottomNavigationItem:
            name: 'screen 2'
            text: "Java"
            icon: 'android'
            MDLabel:
                text: "world"
                halign : 'center'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: "Swift"
            icon: 'apple'
            MDLabel:
                text: "hello"
                halign : 'center'   

    



"""

Splash = """

MDScreen:
    name: "splash"
    MDFloatLayout:
        MDLabel:
            text: "hello welcome to app"
            haligin: "center"
   


"""


class Myapp(MDApp):
    def drawer(self):
        print('hellow world')
    data = {
        'Python': 'language-python',
        'Java': 'language-java',
        'Swift': 'language-swift',
        }
    def build(self):
       
        sm = ScreenManager()
        sm.add_widget(Builder.load_string(Main))
        # sm.add_widget(Builder.load_string(Splash))
        return sm
    #     Clock.schedule_once(self.home, 10)

    # def home(self, dt):
    #     sm.current = "Main"
    


Myapp().run() 