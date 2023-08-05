from open_ai import OpenAI
import os

# Getting the base directory name for the file to append to the subdirectory files needed
base_dir = os.path.dirname(__file__)

system_text = open(base_dir + '/prompt/system_persona_context.txt').read()
prompt_text = open(base_dir + '/data/api.json').read()

ai = OpenAI(3000, 0)

with open(base_dir + '/output/get_tests_response.txt', 'w') as f:
    f.write(ai.get_tests_response(system_text, prompt_text))

