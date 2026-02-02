from typing import Dict
from models.address import Address
from models.user import User


class UserService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.users:Dict[str, User] = {}

    def add_user(self, user_id:str, user_name:str, address:Address):
        if user_id in self.users:
            return 'This user is already added.'
        user = User(user_id, user_name, address)
        self.users[user_id] = user
        return user

    def remove_user(self, user_id:str):
        if user_id not in self.users:
            return "This user is not present."
        del self.users[user_id]

    def get_user(self, user_id:str):
        if user_id not in self.users:
            return "This user is not present."
        return self.users.get(user_id)
    
    def get_all_users(self):
        return self.users