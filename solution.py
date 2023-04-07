import pandas as pd
import numpy as np


chat_id = 243149489 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return (4 * np.log((x - 415).mean()) - np.log(((x - 415)**2).mean())) / 2
