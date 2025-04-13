from channels.generic.websocket import WebsocketConsumer
import json
import os
import ChatWithKisan.savingChatInDB as savingChatInDB
from groq import Groq

client = Groq(
    api_key="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"
)
class ConnectTOBot(WebsocketConsumer):
    def connect(self):
        
        print("connection done from client")
        self.accept()
        self.send(json.dumps({"message" : "Hi I am Kisan`s Friend!! Ask Me any question.."}))
    

    def receive(self, text_data=None, bytes_data=None):
        

        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{ text_data}",
        }
            ],
    model="llama3-8b-8192",
        )
        self.send(json.dumps({'message':f" {chat_completion.choices[0].message.content}"}))
        print("usercheck")
        try:
            isUserLogedIn= savingChatInDB.CheckingForTheUserLogin()
            print("usercheck try")
            if isUserLogedIn:
                print("usercheck login")
                QuestionText = text_data
                AiResponseText = chat_completion.choices[0].message.content
                savingChatInDB.SaveChatHistoryInDBSaved(QuestionText, AiResponseText)
            else:
                print("no logged")
        except Exception as e:
            print("Error in checking user login status", e)
            isUserLogedIn=False


        return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        print("Client Disconnected")
        self.disconnect(code)




        
