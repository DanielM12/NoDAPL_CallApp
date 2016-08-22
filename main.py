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
    Label:
        text: "This App calls These following Elected and Appointed US goverment officals and offices:
	ND Gov'nr : Billy Dumbass
	Da White House - YO!
	Couple Yeahoos from the Army Corp of Engineers
	etc"
    BoxLayout:
        size_hint_y: None
        size: (400,400)
       
        MakeCallButton:
            text: 'Make call via this app'
            on_release: self.call()


''')




class CallInterface(BoxLayout):
    pass


    
   



class MakeCallButton(Button):
    tel = {
        'Sam' : 'XXXXXXXXXX',
        'Sammie' : 'xxxxxxxxxx',
        'Samuel' : 'xxxxxxxxxx'
    }

    def call(self, *args):
        call.makecall(tel=self.tel['Sam'])
        call.makecall(tel=self.tel['Sammie'])
        call.makecall(tel=self.tel['Samuel'])
        	


class CallApp(App):

    def build(self):
        return CallInterface()

if __name__ == "__main__":
    app = CallApp()
    app.run()
