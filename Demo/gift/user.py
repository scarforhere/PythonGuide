# coding: utf-8
"""
-------------------------------------------------
   File Name：     user
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-06 09:41 AM
-------------------------------------------------
Description : 

    1.  user类的初始化
    2.  get_user（时间的转变）
    3.  查看奖品列表
"""
import os
import random
from base import Base
from Demo.gift.common.utils import timestamp_to_string
from Demo.gift.common.error import NotUserError, RoleError, UserActiveError, CountError


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()
        self.gift_random = list(range(1, 101))

    def get_user(self):
        users = self._Base__read_users()
        if self.username not in users:
            raise NotUserError(f'not user {self.username}')

        current_user = users.get(self.username)

        if current_user.get('active') == False:
            raise UserActiveError(f'the user {self.username} had not use')

        if current_user.get('role') != 'normal':
            raise RoleError('you are not normal user')

        self.user = current_user
        self.name = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get('create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_lists = []

        for level_one, level_one_pool in gifts.items():
            for level_two, level_two_pool in level_one_pool.items():
                for gift_name, gift_info in level_two_pool.items():
                    gift_lists.append(gift_info.get('name'))
        return gift_lists

    def choice_gift(self):
        self.get_user()
        # level1 get
        first_level, second_level = None, None
        level_one_count = random.choice(self.gift_random)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51 <= level_one_count <= 80:
            first_level = 'level2'
        elif 81 <= level_one_count < 95:
            first_level = 'level3'
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise CountError('level_one_count need 0~100')

        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level)

        level_two_count = random.choice(self.gift_random)
        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81 <= level_two_count < 95:
            second_level = 'level2'
        elif 95 <= level_two_count < 100:
            second_level = 'level3'

        else:
            raise CountError('level_one_count need 0~100')

        level_two = level_one.get(second_level)

        gift_names = []
        for k, _ in level_two.items():
            gift_names.append(k)

        if len(level_two) == 0:
            print('可惜 您没有中奖')
            return

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') == 0:
            print('可惜 您没有中奖')
            return
        gift_info['count'] -= 1

        level_two[gift_name] = gift_info
        level_one[second_level] = level_two
        gifts[first_level] = level_one

        self._Base__save(gifts, self.gift_json)

        self.user['gifts'].append(gift_name)
        self.update()
        print(f'恭喜您 获得 {gift_name}')

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user

        self._Base__save(users, self.user_json)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    user = User('song', user_path, gift_path)
    user.choice_gift()
