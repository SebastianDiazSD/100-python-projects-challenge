import time
import random
from constants import TIME_LIMIT_SECONDS, COLOMBIAN_PROMPTS


class WritingLogic:
    def __init__(self):
        self.last_keypress_time = time.time()

    def update_keypress(self):
        self.last_keypress_time = time.time()

    def should_delete_text(self):
        current_time = time.time()
        return (current_time - self.last_keypress_time) > TIME_LIMIT_SECONDS

    def get_prompt(self):
        return random.choice(COLOMBIAN_PROMPTS)