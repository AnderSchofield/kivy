import textwrap
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

class KvApp(App):
    def build(self):
        # Set the window size to 1200x800 pixels
        Window.size = (1200, 800)

        self.root = BoxLayout(orientation='horizontal')

        # Create a Text Input for KV code
        self.kv_input = TextInput(size_hint_x=0.7)
        self.kv_input.bind(text=self.update)
        self.root.add_widget(self.kv_input)

        # Create widget placeholder
        self.kv_display = Label(size_hint_x=0.3)
        self.root.add_widget(self.kv_display)

        return self.root

# ... in the KvViewerApp class ...

    def update(self, instance, value)
        self.root.remove_widget(self.kv_display)
        try:
            # Use textwrap.dedent on value to remove any common leading whitespace
            self.kv_display = Builder.load_string(textwrap.dedent(value))
            self.kv_display.size_hint_x = 0.5
            self.root.add_widget(self.kv_display)
        except Exception as e:
            self.kv_display = Label(text=str(e), size_hint_x=0.5)
            self.root.add_widget(self.kv_display)

if __name__ == '__main__':
    KvApp().run()
