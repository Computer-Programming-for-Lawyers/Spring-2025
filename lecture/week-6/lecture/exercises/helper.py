def does_it_work():
    return 'Systems are go!'

def parse_yn1(prompt):
    answer = input(prompt)
    return answer == 'y' or answer == 'yes'

def parse_yn2(prompt):
    answer = input(prompt)
    yeses = ['y', 'yes']
    return answer in yeses

### Clear out the above, make these at the top of the file
yeses = ['y', 'yes'] #, 'yessssss', 'oui', 'si']
nos = ['n', 'no', 'non', 'hell no']

def parse_yn3(prompt):
    answer = input(prompt)
    return answer in yeses

def parse_yn4(prompt):
    answer = input(prompt).lower()
    return answer in yeses

def parse_yn5(prompt: str) -> bool:
    answer = input(prompt).lower()
    return answer in yeses

def parse_yn6(prompt: str) -> bool:
    while True:
        answer = input(prompt).lower()
        if answer in yeses:
            return True
        elif answer in nos:
            return False
        
        print("I don't understand you. Try again.")


def validate1(prompt, lower_bound, upper_bound):
    # Version when there is both a lower_bound and a upper_bound
    while True:
        answer = int(input(prompt))
        if lower_bound <= answer <= upper_bound:
            return answer
        else:
            print(f"The input must be a number between {lower_bound} and {upper_bound}.")

def validate2(prompt, lower_bound, upper_bound=None):
    # Version when there is both a lower_bound and a upper_bound
    while True:
        answer = int(input(prompt))
        if upper_bound is not None:
            if lower_bound <= answer <= upper_bound:
                return answer
            else:
                print(f"The input must be a number between {lower_bound} and {upper_bound}.")
        else:
            if lower_bound <= answer:
                return answer
            else:
                print(f"The input must be a number greater than or equal to {lower_bound}.")
