from flaskext.mysql import MySQL
import json

class Account(object):
    def __init__(self, name: str, userid: int, password: str, role: str, loginid: str) -> None:
        self.name = name
        self.userid = userid
        self.password = password
        self.role = role
        self.loginid = loginid

    def serialize(self):
        return {
            'name': self.name,
            'userid': self.userid,
            'role': self.role,
            'loginid': self.loginid,
        }

class AccountDao(object):
    def list_accounts(self, mysql: MySQL):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT userid, name,password,role,loginid FROM user")
        result = cur.fetchall()
        return self.array_to_account(result)

    def array_to_account(self, arr):
        accounts = []
        if arr: # check if array is not empty
            for tup in arr:
                account = Account(tup[1], tup[0], tup[2], tup[3], tup[4])
                accounts.append(account)
        return accounts
