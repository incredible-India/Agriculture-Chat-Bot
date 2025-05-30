from channels.generic.websocket import WebsocketConsumer
import json
import ChatWithKisan.savingChatInDB as savingChatInDB
from groq import Groq

client = Groq(
    api_key="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"
)

class ConnectTOBot(WebsocketConsumer):
    def connect(self):
        print("connection done from client")
        self.accept()
        self.send(json.dumps({"message": "Hi I am Kisan`s Friend!! Ask Me any question.."}))

    def receive(self, text_data=None, bytes_data=None):
        try:
            # Assuming text_data is a plain string message
            user_message = text_data
            print("Received message from client:", json.loads(user_message)["message"],type(user_message))
            chat_completion = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": json.loads(user_message)["message"],
                }],
                model="llama3-8b-8192",
            )

            ai_response = chat_completion.choices[0].message.content
            self.send(json.dumps({'message': ai_response}))

            try:
                isUserLogedIn = savingChatInDB.CheckingForTheUserLogin()
                if isUserLogedIn:
                    savingChatInDB.SaveChatHistoryInDBSaved(user_message, ai_response)
                else:
                    print("User not logged in")
            except Exception as e:
                print("Error in checking user login status or saving chat:", e)

        except Exception as e:
            print("Error in processing chat message:", e)
            self.send(json.dumps({'message': 'Sorry, something went wrong.'}))

    def disconnect(self, code):
        print("Client Disconnected")
        super().disconnect(code)
