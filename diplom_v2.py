import time
import requests
import json

TOKEN = '9a30726ddbbf1b0bf8748eff7822a6b3a228157badc24fdde455574b5221ede26d4756703cadc9b6cf13b' #AUTH TOKEN

class User:
    def __init__(self, token, id, user):
        self.id = id
        self.token = token
        if user:
            self.id = self.get_user_id()

    def __repr__(self):
        return f'https://vk.com/id{self.id}'

    def get_user_id(self):
        params = {
            'v': '5.92',
            'access_token': self.token,
            'user_ids': self.id,
        }
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        a = response.json()['response'][0]['id']
        return a

    def get_params(self, id):
        if type(id) == int:
            return {
                'v': '5.92',
                'access_token': self.token,
                'user_id': id,
                'extended': 1
            }

    def get_groups(self):
        params = self.get_params(self.id)
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()

    def get_friends(self):
        params = self.get_params(self.id)
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        resp_list = response.json()
        friend_list = list()
        for g in resp_list['response']['items']:
            a = User(TOKEN, g, False)
            friend_list.append(a)
        return friend_list

    def spy_game(self):
        f_list = self.get_friends()
        self.user = user
        a = user.get_groups()['response']['items']
        #print(f_list)
        #print(a)
        unic_group, friend_group = set(), set()
        for i in a:
            unic_group.add(i['id'])
        #print('unic group = ', unic_group)
        for j in f_list:
            print('j = ', j)
            try:
               for id_f in j.get_groups()['response']['items']:
                   er = id_f
                   print('er =', er)
                   friend_group.add(id_f['id'])
            except KeyError:
                print('Key error')
                time.sleep(1)
                print('Ошибка 2: ', j.get_groups())

        print(set.difference(unic_group, friend_group))
user = User(TOKEN, 'arr_karo', True)
user.spy_game()