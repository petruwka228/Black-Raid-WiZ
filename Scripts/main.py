import tkinter as tk
from tkinter import messagebox
import time


# Функция для создания INI файла
def create_event_file():
    try:
        with open('Events_Story.ini', 'w', encoding='utf-8-sig') as f:
            f.write('[Event-Info] \n')
            f.write('Step=1\n')
            f.write('Zona=1\n')
            f.write('Type=Info\n')
            f.write('Img=gfx\\icons\\events\\start.png\n')
            f.write('TargetResourceImg=gfx\\old\\NoData_100x100.png\n')
            f.write('Name=Информация\n')
            f.write(
                'Desc-Owner=Добро пожаловать в ад, ребята. Каждые 5 ходов на карте появляется аирдроп. на 25 ходу будет известна точка эвакуации. Работаем быстро и четко. Кто накосячит - останется на острове\n')
            f.write(
                'Desc-NonOwner=Добро пожаловать в ад, ребята. Каждые 5 ходов на карте появляется аирдроп. на 25 ходу будет известна точка эвакуации. Работаем быстро и четко. Кто накосячит - останется на острове\n')
            f.write('ShowForOwner=True\n')
            f.write('ShowForNonOwner=True\n')
            f.write('AddToGameLog=True\n')
            f.write('SoundFXForOwner=True\n')
            f.write('SoundFXForOwnerFile=sfx\events\\baron.mp3\n')
            f.write('SoundFXForNonOwner=True\n')
            f.write('SoundFXForNonOwnerFile=sfx\events\\baron.mp3\n')
            f.write('\n')


    except Exception as e:
        return f"Ошибка при создании файла: {e}"


# Функция для импорта модулей
def import_modules():
    try:
        import wiz
        import airdrops
        import zombie_addunits
        import Zombie_Invasion
        import Shopot_AddResources
        import traders
        import market
        import camp
        import base
        time.sleep(1)
        import EndVictory
        import traders_good
        return "Модули успешно импортированы."
    except ImportError as e:
        return f"Ошибка импорта: {e}"


# Основная функция для обработки событий при нажатии кнопки
def on_button_click():
    file_creation_message = create_event_file()  # Создание INI файла
    module_import_message = import_modules()  # Импортирование модулей

    # Выводим сообщение в окно
    messagebox.showinfo("Результат", f"{module_import_message}")


# Создание основного окна приложения
root = tk.Tk()
root.title("Рандомайзер")

# Настройка интерфейса
label = tk.Label(root, text="Нажмите кнопку для того, чтобы зарандомить файлы.", padx=20, pady=20)
label.pack()

button = tk.Button(root, text="Roll", command=on_button_click, padx=10, pady=10)
button.pack()

# Запуск приложения
root.mainloop()

#pyinstaller --onefile --windowed C:\github\Black-Raid-WiZ\Scripts\main.py