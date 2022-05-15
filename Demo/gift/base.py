# coding: utf-8
"""
-------------------------------------------------
   File Name：     base
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-06 09:41 AM
-------------------------------------------------
Description : 

    1.  导入user.json 文件检查
    2.  导入gift.json 文件检查
    3.  确定用户表中每个用户的信息字段
    4.  读取user.json文件
    5.  写入user.json（检测该用户是否存在），存在则不可写入
        username    姓名
        role normal or admin
        active True or False
        create_time timestamp
        update_time timestamp
        gifts[]

        user:   {username,role,active}
    6.  role的修改
    7.  active的修改
    8.  delete_user
    9.  gifts 奖品结构确定
        {
            lwvel1: {
                level1: {
                    gift_name1: {
                            name: xx
                            count: xx
                                }
                    gift_name2: {
                            name: xx
                            count: xx
                                }
                        }
                    }
        }

    10. gifts 奖品的读取
    11. gifts 添加
    12. gifts 初始化
    13  gifts 修改
    14  gifts 奖品删除
    15. 抽奖函数    随机判断第一层（level1） 1：50%   2：30%   3： 15%  4： 5%
    16. 抽奖函数    随机判断第二层（level2） 1：80%   2：00%   3： 15%  4： 5%
    17. 抽奖函数    获取对应层级的真是奖品，并随机一个奖品，查看奖品的count是否为0
                    不为0       中奖  提示用户    奖品数量-1  为用户更新
                    奖品到user表中的gifts中
                    数量为0    未中奖
    18. 防止并发操作userjson与giftjson
    19， 用__gift_update替代抽奖函数中手动更改奖品数量
    20. 登录体系优化
    21. 获取所有active为False的用户
    22. 每日抽奖次数限制

"""
import json
import os
import time

from common.utils import check_file, timestamp_to_string
from common.consts import ROLES, FIRSTLEVELs, SECONDLEVELs
from common.error import UserExistsError, RoleError, LevelError, NegativeNumerError, CountError


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()

        self.__init_gifts()

    def __check_user_json(self):
        check_file(self.user_json)

    def __check_gift_json(self):
        check_file(self.gift_json)

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())

        if time_to_str == True:
            for username, v in data.items():
                v['create_time'] = timestamp_to_string(v['create_time'])
                v['update_time'] = timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')

        user['active'] = True
        user['create_time'] = time.time()
        user['create_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()

        if user['username'] in users:
            raise UserExistsError(f"username {user['username']} had exists")

        users.update(
            {user['username']: user}
        )

        self.__save(users, self.user_json)

    def __change_role(self, username, role):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        if role not in ROLES:
            raise RoleError(f'not use role {role}')

        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        delete_user = users.pop(username)

        self.__save(users, self.user_json)

        return delete_user

    def __read_gifts(self):
        with open(self.gift_json, 'r') as f:
            data = json.loads(f.read())

        return data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level2': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level3': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level4': {
                'level1': {},
                'level2': {},
                'level3': {}
            }
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return

        self.__save(data, self.gift_json)

    def __write_gift(self, first_level, second_level,
                     gift_name, gift_count):

        if not first_level in FIRSTLEVELs:
            raise LevelError('firstlevel not exist')
        if not second_level in SECONDLEVELs:
            raise LevelError('secondlevel not exist')

        gifts = self.__read_gifts()

        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]

        if gift_count <= 0:
            gift_count = 1

        if gift_name in current_second_gift_pool:
            current_second_gift_pool[gift_name]['count'] += gift_count
        else:
            current_second_gift_pool[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }

        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool

        self.__save(gifts, self.gift_json)

    def __gift_update(self, first_level, second_level,
                      gift_name, gift_count=1, is_admin=False):

        assert isinstance(gift_count, int), 'gift count is not a int'
        data = self.__check_and_getgift(first_level, second_level, gift_name)

        if data == False:
            return data

        current_gift_pool = data.get('level_own')
        current_second_gift_pool = data.get('level_two')
        gifts = data.get('gifts')

        current_gift = current_second_gift_pool[gift_name]

        if is_admin == True:

            if gift_count <= 0:
                raise CountError('gift count should not be 0')

            current_gift['count'] = gift_count

        else:

            if current_gift['count'] - gift_count <= 0:
                raise NegativeNumerError('gift count can not be negative')

            current_gift['count'] -= gift_count

        current_second_gift_pool[gift_name] = current_gift
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool

        self.__save(gifts, self.gift_json)

    def __delete_gift(self, first_level, second_level,
                      gift_name):
        data = self.__check_and_getgift(first_level, second_level, gift_name)

        if data == False:
            return data

        current_gift_pool = data.get('level_own')
        current_second_gift_pool = data.get('level_two')
        gifts = data.get('gifts')

        delete_gift_data = current_second_gift_pool.pop(gift_name)

        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool

        self.__save(gifts, self.gift_json)

        return delete_gift_data

    def __check_and_getgift(self, first_level, second_level,
                            gift_name):

        if not first_level in FIRSTLEVELs:
            raise LevelError('firstlevel not exist')
        if not second_level in SECONDLEVELs:
            raise LevelError('secondlevel not exist')

        gifts = self.__read_gifts()

        current_gift_pool = gifts[first_level]
        current_second_gift_pool = current_gift_pool[second_level]

        if gift_name not in current_second_gift_pool:
            return False

        return {'level_own': current_gift_pool,
                'level_two': current_second_gift_pool,
                'gifts': gifts}

    def __save(self, data, path):
        json_data = json.dumps(data)
        with open(path, 'w') as f:
            f.write(json_data)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    print(gift_path)
    print(user_path)

    base = Base(user_json=user_path, gift_json=gift_path)
    base._Base__write_user(username='sss', role='normal')
    # base.gift_delete(first_level='level1', second_level='level1', gift_name='asdas')
    # print(result)
