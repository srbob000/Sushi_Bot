import win32api, win32con
from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *

"""
All coordinates assume a screen resolution of 1920 x 1080.
The play area is centered to the bottom of the windows start
menu bar
x_pad = 608
y_pad = 554
Play area =  x_pad+1, y_pad+1, 1248, 1030
"""

x_pad = 608
y_pad = 554

class Blank:
    seat_1 = 2612
    seat_2 = 8448
    seat_3 = 8945
    seat_4 = 5702
    seat_5 = 8045
    seat_6 = 7230

sushiTypes = {1277:'onigiri',
              1921:'caliroll',
              1284:'gunkan',}

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

class Cord:
    f_shrimp = (34, 332)
    f_rice = (88, 333)
    f_nori = (23, 390)
    f_roe = (95, 394)
    f_salmon = (33, 341)
    f_unagi = (91, 443)

    phone = (587, 350)

    menu_toppings = (524, 271)
    t_shrimp = (494, 218)
    t_nori = (491, 275)
    t_roe = (576, 277)
    t_salmon = (490, 323)
    t_unagi = (575, 218)
    t_exit = (595, 330)

    menu_rice = (514, 291)
    buy_rice = (552, 276)

    delivery_norm = (491, 294)

def clear_tables():
    mousePos((81, 205))
    leftClick()

    mousePos((181, 207))
    leftClick()

    mousePos((282, 207))
    leftClick()

    mousePos((380, 205))
    leftClick()

    mousePos((486, 207))
    leftClick()

    mousePos((588, 207))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print ('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        print ('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def buyFood(food):

    mousePos(Cord.phone)

    mousePos(Cord.menu_toppings)

    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)

    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)

    mousePos(Cord.delivery_norm)

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print ('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print ('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (101, 13, 13):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'salmon':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_salmon) != (127, 71, 47):
            print ('salmon is available')
            mousePos(Cord.t_salmon)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['salmon'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('salmon is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'shrimp':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_shrimp) != (127, 71, 47):
            print ('shrimp is available')
            mousePos(Cord.t_shrimp)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['shrimp'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('shrimp is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'unagi':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_unagi) != (94, 49, 8):
            print ('unagi is available')
            mousePos(Cord.t_unagi)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['unagi'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('unagi is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print ('%s is low and needs to be replenished' % i)
                buyFood(i)

def foldMat():
    mousePos((243, 435))
    leftClick()
    time.sleep(.1)

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 476)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+476)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)

def get_seat_one():
    box = (654, 605, 654 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    box = (755, 605, 755 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (857, 605, 857 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (957, 605, 957 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (1058, 605, 1058 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (1159, 605, 1159 + 21, 605 + 21)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    ##im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print
            'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print
            'sushi not found!\n sushiType = %i' % s1

    else:
        print
        'Table 1 unoccupied'

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print
            'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print
            'sushi not found!\n sushiType = %i' % s2

    else:
        print
        'Table 2 unoccupied'

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print
            'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print
            'sushi not found!\n sushiType = %i' % s3

    else:
        print
        'Table 3 unoccupied'

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print
            'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print
            'sushi not found!\n sushiType = %i' % s4

    else:
        print
        'Table 4 unoccupied'

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print
            'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print
            'sushi not found!\n sushiType = %i' % s5

    else:
        print
        'Table 5 unoccupied'

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print
            'table 1 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print
            'sushi not found!\n sushiType = %i' % s6

    else:
        print
        'Table 6 unoccupied'

    clear_tables()

def startGame():
    # location of play button
    mousePos((319, 201))
    leftClick()
    time.sleep(.1)

    # location of continue button
    mousePos((311, 410))
    leftClick()
    time.sleep(.1)

    # location of skip button
    mousePos((561, 452))
    leftClick()
    time.sleep(.1)

    # location of continue button
    mousePos((312, 380))
    leftClick()
    time.sleep(.1)

def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()
