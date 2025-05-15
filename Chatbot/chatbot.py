import json

class ChatBot:
    def __init__(self, knowledge_file="knowledge.json"):
        self.knowledge_file = knowledge_file
        try:
            with open(self.knowledge_file, "r") as file:
                self.knowledge = json.load(file)
        except FileNotFoundError:
            self.knowledge = {}

    def save_knowledge(self):
        with open(self.knowledge_file, "w") as file:
            json.dump(self.knowledge, file, indent=4)

    def get_response(self, question):
        question = question.lower()
        if question in self.knowledge:
            return self.knowledge[question]
        else:
            print("No tengo una respuesta para eso. ¿Cuál debería ser la respuesta?")
            response = input("Tu respuesta: ")
            self.knowledge[question] = response
            self.save_knowledge()
            return "Gracias, ahora lo recordaré."

def main():
    bot = ChatBot()
    print("¡Hola! Soy tu chatbot. Pregúntame algo (escribe 'salir' para terminar).")
    while True:
        question = input("Tú: ")
        if question.lower() == "salir":
            print("¡Adiós!")
            break
        response = bot.get_response(question)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()