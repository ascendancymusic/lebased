import re
import random
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime, timedelta
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
import kivymd.icon_definitions
import sqlite3
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
LabelBase.register(name="Poppins", fn_regular="fonts/Poppins-Regular.ttf")
LabelBase.register(name="PoppinsBold", fn_regular="fonts/Poppins-SemiBold.ttf")
LabelBase.register(name="PoppinsThin", fn_regular="fonts/Poppins-Thin.ttf")
LabelBase.register(name="Elegance", fn_regular="fonts/Rounded_Elegance.ttf")
LabelBase.register(name="Tex", fn_regular="fonts/tex-gyre-adventor.regular.otf")
LabelBase.register(name="TexBold", fn_regular="fonts/tex-gyre-adventor.bold.otf")
Window.size = (575, 960)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class AddToDoScreen(Screen):
    def validate_and_add_task(self):
        title = self.ids.title.text.strip()
        description = self.ids.description.text.strip()
        
        # Validate title length
        if not 0 < len(title) <= 20:
            self.show_error_dialog("Title length should be between 1 and 20 characters.")
            return
        
        # Validate description length
        if not 0 < len(description) <= 60:
            self.show_error_dialog("Description length should be between 1 and 60 characters.")
            return
        
        # Add task if validation passes
        todo_screen = self.manager.get_screen("todo")
        todo_screen.add_task(title, description)
        self.manager.current = "todo"
        
    def show_error_dialog(self, message):
        dialog = MDDialog(title="Error", text=message)
        dialog.open()


# Connect to SQLite database
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             description TEXT,
             date TEXT,
             checkbox_state INTEGER)''')

# Check if the checkbox_state column exists in the tasks table
c.execute("PRAGMA table_info(tasks)")
columns = c.fetchall()
column_names = [column[1] for column in columns]
if 'checkbox_state' not in column_names:
    # Add the checkbox_state column if it doesn't exist
    c.execute("ALTER TABLE tasks ADD COLUMN checkbox_state INTEGER")
    conn.commit()



class TaskBoxLayout(BoxLayout):
    title_label = ObjectProperty(None)
    description_label = ObjectProperty(None)
    checkbox = ObjectProperty(None)
    task_id = None
    checkbox_state = NumericProperty(0)

    def on_checkbox_active(self, checkbox, active):
        self.checkbox_state = 1 if active else 0
        if self.task_id:
            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()
            c.execute("UPDATE tasks SET checkbox_state=? WHERE id=?", (self.checkbox_state, self.task_id))
            conn.commit()
            conn.close()

        if active:
            self.title_label.text = '[s]' + self.title_label.text + '[/s]'
            self.description_label.text = '[s]' + self.description_label.text + '[/s]'
        else:
            self.title_label.text = self.title_label.text.replace('[s]', '').replace('[/s]', '')
            self.description_label.text = self.description_label.text.replace('[s]', '').replace('[/s]', '')

        # Notify the Kv language file to update the background color
        self.canvas.before.children[0].rgba = (0.341, 0.773, 0.714, 1) if active else (0, 0.169, 0.357, 1)

    def set_checkbox_state(self, state):
        self.checkbox_state = state
        if self.checkbox:
            self.checkbox.active = bool(state)

    def on_checkbox_state(self, instance, value):
        if self.checkbox:
            self.checkbox.active = bool(value)

class ToDoScreen(Screen):
    current_date = datetime.now()

    def __init__(self, **kwargs):
        super(ToDoScreen, self).__init__(**kwargs)
        self.refresh_tasks()

    def update_date(self, delta):
        self.current_date += timedelta(days=delta)
        self.ids.date_label.text = self.current_date.strftime("%A, %B %d, %Y")
        self.refresh_tasks()

    def refresh_tasks(self):
        current_date_str = self.current_date.strftime("%d.%m.%Y")
        task_layout = self.ids.task_list
        task_layout.clear_widgets()
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE date=?", (current_date_str,))
        tasks = c.fetchall()
        for task in tasks:
            task_widget = TaskBoxLayout()
            task_widget.title_label.text = task[1]
            task_widget.description_label.text = task[2]
            task_widget.task_id = task[0]
            task_widget.set_checkbox_state(task[4])  # Set checkbox state
            task_layout.add_widget(task_widget)
        conn.close()

    def add_task(self, title, description):
        current_date_str = self.current_date.strftime("%d.%m.%Y")
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("INSERT INTO tasks (title, description, date, checkbox_state) VALUES (?, ?, ?, ?)", (title, description, current_date_str, 0))
        conn.commit()
        conn.close()
        self.refresh_tasks()

    def delete_task(self, task_id):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
        self.refresh_tasks()



class StatsScreen(Screen):
    stats_text = StringProperty()
    average_sleep_time = StringProperty("N/A")
    average_get_up_time = StringProperty("N/A")

    def on_enter(self):
        self.refresh_stats()

    def refresh_stats(self):
        stats_text = self.get_stats_text()
        stats_label = self.ids.stats_label
        stats_label.text = stats_text
        stats_label.color = (1, 1, 1, 1)  # Set text color to white

        # Update average sleep time
        self.update_average_sleep_time()

        # Update average get up time
        self.update_average_get_up_time()

    def get_stats_text(self):
        stats_text = ""
        with open("stats.txt", "r") as file:
            lines = file.readlines()
            entries = []  # List to store individual entries
            current_entry = ""  # String to accumulate lines for each entry
            for line in lines:
                if line.strip():  # Non-empty line
                    current_entry += line
                else:  # Empty line, indicates end of current entry
                    entries.append(current_entry.strip())
                    current_entry = ""

            if current_entry:  # Add the last entry if not empty
                entries.append(current_entry.strip())

            entries.sort(reverse=True)  # Sort the entries in descending order by date

            for entry in entries:
                lines = entry.split('\n')
                for index, line in enumerate(lines):
                    if (index + 1) % 7 == 1:  # Apply TexBold formatting every 7th line starting from the 1st line
                        stats_text += f"[font=TexBold]{line.strip()}[/font]\n"
                    else:
                        stats_text += f"[font=Tex]{line.strip()}[/font]\n"
                stats_text += "\n\n"  # Add two newline characters between entries

        return stats_text

        

    def update_average_sleep_time(self):
        sleep_times = []
        with open("stats.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Sleep: " in line:
                    try:
                        sleep_time = line.strip().split(": ")[1]
                        hours, minutes = map(int, sleep_time.split(":"))
                        total_minutes = hours * 60 + minutes
                        sleep_times.append(total_minutes)
                    except ValueError:
                        pass

        if sleep_times:
            average_minutes = sum(sleep_times) // len(sleep_times)
            average_hours = average_minutes // 60
            average_minutes %= 60
            self.average_sleep_time = f"{average_hours:02d}:{average_minutes:02d}"
        else:
            self.average_sleep_time = "N/A"

    def update_average_get_up_time(self):
        get_up_times = []
        with open("stats.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Got up: " in line:
                    try:
                        get_up_time = line.strip().split(": ")[1]
                        hours, minutes = map(int, get_up_time.split(":"))
                        total_minutes = hours * 60 + minutes
                        get_up_times.append(total_minutes)
                    except ValueError:
                        pass

        if get_up_times:
            average_minutes = sum(get_up_times) // len(get_up_times)
            average_hours = average_minutes // 60
            average_minutes %= 60
            self.average_get_up_time = f"{average_hours:02d}:{average_minutes:02d}"
        else:
            self.average_get_up_time = "N/A"

    def show_delete_confirmation_dialog(self):
        dialog = MDDialog(
            title="Delete Confirmation",
            text="Are you sure you want to delete all data?",
            size_hint=(0.8, 0.18),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="Delete",
                    on_release=lambda *args: self.delete_stats_data(dialog)
                ),
            ]
        )
        dialog.open()

    def delete_stats_data(self, dialog):
        with open("stats.txt", "w") as file:
            file.write("")
        dialog.dismiss()
        self.refresh_stats()  # Refresh the stats screen after deletion 


class SleeparScreen(Screen):
    sleep_button_disabled = BooleanProperty(False)
    text_input_visible = BooleanProperty(False)
    done_button_visible = BooleanProperty(False)
    get_up_data = None

    def on_enter(self):
        Clock.schedule_interval(self.update_time, 0)

    def update_time(self, dt):
        current_time = datetime.now().strftime("%H:%M")
        self.ids.current_time_label.text = current_time

    def switch_buttons(self, mode):
        sleep_button = self.ids.sleep_button
        get_up_button = self.ids.get_up_button
        cleanar_label = self.ids.cleanar_label
        cleanar_options = self.ids.cleanar_options

        if mode == 'sleep':
            sleep_button.disabled = True
            get_up_button.disabled = True
            cleanar_label.opacity = 1
            cleanar_options.opacity = 1
        elif mode == 'get_up':
            sleep_button.disabled = True
            get_up_button.disabled = True
            cleanar_label.opacity = 0
            cleanar_options.opacity = 0

    def show_cleanar_options(self):
        self.switch_buttons('sleep')

    def hide_cleanar_options(self):
        cleanar_label = self.ids.cleanar_label
        cleanar_options = self.ids.cleanar_options
        cleanar_label.opacity = 0
        cleanar_options.opacity = 0

    def set_sleep_button_state(self, status):
        self.sleep_button_disabled = status == 'ofc' or status == 'no'

    def on_cleanar_button_press(self, status):
        self.hide_cleanar_options()
        get_up_button = self.ids.get_up_button

        # Get current time
        current_time = datetime.now().strftime("%H:%M")

        # Determine text based on current time
        if "20:00" <= current_time <= "21:29":
            dialog_text = "Alien sleepar early af nigga!"
        elif "21:30" <= current_time <= "21:59":
            dialog_text = "WOW! Early sleepar! Good night!"
        elif "22:00" <= current_time <= "22:15":
            dialog_text = "Great! Sleepar well!"
        elif "22:16" <= current_time <= "22:30":
            dialog_text = "Nice! Good night!"
        elif "22:31" <= current_time <= "22:45":
            dialog_text = "Not bad!"
        elif "22:46" <= current_time <= "23:00":
            dialog_text = "You can do better, but good night!"
        elif "23:01" <= current_time <= "23:59":
            dialog_text = "Go to sleep earlier tomorrow."
        elif "00:00" <= current_time <= "05:00":
            dialog_text = "What is wrong with you?"
        else:
            dialog_text = "Alien time sleepar"

        # Create and display the dialog
        dialog = MDDialog(title='Sleep time!', text=dialog_text, size_hint=(0.8, 0.1))
        dialog.font_name = "TexBold"
        dialog.open()

        # Automatically dismiss the dialog after 3 seconds
        Clock.schedule_once(lambda dt: dialog.dismiss(), 3)

        # Update sleep and clean status in stats.txt
        current_date = datetime.now().strftime("%d.%m.%Y")
        current_time = datetime.now().strftime("%H:%M")

        # Check if sleep time is between 0:00 and 5:00 to consider it part of the previous day
        if 0 <= int(current_time.split(':')[0]) <= 5:
            current_date = (datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")

        with open("stats.txt", "r+") as file:
            lines = file.readlines()
            found = False
            for index, line in enumerate(lines):
                if line.startswith(current_date):
                    found = True
                    lines[index + 2] = f"Sleep: {current_time}\n"
                    lines[index + 3] = f"Clean: {'Yes' if status == 'ofc' else 'No'}\n"
                    file.seek(0)
                    file.truncate()
                    file.writelines(lines)
                    break

            if not found:
                lines.append(f"{current_date}\n")
                lines.append(f"Got up: -\n")
                lines.append(f"Sleep: {current_time}\n")
                lines.append(f"Clean: {'Yes' if status == 'ofc' else 'No'}\n\n\n")
                file.seek(0)
                file.writelines(lines)

        # Enable the get up button
        get_up_button.disabled = False

    def get_up_pressed(self):
        current_date = datetime.now().strftime("%d.%m.%Y")
        current_time = datetime.now().strftime("%H:%M")
        self.text_input_visible = True
        self.done_button_visible = True
        self.get_up_data = (current_date, current_time)
        get_up_button = self.ids.get_up_button
        get_up_button.disabled = True
        # Update the UI
        self.switch_buttons('get_up')

    def done_button_pressed(self):
        current_date, current_time = self.get_up_data
        dream_text = self.ids.dream_input.text.strip()  # Get the dream text from the input field
        self.text_input_visible = False
        self.done_button_visible = False
        get_up_button = self.ids.get_up_button
        sleep_button = self.ids.sleep_button
        get_up_button.disabled = True
        sleep_button.disabled = False
        dream_text = self.ids.dream_input.text if self.ids.dream_input.text.strip() else "No dreams"

        # Determine text based on current time
        if "05:00" <= current_time <= "06:59":
            dialog_text = "Alien wake upar early af nigga!"
        elif "07:00" <= current_time <= "07:45":
            dialog_text = "WOW! Early get up! Good Morning King!"
        elif "07:46" <= current_time <= "08:15":
            dialog_text = "Great! Good morning!"
        elif "08:16" <= current_time <= "08:45":
            dialog_text = "Nice! Good morning!"
        elif "08:46" <= current_time <= "09:15":
            dialog_text = "Not bad! Go seize the day!"
        elif "09:16" <= current_time <= "09:59":
            dialog_text = "You can do better, but good morning!"
        elif "10:00" <= current_time <= "11:00":
            dialog_text = "Get up a lot earlier tomorrow."
        elif "11:01" <= current_time <= "12:00":
            dialog_text = "What is wrong with you?"
        else:
            dialog_text = "What's wrong with you nigga who gets up this late?"

        # Create and display the dialog
        dialog = MDDialog(title='Morning!', text=dialog_text, size_hint=(0.8, 0.1))
        dialog.font_name = "TexBold"
        dialog.open()

        # Automatically dismiss the dialog after 3 seconds
        Clock.schedule_once(lambda dt: dialog.dismiss(), 3)

        with open("stats.txt", "r+") as file:
            lines = file.readlines()
            found = False
            for index, line in enumerate(lines):
                if line.startswith(current_date):
                    found = True
                    lines[index + 1] = f"Got up: {current_time}\n"
                    lines[index + 4] = f"Dreams: {dream_text}\n\n"  # Update the line for dreams
                    file.seek(0)
                    file.truncate()
                    file.writelines(lines)
                    break

            if not found:
                lines.append(f"{current_date}\n")
                lines.append(f"Got up: {current_time}\n")
                lines.append(f"Sleep: -\n")
                lines.append(f"Clean: -\n")
                lines.append(f"Dreams: {dream_text}\n\n\n")  # Add line for dreams
                file.seek(0)
                file.writelines(lines)

    def sleep_button_pressed(self):
        self.show_cleanar_options()


class PlannerScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LeBasedApp(MDApp):
    def build(self):
        self.icon = "LeBased.png"
        # Load KV files for each screen
        Builder.load_file('main_screen.kv')
        Builder.load_file('todo_screen.kv')
        Builder.load_file('stats_screen.kv')
        Builder.load_file('sleepar_screen.kv')
        Builder.load_file('planner_screen.kv')
        Builder.load_file('about_screen.kv')
        Builder.load_file('add_todo.kv')
        
        # Screen Manager
        sm = ScreenManager()

        # Main Screen
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)

        # To-Do Screen
        todo_screen = ToDoScreen(name='todo')
        sm.add_widget(todo_screen)

        # Stats Screen
        stats_screen = StatsScreen(name='stats')
        sm.add_widget(stats_screen)

        # Sleepar Screen
        sleepar_screen = SleeparScreen(name='sleepar')
        sm.add_widget(sleepar_screen)

        # Planner Screen
        planner_screen = PlannerScreen(name='planner')
        sm.add_widget(planner_screen)

        # About Screen
        about_screen = AboutScreen(name='about')
        sm.add_widget(about_screen)

        # Add ToDo Screen
        add_todo_screen = AddToDoScreen(name='add_todo')
        sm.add_widget(add_todo_screen)

        # Layout for Main Screen
        main_layout = GridLayout(cols=1, padding=[0, 50], spacing=10)

        # Title
        title = MDLabel(text="Welcome to Le Based App", halign="center", bold=True, theme_text_color="Custom", text_color=(1, 1, 1, 1))
        title.font_size = "32"
        title.font_name = "TexBold"
        title.text_color = (1, 1, 1, 1)
        main_layout.add_widget(title)

        # Load quotes from file
        quotes = self.load_quotes()

        # Randomly select a quote
        random_quote = random.choice(quotes)

        # Strip number prefix from the quote
        random_quote = re.sub(r'^\d+: ', '', random_quote)

        # Quote Label
        quote_label = MDLabel(
            text=f"[font=TexBold]Random insight[/font]: [font=Tex]{random_quote}[/font]",
            halign="center",
            markup=True,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        quote_label.font_size = "20"
        main_layout.add_widget(quote_label)

        # Buttons layout
        buttons_layout = GridLayout(cols=1, spacing=5)

        # Calculate button height and width based on screen width
        button_height = 750
        button_width = 0.5  # Relative width

        # Button 1: To-Do
        todo_button = MDFlatButton(
            text="To-Do",
            size_hint=(button_width, None),
            height=button_height,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_name="Tex",
            md_bg_color=(0.341, 0.773, 0.714),
        )
        todo_button.bind(on_press=self.switch_to_todo)
        buttons_layout.add_widget(todo_button)

        # Button 2: Stats
        stats_button = MDFlatButton(
            text="Stats",
            size_hint=(button_width, None),
            height=button_height,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_name="Tex",
            md_bg_color=(0.341, 0.773, 0.714),
        )
        stats_button.bind(on_press=self.switch_to_stats)
        buttons_layout.add_widget(stats_button)

        # Button 3: Sleepar
        sleepar_button = MDFlatButton(
            text="Sleepar",
            size_hint=(button_width, None),
            height=button_height,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_name="Tex",
            md_bg_color=(0.341, 0.773, 0.714),
        )
        sleepar_button.bind(on_press=self.switch_to_sleepar)
        buttons_layout.add_widget(sleepar_button)

        # Button 4: Planner
        planner_button = MDFlatButton(
            text="Planner",
            size_hint=(button_width, None),
            height=button_height,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_name="Tex",
            md_bg_color=(0.341, 0.773, 0.714),
        )
        planner_button.bind(on_press=self.switch_to_planner)
        buttons_layout.add_widget(planner_button)

        # Button 5: About
        about_button = MDFlatButton(
            text="About",
            size_hint=(button_width, None),
            height=button_height,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_name="Tex",
            md_bg_color=(0.341, 0.773, 0.714),
        )
        about_button.bind(on_press=self.switch_to_about)
        buttons_layout.add_widget(about_button)

        # Add Buttons layout to Main Screen layout
        main_layout.add_widget(buttons_layout)

        # Add Main Screen Layout to Main Screen
        main_screen.add_widget(main_layout)

        # Layout for To-Do Screen
        todo_layout = GridLayout(cols=1)

        # Add To-Do Screen Layout to To-Do Screen
        todo_screen.add_widget(todo_layout)

        # Layout for Stats Screen
        stats_layout = GridLayout(cols=1)

        # Add Stats Screen Layout to Stats Screen
        stats_screen.add_widget(stats_layout)

        # Layout for Sleepar Screen
        sleepar_layout = GridLayout(cols=1)

        # Add Sleepar Screen Layout to Sleepar Screen
        sleepar_screen.add_widget(sleepar_layout)

        return sm

    def load_quotes(self):
        quotes = []
        with open('quotes.txt', 'r') as file:
            quote = ''
            for line in file:
                line = line.strip()
                if re.match(r'^\d+: ', line):
                    if quote:
                        quotes.append(quote)
                    quote = line
                else:
                    quote += '\n' + line
            if quote:
                quotes.append(quote)
        return quotes

    def switch_to_main(self, instance):
        self.root.current = 'main'

    def switch_to_todo(self, instance):
        self.root.current = 'todo'

    def switch_to_stats(self, instance):
        self.root.current = 'stats'

    def switch_to_sleepar(self, instance):
        self.root.current = 'sleepar'

    def switch_to_planner(self, instance):
        self.root.current = 'planner'

    def switch_to_about(self, instance):
        self.root.current = 'about'

    def switch_to_add_todo(self, instance):
        self.root.current = 'add_todo'


if __name__ == '__main__':
    LeBasedApp().run()
