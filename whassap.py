# import pyautogui as pg
# import time
# import webbrowser as web

# web.open('https://web.whatsapp.com/send?phone='+"542223432763")
# mensaje = "holaaaa"
# for i in range(100):
#     pg.write(mensaje)
#     time.sleep(1)
#     pg.press("enter")

import pyautogui as pg
import time
import webbrowser as web
phone_no="+54222432763"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(1)
for i in range(50):
    pg.write('gorda inbecil ')
    pg.press('enter' )
    if i == 20:
        pg.write('AHI VIENE LA SEGUNDA OLEADA DE MENSAJES?)')
        pg.press('enter')
    
    
pg.alert('Bomba de mensajes finalizada')
