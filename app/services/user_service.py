import json
from config import USERS_DATA_FILE


class UserService:
    def __init__(self):
        self.users_file = USERS_DATA_FILE
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_users(self):
        with open(self.users_file, "w") as f:
            json.dump(self.users, f)

    def increment_counter(self, user_id, username=None):
        user_id_str = str(user_id)
        if user_id_str not in self.users:
            self.users[user_id_str] = {"count": 0}
        if "count" not in self.users[user_id_str]:
            self.users[user_id_str]["count"] = 0
        self.users[user_id_str]["count"] += 1
        self.users[user_id_str]["username"] = username if username else "-"
        self._save_users()

    def get_counter(self, user_id):
        return self.users.get(str(user_id), {}).get("count", 0)

    def get_users_stats(self):
        return [
            {
                "user_id": uid,
                "count": data.get("count", 0),
                "username": data.get("username", "-") or "-"
            }
            for uid, data in self.users.items()
        ]
