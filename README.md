# Простенький Anime Discord Rich Presence

Простенький Anime Rich Presence написанный на python для отображения текущего аниме в игровой активности

# Установка (.exe файла)
* Распаковать Приложение вместе с конфигом в удобное для вас место 
* Настроить config.json и запустить

# Установка (Через source, python)
* git clone https://github.com/FunTa3y/simple-anime-drp
* Установить зависимости: 
    * `pip install pypresence` - библиотека для отправки RPC статуса
* Настроить config.json
* Запустить main.py

# Инструкция:
#### config.json --> Настройки для программы //Описание настроек
* appid --> ID Приложения для Rich Presence `//Подробнее https://discord.com/developers/applications/ //Рекомендую поставить своё`
* autopause --> Если включено (true) после истечении времени серии ставит воспроизведение DRP на паузу `//Чтобы выключить false`
* viewedanime --> Количество просмотренных аниме `//Используются только числа, можно оставить пустым`
* viewedanimelink --> Ссылка на ваш список аниме `//Используются только ссылки, можно оставить пустым`

#### anime drp.exe --> Сама программа //Описание возможностей
* Название --> Название вашего аниме
* Название обложки --> Название картинки из appid `//Если используется стандартный appid тогда название аниме на английском (поддерживает очень мало аниме)`
* Ссылка на аниме --> Ссылка на аниме что вы смотрите, можно оставить пустым
* Номер эпизода --> Номер серии что вы смотрите
* Время серии --> Время которое длится серия (включая опенинг и эндинг) // `ТОЛЬКО МИНУТЫ желательно добавлять одну минуту p.s. От серии всегда отнимается 2 минуты и 0-30 секунд которые примерно отведены на Эндинг (Я фанат опенингов простите)`
#### //Команды -->
* Enter (пустой текст) --> Ставит воспроизведении DRP на паузу и возобновляет его при повторной команде
* n --> Перезапускает программу
* s --> Меняет серию на следуюущую

# F.A.Q.

##### q> При запуске программа долго запускается, что это?
a> Это тайм-аут от дискорда, просто подождите
 
##### q> Программа сразу закрывается, что делать?
a> Проверьте что в папке где находится программа есть файл config.json
 
##### q> Как сделать это всё автоматизированым?
a> Пока что никак, дойдут руки сделаю расширение для браузера
 
##### q> Как узнавать об апдейтах программы?
a> При запуске программы она автоматически уведомит о устаревшой версии
 
##### q> Программа ничего не отображает в статусе игры, что делать?
a> Проверьте что дискорд запущен, если это не помогло, убедитесь, что статус активности включен в настройках Discord
 
##### q> Ввёл название обложки но картинка не появляется, что делать?
a> Возможно вы ошиблись в написании или этой обложки нет в appid, рекомендуем создать своё appid 
 
##### q> Как мне создать своё appid?
a> https://docs.customrp.xyz/v/ru/setting-up

#### В случае любых ошибок/вопросов в лс 
`Телеграмм: @funtazzy`

`Вконтакте: vk.com/funtazygg`

`Дискорд: Фантэйззu♯uwu#6107 (Врядли замечу вас)`
