from pyautogui import *
import pyautogui
import time
import keyboard
import schedule
import logging
import success
import fail

time.sleep(1)

def menu():
    print("Module")
    print("1. Veve")
    print("2. Exit Program\n")
    selection=int(input("Enter choice: "))
    if selection==1:
        print("")

        scheduled = input("Release time (ex. 11:59:59): ")

        while keyboard.is_pressed('q') == False:

            def script():
                logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s:%(msecs)03d] \t%(message)s',datefmt='%H:%M:%S')
                logging.info('Live! Attempting Reservation') #live
                pyautogui.click(505,650)

                while 1:
                    if pyautogui.locateOnScreen('reserving.png', region=(0,0,749,1199), confidence=0.6) != None:
                        logging.info('Reservation in Progress...') #in progress
                    elif pyautogui.locateOnScreen('balance.png', region=(0,0,749,1199), confidence=0.6) != None:
                        logging.info('Reservation Success!') #success
                        success.send()
                        break
                    elif pyautogui.locateOnScreen('sorry.png', region=(0,0,749,1199), confidence=0.6) != None:
                        logging.info('Reservation Failed!') #fail
                        fail.send()
                        break
                    else:
                        logging.info('Waiting for Reservation...') #fail
                        time.sleep(1)

            schedule.every().day.at(scheduled).do(script)

            while True:
                schedule.run_pending()
       
    else:
        exit

menu()