# coding: utf-8
"""
-------------------------------------------------
   File Name：     admin
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-06 09:41 AM
-------------------------------------------------
Description : 

    1.  admin类的搭建
    2.  获取档期那用户函数（包含获取身份）
    3.  提娜佳永华（判断是否时管理员）
    4.  冻结与恢复用户
    5.  修改用户身份
    6.  admin验证（只有admin的用户才能使用这个类）
    7.  任何函数都应该动态更新getuser
    8。 奖品的添加
    9.  奖品数量的更新（同步base调整）

"""
import os
from base import Base
from Demo.gift.common.error import NotUserError, UserActiveError, RoleError


class Admin(Base):
    def __init__(self, username, user_jason, gift_jason):
        self.username = username
        super().__init__(user_jason, gift_jason)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user == None:
            raise NotUserError(f'not user {self.username}')

        if current_user.get('active') == False:
            raise UserActiveError(f'the user {self.username} had not use')

        if current_user.get('role') != 'admin':
            raise RoleError('you are not admin')

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def add_user(self, username, role):
        self.__check('permission denied')

        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        self.__check('permission denied')

        self._Base__change_active(username=username)

    def update_user_role(self, username, role):
        self.__check('permission denied')

        self._Base__change_role(username=username, role=role)

    def add_gift(self, first_level, second_level,
                 gift_name, gift_count):
        self.__check('permission denied')

        self._Base__write_gift(first_level=first_level,
                               second_level=second_level,
                               gift_name=gift_name,
                               gift_count=gift_count)

    def delete_gift(self, first_level, second_level,
                    gift_name):
        self.__check('permission denied')

        self._Base__delete_gift(first_level, second_level,
                                gift_name)

    def update_gift(self, first_level, second_level,
                    gift_name, gift_count):
        self.__check('permission denied')

        self._Base__gift_update(first_level=first_level,
                                second_level=second_level,
                                gift_name=gift_name,
                                gift_count=gift_count, is_admin=True)

    def __check(self, message):
        self.get_user()
        if self.role != 'admin':
            raise Exception(message)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    admin = Admin('scar', user_path, gift_path)
    # admin.update_user_role(username='song',role='normal')
    admin.update_user_active('song')
    print(admin.name, admin.role)
