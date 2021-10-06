class Types:
    def get_user_type(self, user_type):
        """Returns a random key for user type."""
        user_type_dict = {'admin': 1, 'user': 2}
        if type(user_type).__name__ == 'int':
            for key, value in user_type_dict.items():
                if value == user_type:
                    return key
        if user_type_dict.get(user_type):
            return user_type_dict[user_type]
        return 0

    def get_status(self, status):
        """Returns a random key for status type."""
        status_dict = {'pending': 1, 'active': 2, 'deactivate': 3, 'deleted': 4}
        if type(status).__name__ == 'int':
            for key, value in status_dict.items():
                if value == status:
                    return key

        if status_dict.get(status):
            return status_dict[status]
        return 0

    def get_priority(self, priority):
        """Returns a random key for priority type."""
        priority_dict = {'low': 1, 'medium': 2, 'high': 3}
        if type(priority).__name__ == 'int':
            for key, value in priority_dict.items():
                if value == priority:
                    return key
        if priority_dict.get(priority):
            return priority_dict[priority]
        return None

