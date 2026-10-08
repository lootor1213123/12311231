from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SimpleMusicApp(App):

  def build(self):
    # 加载同目录下的音乐文件
    self.sound = SoundLoader.load("奶龙大笑.mp3")
    if self.sound:
      self.sound.loop = True
      self.sound.play()

    # 简单的界面显示
    layout = BoxLayout(orientation="vertical", padding=50)
    layout.add_widget(
        Label(
            text="程序运行中...\n请勿在多任务界面强制划掉后台",
            font_size=20,
            halign="center",
        )
    )
    return layout

  def on_stop(self):
    if self.sound:
      self.sound.stop()


if __name__ == "__main__":
  SimpleMusicApp().run()