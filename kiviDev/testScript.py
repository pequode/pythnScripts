# import kivy.core.audio
# print("test")
# from kivy.app import App
# from kivy.uix.label import Label
#
# class MainApp(App):
#     def build(self):
#         label = Label(text='Hello from Kivy',
#                       size_hint=(.5, .5),
#                       pos_hint={'center_x': .5, 'center_y': .5})
#
#         return label
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )
            btn.bind(on_press=self.on_press_button)

            layout.add_widget(btn)
        return layout
    def on_press_button(self, instance):
        print('You pressed the button!')

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
