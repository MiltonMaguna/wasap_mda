import requests

from credenciales import TOKEN


def main():
    url = 'https://api.telegram.org/bot6560420240:AAEszg_dOFwcBYRlYmhZWSJnpYqLwqo9slA/sendMessage'
    id = '-1002021330172'  # group id
    text = 'Primer mensaje desde Python!'
    params = {'chat_id': id, 'text': text}
    method = 'sendMessage'

    return requests.post(url, params=params)


def telegram_bot_sendtext(bot_message):

    bot_token = TOKEN
    bot_chatID = '1671340058'  # lola mda bot
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
        bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if __name__ == '__main__':
    # test = telegram_bot_sendtext("Testing Telegram bot")
    # print(test)
    print(main())
