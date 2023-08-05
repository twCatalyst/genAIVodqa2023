import os
import openai
import json

api_key = os.getenv("OPENAI_KEY")
MODEL = "gpt-3.5-turbo-16k-0613"
FREQUENCY_PENALTY = 1
TOP_P = 1
PRESENCE_PENALTY = 1


class OpenAI:
    def __init__(self, _max_tokens, _temperature):
        openai.api_key = api_key
        self.max_tokens = _max_tokens
        self.temperature = _temperature


    def get_tests_response(self, system_text, prompt_text):
        # Create a new chat session
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': system_text
                },
                {
                    'role': 'user',
                    'content': prompt_text
                }
            ]
        )

        # Parse the response
        return response['choices'][0]['message']['content']

    def get_test_scenarios_and_data(self, system_text, prompt_text):
        # Create a new chat session
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': system_text
                },
                {
                    'role': 'user',
                    'content': prompt_text
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=1,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )

        # Parse the response
        return response['choices'][0]['message']['content']

