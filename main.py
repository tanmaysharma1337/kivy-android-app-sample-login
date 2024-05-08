from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        
    
class RegisterWindow(Screen):
    def __init__(self, **kwargs):
        super(RegisterWindow, self).__init__(**kwargs)
        Builder.load_file("Controller.kv")
        layout = BoxLayout()
        headerimage = Image(source ='logo.png', size_hint_y=(2))
        Hlabel = Label(text='Sample Login',font_size=(30), bold = True)
        useridlabel = Label(text='Login ID',size_hint_y=(-0.4))
        i1 = TextInput(text = "")
        passwordlabel = Label(text='Password',size_hint_y=(-0.4))
        i2 = TextInput(text = "",password = True)
        b1 = Button(text = "Login")
        layout.add_widget(headerimage)
        layout.add_widget(Hlabel)
        layout.add_widget(useridlabel)
        layout.add_widget(i1)
        layout.add_widget(passwordlabel)
        layout.add_widget(i2)
        layout.add_widget(b1)
        self.add_widget(layout)
    def on_button_click(self,instance):
        print("working")
    
class LoginWindow(Screen):
        def __init__(self, **kwargs):
            super(LoginWindow, self).__init__(**kwargs)
            self.btn2 = Button(text='Go')
            self.add_widget(self.btn2)
            self.btn2.bind(on_press = self.screen_transition)

        def screen_transition(self, *args):
            self.manager.current = 'register'
    
# kv = Builder.load_file("Controller.kv")

class MainApp(App):
    
    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(RegisterWindow(name='register'))
        return sm

app = MainApp()
app.run()
