import re

class Solution:
    def is_valid_password(self, password: str) -> bool:
        if not re.match(r'^[a-zA-Z0-9_#%]+$', password):
            return False

        if not re.search(r'[0-9]', password):
            return False

        if not re.search(r'[_#%]', password):
            return False

        if len(password) < 8:
            return False

        if not re.search(r'[A-Z]', password):
            return False

        lower = password.lower()
        if lower == lower[::-1]:
            return False

        return True
