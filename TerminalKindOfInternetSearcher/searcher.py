import webbrowser
import re
call = input('Введите ссылку или запрос: ')
if re.search(r'\.', call):
    webbrowser.open_new_tab('https://' + call)
elif re.search(r'\ ', call):
    webbrowser.open_new_tab('https://yandex.ru/search/?text='+call)
else:
    webbrowser.open_new_tab('https://yandex.ru/search/?text=' + call)