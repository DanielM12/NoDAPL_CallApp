from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty
from plyer import call


Builder.load_string('''


#: import Platform kivy.utils.platform
<CallInterface>:
    orientation: 'vertical'

    BoxLayout:
        size_hint_y: None
        size: (600,400)
	 Label:
            text: "NO DAPL Call App"
       
        MakeCallButton:
            text: 'Call Officials Now'
            on_release: self.call()


''')

class CallInterface(BoxLayout):
    pass

class MakeCallButton(Button):
    tel = {
        'Congressman_Cramer' : '2022252611',
        'Governor_Dalrymple' : '7013282200',
        'John_Henderson_ArmyCorp' : '4029952229',
        'Eileen_Williamson_ArmyCorp' : '4029952417',
        'White_House' : '20245461111'
    }

    def call(self, *args):
        call.makecall(tel=self.tel['White_House'])
    	call.makecall(tel=self.tel['Eileen_Williamson_ArmyCorp'])
    	call.makecall(tel=self.tel['John_Henderson_ArmyCorp'])
    	call.makecall(tel=self.tel['Governor_Dalrymple'])
        call.makecall(tel=self.tel['Congressman_Cramer'])
        	


class CallApp(App):

    def build(self):
        return CallInterface()

if __name__ == "__main__":
    app = CallApp()
    app.run()
