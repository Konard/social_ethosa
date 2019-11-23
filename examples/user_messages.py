# -*- coding: utf-8 -*-
# author: Ethosa
# Import what we need
from social_ethosa import Vk, printf

# Declare constant variables
TOKEN = ""

# we authorize through the user
vk = Vk(token=TOKEN, debug=1)

# Start listening for new messages in a separate thread
@vk.on_user_new_message
def get_new_message(msg):
    # Output the received message
    printf(msg)