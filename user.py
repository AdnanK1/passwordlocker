class User:
    """
    Class that generates new instances of user
    """

    user_detail = [] # Empty user detail list

    

    def __init__(self,email,password):
        
        # docstring removed for simplicity
        self.email = email
        self.password = password