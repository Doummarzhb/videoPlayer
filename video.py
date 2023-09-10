import kivy
from kivy.app import App
from kivy.uix.video import Video
from kivy.core.window import window 
window.size=(380,610)
class MyApp(App):
    def build(self):
        self.title='Doummar[video players]'
        video =Video(source='vid.mp4')
        video.state='play'
        video.options ={'eos':'loop'}
        video.allow_stretch=True
    if __name__=='__main__':
        MyApp().run()