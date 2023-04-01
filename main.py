#----------------------------------------------------------------#
#-by- Фантэйззu
#version 2.0 beta
#----------------------------------------------------------------#
from pypresence import Presence
from time import time, sleep
import random, os, sys, json, re
import urllib.request

response = urllib.request.urlopen("https://raw.githubusercontent.com/FunTa3y/simple-anime-drp/main/version.txt")
gitversion = response.read().decode('utf-8').strip()
version = "2.1 beta"


with open('config.json', 'r', encoding="utf8") as f:
    config = json.load(f)

buttons = []  # список кнопок по умолчанию пустой

if not config['ViewedAnimeLink'].startswith(('https://', 'http://')):
    print('Еррорка: ссылка на список аниме должна начинаться с https:// или http://')
else:    
    buttons.append({"label": "Список просмотренных аниме", "url": config['ViewedAnimeLink']})


if config['ViewedAnime'] != "": #Если кол-во аниме не пустое значение 
    if config['ViewedAnime'].isdigit(): #И это число
        intuseranime = config['ViewedAnime'] #Тогда мы согласны
    else:    
        print('Еррорка: Значение должно быть цифрой') #Если это не число
        intuseranime = "NaN"
else:
    intuseranime = "?" #Если там пусто


RPC = Presence((config['appid']))
RPC.connect()
RPC.update( #При запуске и без указания параметров aN Ставим такой drp
        details="Выбираю аниме",
        state="Просмотренно: "+ intuseranime +" Аниме", 
        large_image="wait",
        small_image="paused",
        large_text="ANIME IS MY LIFE",
        small_text="Выбираю Аниме",
        buttons=buttons
    )
print("\n\n █████╗ ███╗   ██╗██╗███╗   ███╗███████╗              ██████╗ ██████╗ ██████╗ \n██╔══██╗████╗  ██║██║████╗ ████║██╔════╝              ██╔══██╗██╔══██╗██╔══██╗\n███████║██╔██╗ ██║██║██╔████╔██║█████╗      █████╗    ██║  ██║██████╔╝██████╔╝\n██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══╝      ╚════╝    ██║  ██║██╔══██╗██╔═══╝ \n██║  ██║██║ ╚████║██║██║ ╚═╝ ██║███████╗              ██████╔╝██║  ██║██║     \n╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝              ╚═════╝ ╚═╝  ╚═╝╚═╝     \n                                  Версия: "+ version +"\n                                  -by- Фантэйззи\n\n")
if gitversion != version:
    print("Похоже ваша версия устарела, Актуальная версия: " + gitversion + "\nПожалуйста обновите программу\n https://github.com/FunTa3y/simple-anime-drp \n ")
#!Параметры aN
NameOfAnime = input("Название: ")
NameOfCover = input("Название обложки: ")
LinkToAnime = input("Ссылка на аниме: ")
NumberOfEpisode = input("Номер эпизода: ")
TimeOfEpisode = (int(input("Время серии: ")) - 2) * 60 - random.randint(0, 32)
################################ просто время
start_time = time() #определение start_time
total_time = TimeOfEpisode  #сохраняем общее время серии в переменной

if config['appid'] == "1090959676281212949":#Если используется обычный appid тогда пользуемся этим алгоритмом
    NameOfCover = re.sub(r'[^a-zA-Z\s]', '', NameOfCover)
    NameOfCover = NameOfCover.lower().replace(' ', '')

if not LinkToAnime.startswith(('https://', 'http://')): #Если это не ссылка тогда
    print('Еррорка: ссылка на аниме должна начинаться с https:// или http://') #ОШибка
else:
    buttons.append({"label": "Ссылка на аниме", "url": LinkToAnime})

while True:
    #возможность поставить на паузу и продолжить
    is_paused = False
    while True:
        # показываем информацию о просмотре, #!(Пауза)
        if is_paused:
            RPC.update(
                details="Аниме: " + NameOfAnime,
                state="Серия: " + NumberOfEpisode + " (Пауза)",
                large_image=NameOfCover,
                small_image="paused",
                large_text=NameOfAnime + " (Пауза)",
                small_text="Пауза",
                buttons=buttons
            )
        else: #!Воспроизведение
            RPC.update(
                details="Аниме: " + NameOfAnime,
                state="Серия: " + NumberOfEpisode,
                end=time() + TimeOfEpisode,
                large_image=NameOfCover,
                small_image="play",
                large_text=NameOfAnime,
                small_text="Смотрю",
                buttons=buttons
                
            )

        # проверяем, если время серии закончилось
        if TimeOfEpisode <= 0:
            NumberOfEpisode = str(int(NumberOfEpisode) + 1)
            TimeOfEpisode = total_time  # обновляем время серии
            if (config['autopause']) == True: #Если включена автопауза
                is_paused = True #Тогда по завершении серии ставим паузу
                print("Продолжить?   " + NumberOfEpisode + " Серия")
                break
            else:
                break

        # ожидаем ввода команды для паузы или возобновления
        command = input("Enter - Продолжить/Поставить на паузу, s - Следующая серия, n - Cменить аниме/настройки: ")
        if command == "s":
            NumberOfEpisode = str(int(NumberOfEpisode) + 1)
            TimeOfEpisode = total_time  # обновляем время серии
            print("--> Серия:" + NumberOfEpisode + "\n")
            break
        elif command == "":
            is_paused = not is_paused  # меняем состояние паузы
            if is_paused:
                # сохраняем оставшееся время серии при паузе
                TimeOfEpisode = TimeOfEpisode - (time() - start_time)
                print("--> Пауза\n")
            else:
                start_time = time()  # сохраняем время возобновления просмотра
                print("--> Воспроизведение \n")
                break
        elif input() == "n":
            print("--> OK")
            sleep(2)
            RPC.close()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            continue
