import random
import webbrowser
list = ["https://uchi.ru/",
"https://ru-ru.facebook.com/",
'https://zen.yandex.ru/',
'https://www.instagram.com/',
'https://www.youtube.com/',
'https://vk.com/feed']
print("1.")
a=random.choice(list)
webbrowser.open_new_tab(a)
cs= "minecraft"
print('i love '+cs)