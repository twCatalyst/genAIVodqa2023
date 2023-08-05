from open_ai import OpenAI
import os

# Getting the base directory name for the file to append to the subdirectory files needed
base_dir = os.path.dirname(__file__)

system_text = open(base_dir + '/prompt/system_persona_test_scenarios_data.txt').read()
prompt_text = open(base_dir + '/prompt/user_prompt_test_scenarios_data.txt').read()

ai = OpenAI(12000, 0)

with open(base_dir + '/output/test_scenarios_and_data.txt', 'w') as f:
    f.write(ai.get_test_scenarios_and_data(system_text, prompt_text))
