from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class Converter(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = 'Decimal to Binary'
            self.input.text = 'Enter a Decimal Number'
            self.converted.text = ''
            self.label.text = ''
        else:
            self.state = 0
            self.toolbar.title = 'Binary to Decimal'
            self.input.text = 'Enter a Binary Number'
            self.converted.text = ''
            self.label.text = ''
    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text,2)
            self.converted.text = str(val)
            self.label.text = 'in decimal is :'
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = val
            self.label.text = 'in Binary is :'
    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = 'Yellow'
        screen = MDScreen()
        # Header
        self.toolbar = MDTopAppBar(title='Binary to Decimal')
        self.toolbar.pos_hint = {'top' : 1}
        # Action button
        self.toolbar.right_action_items = [['rotate-3d-variant', lambda x : self.flip()]]
        screen.add_widget(self.toolbar)
        # Adding Logo
        screen.add_widget(Image(source='logo.png', pos_hint = {'center_x':0.5,'center_y':0.7}))
        # User input
        self.input = MDTextField(text='Enter a Binary Number', halign='center', size_hint=(0.8,1),
                                 pos_hint = {'center_x':0.5,'center_y':0.47}, font_size = 24)
        screen.add_widget(self.input)
        # Primary + Secondary labels
        self.label = MDLabel(halign='center',
                             pos_hint = {'center_x':0.5, 'center_y':0.35},
                             theme_text_color = 'Secondary')
        self.converted = MDLabel(halign='center',
                                 pos_hint={'center_x':0.5, 'center_y':0.3},
                                 theme_text_color = 'Primary',
                                 font_style='H5')
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # convert button
        screen.add_widget(MDFillRoundFlatButton(
            text='CONVERT', font_size=17,
            pos_hint={'center_x':0.5, 'center_y':0.15},
            on_press = self.convert
        )
        )


        return screen


if __name__ == '__main__':
    Converter().run()