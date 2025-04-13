from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from .models import User, ChatHistory
from django.db.models import Q
from ChatWithKisan.globalState import globalinfo 
# Create your views here.
def index(request):
    if request.session.get('user_name'):
        globalinfo["user_name"] = request.session.get('user_name')
        globalinfo["user_email"] = request.session.get('user_email')
        return render(request,"ChatWithKisan/chat.html",{
            "isLogedIn":True,
            "user":request.session.get('user_name'),
        })
    else:
        globalinfo["user_name"] = None
        globalinfo["user_email"] = None
        return render(request,"ChatWithKisan/chat.html",{
            "isLogedIn":False,
            "user":"User"
        })


def login(request):
    if request.method == "GET":
        if request.session.get('user_name'):
            # User is already logged in, redirect to chat page
           return HttpResponseRedirect('/chat')
        else:
            return render(request, "ChatWithKisan/login.html", {
                "isLogedIn": False,
            })
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = User.objects.filter(email=email, password=password).first()
        if user:
            #request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['user_email'] = user.email
            globalinfo["user_name"] = user.name
            globalinfo["user_email"] = user.email
            return render(request, "ChatWithKisan/chat.html", {
                "isLogedIn": True,
                "user": user.name
            })
        else:
            return render(request, "ChatWithKisan/login.html", {
                "isLogedIn": False,
                "invalidCredentials": True
            })

    

def register(request):
    if request.method == "GET":
         if request.session.get('user_name'):
            # User is already logged in, redirect to chat page
           return HttpResponseRedirect('/chat')
         else:
            return render(request, "ChatWithKisan/registration.html", {
                "isLogedIn": False,
            })
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(name, email, password)
        # Save the user to the database
        user = User.objects.filter(Q(name=name) | Q(email=email)).first()
        if user:
            return render(request, "ChatWithKisan/registration.html", {
                "isLogedIn": False,
                "userExist": True
            })
        else:
            user = User.objects.create(name=name, email=email, password=password)
           # request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['user_email'] = user.email
            globalinfo["user_name"] = user.name
            globalinfo["user_email"] = user.email
            return render(request, "ChatWithKisan/chat.html", {
                "isLogedIn": True,
                "user": name
            })
        
def logout(request):
    # Clear the session data
    request.session.flush()
    globalinfo["user_name"] = None
    globalinfo["user_email"] = None
    return HttpResponseRedirect('/chat')


def chatHistory(request):
    print("inside else",globalinfo["user_name"])
    if  globalinfo["user_name"] is not None:
        print("isexist db")
        currentUser = User.objects.filter(Q(name = globalinfo["user_name"]) & Q(email=globalinfo["user_email"])).first()
        print("isexist db",currentUser)
        if currentUser:
            chathistoryList = ChatHistory.objects.filter(user=currentUser)


            print(chathistoryList,"is histry having")
            return render(request,"ChatWithKisan/chatHistory.html",{
                "isLogedIn": True,
                "user": globalinfo["user_name"],
                "chat_history": chathistoryList
            })
        else:
            print("inside else")
            return render(request, "ChatWithKisan/login.html", {
                "isLogedIn": False,
                "invalidCredentials": False
            })
    else:
        print("finasl else")
        return render(request, "ChatWithKisan/login.html", {
                "isLogedIn": False,
                "invalidCredentials": True
            })