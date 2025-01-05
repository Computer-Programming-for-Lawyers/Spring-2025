import pandas as pd

def validate(prompt: str,lower_bound: int,upper_bound: int) -> int:
    # print("The validate function is now running.")
    while True:
        answer = int(input(prompt))
        if lower_bound <= answer <= upper_bound:
            return answer
        else:
            print(f"The input must be a number between {lower_bound} and {upper_bound}")