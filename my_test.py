"""
    TDD 를 위한 unittest
"""

import unittest
import ccu_manager
from user import User

class MyTest(unittest.TestCase):
    # 유저의 정보를 관리한다.
    def test_update_discord_user(self):
        manager = ccu_manager.get_ccu_manager()
        manager.update_user(123456, User())
        self.assertEqual(1,
                         manager.get_user_num())

        # 누적되는지 확인.
        manager.update_user(123458, User())
        self.assertEqual(2,
                         manager.get_user_num())

        # 갱신되는지 확인.
        manager.update_user(123458, User())
        self.assertEqual(2,
                         manager.get_user_num())


    def test_get_discord_user(self):
        manager = ccu_manager.get_ccu_manager()
        manager.claer_users()

        # 설정한 정보가 일치하는지 확인한다.
        user = User()
        user.a = 3
        manager.update_user(123456, user)
        user2 = manager.get_user(123456)
        self.assertEqual(3, user2.a)


    def test_remove_discord_user(self):
        manager = ccu_manager.get_ccu_manager()
        manager.claer_users()

        manager.update_user(123456, User())
        self.assertEqual(1,
                         manager.get_user_num())

        # 누적되는지 확인.
        manager.update_user(123458, User())
        self.assertEqual(2,
                         manager.get_user_num())

        # 삭제되는지 확인.
        manager.remove_user(123458)
        self.assertEqual(1,
                         manager.get_user_num())


    #def test_timeout_discord_user(self):
    #    self.assertEqual(1,0)



    # 어떻게 분산처리를 하지?
    # 일단 유저 여러명이 처리가 가능하게 한다.
    # I/O 가 blocking 되는것과 같은 원리로 처리하던지 한다.

    # 메세지 파싱부분.
    # UI 와 같은 형식으로 메세지를 만들기 떄문에 이 테스트는 적절하지 않다.
    #def message_parser_test(self):
    #    parser = MessageParser()
    #    data = parser.parse_first_bonus_book_to_data("123")
    #    self.assertEqual(1,0)


# 쓰레드가 잘 생성되고 죽는 지 확인해야함.
if __name__ == '__main__':
    unittest.main()
#unittest.main()
