import openai
import os

# Set your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=100  # Adjust max tokens as needed
    )
    return response.choices[0].text

def explain_sentiment(text, sentiment):
    explanation_prompt = f"Explain why '{text}' is {sentiment}."
    explanation = chat_with_gpt3(explanation_prompt)
    return explanation

if __name__ == '__main__':
    print(chat_with_gpt3('Write me a poem'))