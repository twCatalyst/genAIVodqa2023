import os
import openai

api_key = os.getenv("OPENAI_KEY")
MODEL = "gpt-3.5-turbo-0613"
MAX_RESPONSE_TOKENS = 3
TEMPERATURE = 2
FREQUENCY_PENALTY = 1
TOP_P = 1
PRESENCE_PENALTY = 1


# noinspection PyMethodMayBeStatic
class OpenAI:
    def __init__(self, max_tokens, temperature):
        openai.api_key = api_key

    def generate_response(self, _prompt):
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": _prompt
                }
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_RESPONSE_TOKENS,
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
            temperature=TEMPERATURE,
            max_tokens=MAX_RESPONSE_TOKENS,
            top_p=TOP_P,
            n=_num_responses,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )

        return response["choices"][i]["message"]["content"]


# Test openai
if __name__ == '__main__':

    ai = OpenAI()

    # Testing single reply
    print('-'*10 + 'TESTING SINGLE RESPONSE')
    prompt = 'Listen to your heart '
    print(ai.generate_response(prompt))

    # Testing multiple replies
    num_responses = 3
    print('-' * 10 + 'TESTING MULTIPLE RESPONSES')
    for i in range(num_responses):
        print('Response #' + str(i))
        prompt = 'The name of best rated Dosa restaurant in Bengaluru is '

        print(ai.generate_multiple_responses(prompt, num_responses))
