class User:
    """
    Class that generates new instances of user
    """

    user_detail = [] # Empty user detail list

    def save_user(self):

        User.user_detail.append(self) #Save user's info

    def __init__(self,username,email,password):
        
        # docstring removed for simplicity
    self.username = username
        self.email = email
        self.password = password