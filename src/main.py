from random import randint

import Lib
import TokenFile  # Here your Token
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType, VkLongPoll
from datetime import datetime 
import time
import logging

logging.basicConfig(filename="cynthia_vkbot.log", level=logging.INFO)
logging.info("Start Cynthia! " + str(datetime.now()))

vk_session = vk_api.VkApi(token=TokenFile.token)

def getAnswer():
    return Lib.AnswersLib[randint(0, Lib.AnswersCount)]

def main():
    while True:
        try:
            longpoll = VkLongPoll(vk_session)
            vk = vk_session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button(Lib.KeyboardLib[randint(0, Lib.KeyboardCount)], color=VkKeyboardColor.POSITIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=randint(0, 2147483647),
                        keyboard=keyboard.get_keyboard(),
                        message=getAnswer()
                    )
        except Exception as e:
            logging.error(str(datetime.now()) + " " +str(e))
            time.sleep(30)                


if __name__ == '__main__':
    main()
