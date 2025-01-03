from textblob import TextBlob

class ChatBot:
    def __init__(self):
        self.sentiment_analyzer = TextBlob("")

    def start_chat(self):
        print("ChatBot: Hi, how can I help you?")
        while True:
            user_message = input("You: ").strip()

            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            if sentiment_score > 0:
                chatbot_message = f"ChatBot: That's great to hear! \n Sentiment score: {sentiment_score}\n"
            elif sentiment_score < 0:
                chatbot_message = f"ChatBot: I'm sorry to hear that. Can you elaborate on the issue?\n Sentiment score: {sentiment_score}\n"
            else:
                chatbot_message = f"ChatBot: Hmm, I see. \n Sentiment score: {sentiment_score}\n"

            print(chatbot_message)


if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()
