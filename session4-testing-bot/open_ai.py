import os
import openai
import json

api_key = os.getenv("OPENAI_KEY")
MODEL = "gpt-3.5-turbo-0613"
FREQUENCY_PENALTY = 1
TOP_P = 1
PRESENCE_PENALTY = 1


class OpenAI:
    def __init__(self, _max_tokens, _temperature):
        openai.api_key = api_key
        self.max_tokens = _max_tokens
        self.temperature = _temperature

    def generate_response(self, _prompt):
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": _prompt
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=TOP_P,
            n=1,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )

        return response["choices"][0]["message"]["content"]

    def generate_multiple_responses(self, _prompt, _num_responses):
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": _prompt
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=TOP_P,
            n=_num_responses,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )

        return response["choices"][i]["message"]["content"]

    def generate_response_with_functions(self, _prompt):
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": _prompt
                }
            ],
            functions=[
                {
                    "name": "get_response",
                    "description": "List of options for the prompt asked",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "options": {
                                "type": "array",
                                "description": "Option list",
                                "items": {
                                    "type": "string",
                                    "description": "Option for the prompt asked in the question"
                                },
                            }
                        },
                        "required": ["options"]
                    }
                }
            ],
            function_call={"name": "get_response"},
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=TOP_P,
            n=1,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )

        return response

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


# Test openai
if __name__ == '__main__':

    max_tokens = 5
    temperature = 0.5

    ai = OpenAI(max_tokens, temperature)

    # Testing single reply
    print('-' * 10 + 'TESTING SINGLE RESPONSE')
    prompt = 'From the '
    print(ai.generate_response(prompt))

    # Testing multiple replies
    num_responses = 3
    print('-' * 10 + 'TESTING MULTIPLE RESPONSES')
    for i in range(num_responses):
        print('Response #' + str(i))
        prompt = 'The name of best rated Dosa restaurant in Bengaluru is '

        print(ai.generate_multiple_responses(prompt, num_responses))

    max_tokens = 2048
    temperature = 0.5
    ai = OpenAI(max_tokens, temperature)
    # Testing function call response
    print('-' * 10 + 'TESTING FUNCTION CALL RESPONSE')
    prompt = 'Name and Address of the 10 best dosa restaurants in Bangalore'
    res = ai.generate_response_with_functions(prompt)
    choices = res['choices'][0]['message'].to_dict()['function_call']['arguments']
    choices = json.loads(choices)
    for choice in choices['options']:
        print(choice)
