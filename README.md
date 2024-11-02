## KISAN MITRA CHAT BOT (किसान मित्र चैटबॉट)

Kisan Mitra is an AI-powered chatbot designed to assist users with their farming-related questions. Whether you're a seasoned farmer or a beginner, Kisan Mitra provides instant replies and expert advice tailored to the agricultural field.

## Key Features

- **Farming Expertise**: Get answers to a wide range of farming questions, including crop selection, pest management, soil health, and more.
- **Instant Responses**: Receive real-time assistance and information, helping you make informed decisions quickly.
- **User-Friendly Interface**: Engage in a seamless chat experience that is easy to navigate and understand.

## Use Cases

- **Crop Management**: Ask questions about best practices for planting, growing, and harvesting different crops.
- **Pest Control**: Get advice on identifying pests and implementing effective control measures.
- **Soil Health**: Inquire about soil testing, nutrient management, and improving soil quality.
- **Weather Information**: Stay updated with weather forecasts that affect farming activities.
![image](https://github.com/user-attachments/assets/70a0b714-229e-4a5a-a2d6-8e3ce2ed78e1)
![image](https://github.com/user-attachments/assets/bd625748-31cc-4507-90f5-dba583c601eb)
![image](https://github.com/user-attachments/assets/c1f419a2-a52d-46da-a45e-a77e70abe346)

## Technologies Used

- **Django**: The web framework used to build the application.
- **Django Channels**: Enables WebSocket support for real-time communication.
- **Python**: The programming language used for implementing the chatbot logic.
- **JavaScript**: For client-side WebSocket connection and interaction.

## Instruction To Run The Project

1. Clone the project or directly download the project
   ```bash
   git clone https://github.com/incredible-India/Agriculture-Chat-Bot.git

2. Now install the follwing packages using pip
   ```bash
    pip install django channels uvicorn wsproto whitenoise groq
3. Once Project Downloaded or cloned then locate directory where manage.py file there
   ![image](https://github.com/user-attachments/assets/cbb6f12e-225b-4b91-a7ed-7339363003e4)

4. Open the terminal in same directory (manage.py) and write follwing command
   ```bash
   python -m uvicorn KisanFriend.asgi:application --host 127.0.0.1 --port 8000
5. Go to the browser and type the url http://127.0.0.1:8000/

## More Info 
- contact at 8604470501
   

