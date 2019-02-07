import json

import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(from_text, to_text,
                 from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(from_text) as f:
        text = f.read()



    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(to_text, 'w', encoding='utf-8') as w:
        w.write(''.join(json_['text']))

    return ''.join(json_['text'])


print(translate_it('FR.txt', 'test_2.txt', 'fr'))


#requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
