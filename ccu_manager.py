"""
    디스코드 사용자 관리 클래스
"""


def get_ccu_manager():
    return CCUManager()


class CCUManager():
    def __new__(cls):
        if not hasattr(cls, "_instance"):         # CCUManager 클래스 객체에 _instance 속성이 없다면
            cls._instance = super().__new__(cls)  # CCUManager 클래스의 객체를 생성하고 _instance로 바인딩
            print("CCUManager created\n")
        return cls._instance                      # _instance를 리턴

    # 아직은 초기화할 목록이 없다.
    #def __init__(self, data):
    #    cls = type(self)
    #    if not hasattr(cls, "_init"):             # Foo 클래스 객체에 _init 속성이 없다면


    def update_user(self, user_uid_, user_):
        self.users[user_uid_] = user_


    def remove_user(self, user_uid_):
        data = self.get_user(user_uid_)
        if data is None:
            print("Failed to remove user data, user_uid : {i}".format(i=user_uid_))
            return

        del self.users[user_uid_]


    def get_user(self, user_uid_):
        ret =  self.users.get(user_uid_)
        if ret is None:
            print("Failed to get user data, user_uid : {i}".format(i=user_uid_))
        return ret


    def get_user_num(self):
        i = 0
        for temp in self.users:
            i += 1
        return i


    # 테스트 전용함수로 서비스 로직에서 사용하지 않는다.
    def claer_users(self):
        self.users = {}


    users = {}
