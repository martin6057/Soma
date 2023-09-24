from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class ExitPopup(Popup):
    def __init__(self, **kwargs):
        super(ExitPopup, self).__init__(**kwargs)
        self.title = "Exit Confirmation"
        self.size_hint = (None, None)
        self.size = (300, 200)

        content_layout = BoxLayout(orientation='vertical')
        content_layout.spacing = 10

        message_label = Label(text="Are you sure you want to exit?")
        content_layout.add_widget(message_label)

        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        cancel_button = Button(text="Cancel")
        confirm_button = Button(text="Exit")

        cancel_button.bind(on_release=self.dismiss)  # Close the popup
        confirm_button.bind(on_release=self.exit_app)  # Call the exit function

        button_layout.add_widget(cancel_button)
        button_layout.add_widget(confirm_button)

        content_layout.add_widget(button_layout)
        self.content = content_layout

    def exit_app(self, instance):
        App.get_running_app().stop()  # Close the app

class MutePopup(Popup):
    def __init__(self, **kwargs):
        super(MutePopup, self).__init__(**kwargs)
        self.title = "Mute Sound"
        self.size_hint = (None, None)
        self.size = (300, 200)

        content_layout = BoxLayout(orientation='vertical')
        content_layout.spacing = 10

        message_label = Label(text="Toggle sound on/off:")
        content_layout.add_widget(message_label)

        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        mute_button = Button(text="Mute")
        unmute_button = Button(text="Unmute")

        mute_button.bind(on_release=self.mute_sound)      # Call the mute function
        unmute_button.bind(on_release=self.unmute_sound)  # Call the unmute function

        button_layout.add_widget(mute_button)
        button_layout.add_widget(unmute_button)

        content_layout.add_widget(button_layout)
        self.content = content_layout

    def mute_sound(self, instance):
        # Implement muting sound functionality here (e.g., stop audio playback)
        pass

    def unmute_sound(self, instance):
        # Implement unmuting sound functionality here (e.g., resume audio playback)
        pass

class IntroScreen(Screen):
    def on_enter(self):
        # Play the animation video when the screen is entered
        self.video = Video(source='intro_animation.mp4', state='play')
        self.add_widget(self.video)

class MainMenuScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title_label = Label(text="Soma - Learning Game for Kids")
        layout.add_widget(title_label)
        start_button = Button(text="Start Learning")
        start_button.bind(on_press=self.go_to_numbers)
        layout.add_widget(start_button)
        return layout

    def go_to_numbers(self, instance):
        # This is where you'll navigate to the Numbers page
        pass

class SideMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(SideMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        login_button = Button(text="Log In")
        login_button.bind(on_release=self.show_login_popup)
        self.add_widget(login_button)

        account_button = Button(text="Account Profile")
        account_button.bind(on_release=self.go_to_account_profile)
        self.add_widget(account_button)

        settings_button = Button(text="Settings")
        settings_button.bind(on_release=self.go_to_settings)
        self.add_widget(settings_button)

        exit_button = Button(text="Exit")
        exit_button.bind(on_release=self.show_exit_popup)
        self.add_widget(exit_button)

        mute_button = Button(text="Mute")
        mute_button.bind(on_release=self.show_mute_popup)
        self.add_widget(mute_button)

    def show_login_popup(self, instance):
        # Display a login popup or screen here
        popup = Popup(title='Log In', content=Label(text='Login Form Here'), size_hint=(None, None), size=(300, 200))
        popup.open()

    def go_to_account_profile(self, instance):
        # Navigate to the user's account profile page
        pass

    def go_to_settings(self, instance):
        # Navigate to the settings page
        pass

    def show_exit_popup(self, instance):
        exit_popup = ExitPopup()
        exit_popup.open()

    def show_mute_popup(self, instance):
        mute_popup = MutePopup()
        mute_popup.open()

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 10

        side_menu = SideMenu()
        self.add_widget(side_menu)

        main_content = Label(text="Welcome to Soma - Learning Game")
        self.add_widget(main_content)

class SomaApp(App):
    def build(self):
        # Create a ScreenManager to manage different screens
        sm = ScreenManager()

        # Create the Intro Screen
        intro_screen = IntroScreen(name='intro')
        sm.add_widget(intro_screen)

        # Create the Main Menu Screen
        main_menu_screen = MainMenuScreen(name='main_menu')
        sm.add_widget(main_menu_screen)

        # Create the Home Page with Side Menu
        home_page = HomePage()
        sm.add_widget(Screen(name='home', content=home
