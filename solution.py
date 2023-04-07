import pandas as pd
import numpy as np


chat_id = 243149489 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.log((x).mean()) - np.log(415)
