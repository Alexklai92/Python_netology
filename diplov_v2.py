import time
import requests
import json

TOKEN = '9a30726ddbbf1b0bf8748eff7822a6b3a228157badc24fdde455574b5221ede26d4756703cadc9b6cf13b' #AUTH TOKEN

class User:
    def __init__(self, token, id):
        self.id = id
        self.token = token

    def __repr__(self):
        return f'https://vk.com/id{self.id} {type(self.id)}'

    def default_params(self, user, id):
        return {
            'v': '5.92',
            'access_token': self.token,
            'extended': 1,
            user: id
        }

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': self.token,
            'user_id': self.id,
            'extended': 1
        }

    def get_user_id(self):
        params = self.default_params('user_ids', self.id)
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        user_id = response.json()['response']
        a = user_id[0]['id']
        return a

    def get_groups(self, params):
        print(self.id)
        params = params
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()

    def get_friends(self, params):
        params = params
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        resp_list = response.json()
        friend_list = list()
        for g in resp_list['response']['items']:
            u = User(TOKEN, g)
            friend_list.append(u)
        return friend_list

    def spy_game(self):
        user_id = self.get_user_id()
        f_list = self.get_friends(self.default_params('user_id', user_id))
        count = 0
        self.user = user
        a = user.get_groups(self.default_params('user_id', user_id))['response']['items']
        #print(a)
        unic_group = list()
        friends_group = set()
        for j in a:
            unic_group.append(j['id'])
        print(unic_group)
        for i in f_list:
            print('i =',i.get_groups(self.default_params('user_id', id)))
            try:
                for g in i.get_groups(self.default_params('user_id', self.id))['response']['items']:
                   print(g)
                   count = count + 1
                   friends_group.add(g['id'])
                   #print('1', friends_group)
                   b = set.difference(set(unic_group), set(friends_group))
                   #print(b)
            except KeyError:
                print('error')
                print('')
            finally:
                time.sleep(1)
        print(b)

####483667681
#spy_id = input()
#user = User(TOKEN, spy_id)
user = User(TOKEN, 'arr_karo')
#print(user.get_groups(user.default_params('user_id', user.get_user_id())))
#print(user)
user.spy_game()