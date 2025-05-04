import customtkinter as ctk
from tkinter import messagebox
import os
import datetime
import pytz
import webbrowser
import subprocess
import platform
from tkcalendar import Calendar
import shutil


# Попробуйте установить winshell: pip install winshell
try:
    import winshell
except ImportError:
    winshell = None

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

class AssistantApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NeoPC Assistant")
        self.geometry("900x600")

        self.current_frame = None

        # Верхнее меню
        self.menu_frame = ctk.CTkFrame(self)
        self.menu_frame.pack(side="top", fill="x", pady=5)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(expand=True, fill="both")

        buttons = [
            ("Игры", self.show_games),
            ("Отдых", self.show_entertainment),
            ("Работа", self.show_work),
            ("Управление", self.show_system),
            ("Приложения", self.show_apps),
            ("Календарь и Время", self.show_calendar_time),
            ("О программе", self.show_about),

        ]

        for name, command in buttons:
            btn = ctk.CTkButton(self.menu_frame, text=name, command=command)
            btn.pack(side="left", padx=5)

        self.show_games()  # Стартовый раздел

    def clear_content(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_games(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="🎮 Игры", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self.current_frame, text="Steam", command=self.run_steam).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Phasmophobia", command=lambda: self.run_steam_game("739630")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Terraria", command=lambda: self.run_steam_game("105600")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Skyrim", command=lambda: self.run_steam_game("72850")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Lost Light", command=lambda: self.run_steam_game("1894920")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="TLauncher (Minecraft)", command=self.run_tlauncher).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Telegram", command=lambda: webbrowser.open("https://web.telegram.org")).pack(pady=5)

    def show_entertainment(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="🎮 Отдых", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self.current_frame, text="YouTube", command=lambda: webbrowser.open("https://youtube.com")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Jut.su (аниме)", command=lambda: webbrowser.open("https://jut.su")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="ReManga", command=lambda: webbrowser.open("https://remanga.org")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Новелла 'Теневой раб'", command=lambda: webbrowser.open("https://ranobelib.me/ru/book/122448--shadow-slave")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Spotify", command=lambda: webbrowser.open("https://open.spotify.com")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Telegram", command=lambda: webbrowser.open("https://web.telegram.org")).pack(pady=5)

    def show_work(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="💼 Работа", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self.current_frame, text="Visual Studio Code", command=self.run_vscode).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Godot", command=self.run_godot).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="OBS Studio", command=self.run_obs).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Создать папку", command=self.create_folder_prompt).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Создать файл", command=self.create_file_prompt).pack(pady=5)

    def show_system(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="⚙️ Управление", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self.current_frame, text="Выключение ПК", command=self.confirm_shutdown).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Перезагрузка ПК", command=self.confirm_restart).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Спящий режим", command=lambda: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Открыть CMD", command=self.open_cmd).pack(pady=5)
        if winshell:
            ctk.CTkButton(self.current_frame, text="Очистить корзину", command=self.clear_recycle_bin).pack(pady=5)

    def show_apps(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="📦 Приложения", font=("Arial", 18)).pack(pady=10)

        ctk.CTkButton(self.current_frame, text="Radmin VPN", command=self.run_radmin).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Opera", command=lambda: os.startfile("C:\\Users\\Public\\Opera\\launcher.exe")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Сhrom", command=lambda: os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")).pack(pady=5)
        ctk.CTkButton(self.current_frame, text="Корзина", command=lambda: os.startfile("shell:RecycleBinFolder")).pack(pady=5)

    def show_about(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="🧬 О программе", font=("Arial", 18)).pack(pady=10)
        ctk.CTkLabel(self.current_frame, text="NeoPC Assistant\nАвтор: MRXIQW3 😄\nВерсия: 1.1", font=("Arial", 14)).pack(pady=20)

    def run_steam(self):
        try:
            os.startfile("steam://open")
        except:
            messagebox.showerror("Ошибка", "Не удалось открыть Steam.")

    def run_steam_game(self, app_id):
        try:
            os.startfile(f"steam://run/{app_id}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось запустить игру.\n{e}")

    def run_tlauncher(self):
        version_dir = r"C:\Users\pojkh\OneDrive\Рабочий стол\Mahiru 2.0\TLauncher\.minecraft_versions"
        mods_dir = r"C:\Users\pojkh\OneDrive\Рабочий стол\Mahiru 2.0\TLauncher\.minecraft_modpacks"
        maps_dir = r"C:\Users\pojkh\OneDrive\Рабочий стол\Mahiru 2.0\TLauncher\.minecraft_maps"  # НОВАЯ ПАПКА С КАРТАМИ

        minecraft_dir = r"C:\Users\pojkh\AppData\Roaming\.minecraft"
        tlauncher_path = os.path.join(minecraft_dir, "TLauncher.exe")

        if not os.path.exists(tlauncher_path):
            messagebox.showerror("Ошибка", "TLauncher не найден.")
            return

        dialog = ctk.CTkToplevel(self)

        dialog.lift()

        dialog.attributes('-topmost', True)

        dialog.title("Выбор сборки")
        dialog.geometry("400x450")

        ctk.CTkLabel(dialog, text="Выберите версию Minecraft").pack(pady=5)
        version_combobox = ctk.CTkComboBox(dialog, values=os.listdir(version_dir))
        version_combobox.pack(pady=5)

        ctk.CTkLabel(dialog, text="Выберите модпак").pack(pady=5)
        mods_combobox = ctk.CTkComboBox(dialog, values=os.listdir(mods_dir))
        mods_combobox.pack(pady=5)

        ctk.CTkLabel(dialog, text="Выберите карту").pack(pady=5)
        maps_combobox = ctk.CTkComboBox(dialog, values=["Нет"] + os.listdir(maps_dir))
        maps_combobox.pack(pady=5)


    # Функция для запуска TLauncher
        def launch():
            selected_version = version_combobox.get()
            selected_mods = mods_combobox.get()
            selected_map = maps_combobox.get()

         # Копируем файлы версии
            version_path = os.path.join(version_dir, selected_version)
            if os.path.exists(version_path):
                shutil.copytree(version_path, minecraft_dir, dirs_exist_ok=True)

        # Копируем моды
            mods_path = os.path.join(mods_dir, selected_mods)
            mods_target = os.path.join(minecraft_dir, "mods")
            if os.path.exists(mods_target):
                shutil.rmtree(mods_target)

            if os.path.exists(mods_path):
                shutil.copytree(mods_path, mods_target)

        # Копируем карту
            if selected_map != "Нет":
                saves_dir = os.path.join(minecraft_dir, "saves")
                map_source = os.path.join(maps_dir, selected_map)
                map_target = os.path.join(saves_dir, selected_map)

                if os.path.exists(map_target):
                    shutil.rmtree(map_target)

                if os.path.exists(map_source):
                    shutil.copytree(map_source, map_target)

            os.startfile(tlauncher_path)
            dialog.destroy()

    # Функция для применения только карты
        def apply_map_only():
            selected_map = maps_combobox.get()
            if selected_map != "Нет":
                saves_dir = os.path.join(minecraft_dir, "saves")
                map_source = os.path.join(maps_dir, selected_map)
                map_target = os.path.join(saves_dir, selected_map)

                if os.path.exists(map_target):
                    shutil.rmtree(map_target)

                if os.path.exists(map_source):
                    shutil.copytree(map_source, map_target)

                messagebox.showinfo("Готово", f"Карта '{selected_map}' успешно применена!")

        # Кнопки
        ctk.CTkButton(dialog, text="Запустить TLauncher", command=launch).pack(pady=10)
        ctk.CTkButton(dialog, text="Добавить/Обновить карту без запуска", command=apply_map_only).pack(pady=10)



    def run_vscode(self):
        try:
            subprocess.Popen(["code"])
        except Exception as e:
            messagebox.showerror("Ошибка", f"VS Code не найден.\n{e}")

    def run_godot(self):
        path = "C:\\Godot\\Godot.exe"
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox.showerror("Ошибка", "Godot не найден.")

    def run_obs(self):
        path = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox.showerror("Ошибка", "OBS Studio не найден.")

    def run_radmin(self):
        path = "C:\\Program Files (x86)\\Radmin VPN\\RadminVPN.exe"
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox.showerror("Ошибка", "Radmin VPN не найден.")

    def confirm_shutdown(self):
        if messagebox.askyesno("Выключение", "Вы уверены, что хотите выключить компьютер?"):
            self.shutdown_pc()


    def shutdown_pc(self):
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /s /t 1")
        elif system == "Linux" or system == "Darwin":
            os.system("shutdown now")
        else:
            messagebox.showerror("Ошибка", "Неизвестная операционная система.")

    def confirm_restart(self):
        if messagebox.askyesno("Перезагрузка", "Вы уверены, что хотите перезагрузить компьютер?"):
            os.system("shutdown /r /t 0")

    def create_folder_prompt(self):
        popup = ctk.CTkInputDialog(title="Создание папки", text="Введите имя папки:")
        folder_name = popup.get_input()
        if folder_name:
            try:
                os.makedirs(folder_name, exist_ok=True)
                messagebox.showinfo("Успех", f"Папка '{folder_name}' создана.")
                os.startfile(folder_name)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    def create_file_prompt(self):
        popup = ctk.CTkInputDialog(title="Создание файла", text="Введите имя файла (с расширением):")
        file_name = popup.get_input()
        if file_name:
            try:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write("")
                messagebox.showinfo("Успех", f"Файл '{file_name}' создан.")
                os.startfile(file_name)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    def open_cmd(self):
        subprocess.Popen("cmd")

    def clear_recycle_bin(self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            messagebox.showinfo("Готово", "Корзина очищена.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при очистке: {e}")

    def show_calendar_time(self):
        self.clear_content()
        self.current_frame = ctk.CTkFrame(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

        ctk.CTkLabel(self.current_frame, text="📅 Календарь и 🌍 Время", font=("Arial", 18)).pack(pady=10)

        cal = Calendar(self.current_frame, selectmode='day')
        cal.pack(pady=10)

        time_zone_label = ctk.CTkLabel(self.current_frame, text="Текущее время по миру:", font=("Arial", 14))
        time_zone_label.pack(pady=5)

        # Метка для отображения времени
        self.time_display = ctk.CTkLabel(self.current_frame, text="", font=("Arial", 14))
        self.time_display.pack(padx=10, pady=5)

        self.update_world_time()

    def update_world_time(self):
        zones = ["Europe/Moscow", "UTC", "America/New_York", "Asia/Tokyo", "Australia/Sydney"]
        now = datetime.datetime.now()
        
        time_str = ""
        for zone in zones:
            tz = pytz.timezone(zone)
            zone_time = now.astimezone(tz)
            time_str += f"{zone}: {zone_time.strftime('%Y-%m-%d %H:%M:%S')}\n"

        self.time_display.configure(text=time_str)

        # Обновление каждые 60 секунд
        self.after(60000, self.update_world_time)  # Обновить каждые 60 секунд


if __name__ == "__main__":
    app = AssistantApp()
    app.mainloop()