import os
from typing import List, Tuple
import reflex as rx
import openai
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
openai.api_key = os.getenv('API_KEY_REFLEX')


class State(rx.State):
    # The current question being asked
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples
    chat_history: List[Tuple[str, str]]

    def answer(self):
        session = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = str()
        self.chat_history.append((self.question, answer))
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.question, answer)
                yield
