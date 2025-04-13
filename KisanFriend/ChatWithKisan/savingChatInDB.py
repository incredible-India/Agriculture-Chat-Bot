import os
import django
from .globalState import globalinfo
# Set the Django settings module path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KisanFriend.settings")

# Setup Django
django.setup()

from ChatWithKisan.models import User, ChatHistory
def CheckingForTheUserLogin():
    print(globalinfo["user_name"] ,
            globalinfo["user_email"] )

    if globalinfo["user_name"] is not None:
        print("User is logged in")
        return True
    else:
        return False




def SaveChatHistoryInDBSaved(QuestionText, AiResponseText):

    user_name = globalinfo['user_name']
    user_email = globalinfo['user_email']
    if user_email is not None and user_name is not None:
        user = User.objects.filter(name=user_name, email=user_email).first()
        print("saving user is",user)
        if user:
            ChatHistory.objects.create(
                user=user,
                message=QuestionText,
                response=AiResponseText
            )
            return True
        else:
            pass
    else:
        return False
