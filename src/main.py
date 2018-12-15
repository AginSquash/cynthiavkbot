from random import randint

import TokenFile #Here your Token
import Lib
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token=TokenFile.token)

def getAnswer():
    return Lib.AnswersLib[randint(0, Lib.AnswersCount)]

def main():
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button(Lib.KeyboardLib[randint(0, Lib.KeyboardCount)], color=VkKeyboardColor.POSITIVE)
            vk.messages.send(
                user_id=event.user_id,
                keyboard=keyboard.get_keyboard(),
                message=getAnswer()
                )

if __name__ == '__main__':
    main()