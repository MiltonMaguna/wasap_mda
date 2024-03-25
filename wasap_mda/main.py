import requests

from credenciales import TOKEN, GROUP_ID, LOLA_MD_BOT_ID


def main():
    method = 'sendMessage'
    url = f'https://api.telegram.org/bot{TOKEN}/{method}'
    id = GROUP_ID
    text = 'Primer mensaje desde Python!'
    params = {'chat_id': id, 'text': text}

    return requests.post(url, params=params)


def telegram_bot_sendtext(bot_message):

    bot_token = TOKEN
    bot_chatID = LOLA_MD_BOT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
        bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if __name__ == '__main__':
    # test = telegram_bot_sendtext("Testing Telegram bot")
    # print(test)
    print(main())
