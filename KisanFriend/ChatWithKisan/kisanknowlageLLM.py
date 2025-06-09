import random
from llm_core import LLMEngine
from gov_knowledge_base import AgricultureKnowledgeBase

class LLMEngine:
    def generate_answer(self, question: str, context: str) -> str:
        prefixes = [
            "Here's what I found:",
            "Based on your question:",
            "This may help you:",
            "According to available government info:"
        ]
        return f"{random.choice(prefixes)}\n👉 {context}"
# Simulated responses based on real government agriculture site topics

class AgricultureKnowledgeBase:
    def __init__(self):
        self.data = {
            "pm-kisan": "PM-KISAN provides ₹6000 per year in three installments to eligible farmers.",
            "soil-health": "Soil Health Card helps farmers understand soil nutrients and fertility status.",
            "crop-advice": "For Kharif season, suitable crops are paddy, maize, and millet. For Rabi, wheat and chickpea.",
            "weather": "As per IMD, rainfall is expected in the next 5 days in northern India.",
            "kcc": "Kisan Credit Card allows farmers to get timely credit with low interest rates for their agricultural needs."
        }

    def search(self, query: str) -> str:
        q = query.lower()
        if "pm-kisan" in q or "income support" in q:
            return self.data["pm-kisan"]
        elif "soil" in q or "health card" in q:
            return self.data["soil-health"]
        elif "crop" in q or "plant" in q:
            return self.data["crop-advice"]
        elif "weather" in q or "rain" in q:
            return self.data["weather"]
        elif "loan" in q or "kcc" in q or "credit" in q:
            return self.data["kcc"]
        else:
            return "Sorry, I couldn't find relevant information in the knowledge base."

class KisanLLMChatbot:
    def __init__(self):
        self.llm = LLMEngine()
        self.kb = AgricultureKnowledgeBase()

    def greet(self):
        print("🌱 Welcome to Kisan Assistant - Your AI farming guide.")
        print("You can ask about crop suggestions, government schemes, loans, and weather updates.")

    def get_input(self):
        return input("\n❓ Your question (type 'exit' to quit): ")

    def run(self):
        self.greet()
        while True:
            question = self.get_input()
            if question.lower() in ["exit", "quit"]:
                print("\n👋 Thank you for using Kisan Assistant. Goodbye!")
                break

            context = self.kb.search(question)
            answer = self.llm.generate_answer(question, context)
            print(f"\n🤖 {answer}")

if __name__ == "__main__":
    bot = KisanLLMChatbot()
    bot.run()
