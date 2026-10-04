from kivy.config import Config
Config.set('graphics','resizable','0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

KV = '''
<RootLayout>:
    canvas.before:
        Rectangle:
            source: "images/fonreg.jpg"
            pos: self.pos
            size: self.size

'''

class RootLayout(BoxLayout):
    pass
class myapp(App):
    def build(self):
        self.bx = RootLayout(orientation = "vertical",padding = 125,spacing = 10)

        self.login_input = TextInput(font_size = 50)
        self.password_input = TextInput(font_size = 50)

        self.login_buton = Button(text = "log in", font_size = 50, on_press = self.login_press)
        self.signup_buton = Button(text="sign up", font_size=50)

        self.lg_text = Label(font_size = 40, text = "")

        self.bx.add_widget(self.lg_text)
        self.bx.add_widget(self.login_input)
        self.bx.add_widget(self.password_input)
        self.bx.add_widget(self.login_buton)
        self.bx.add_widget(self.signup_buton)

        return self.bx

    def login_press(self, instance):
        if self.login_input.text == "WonderExploude" and self.password_input.text == str(1290):
            self.bx.remove_widget(self.login_input)
            self.bx.remove_widget(self.password_input)
            self.bx.remove_widget(instance)
            self.bx.remove_widget(self.signup_buton)
            self.lg_text.text = 'Ты бос'
            self.lg_text.color = (0,1,0,1)
        else:
            self.lg_text.text = "Ты не бос"
            self.lg_text.color = (1,0,0,1)

Builder.load_string(KV)
myapp().run()
