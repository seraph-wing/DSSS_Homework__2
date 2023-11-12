import random



def get_random_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def get_random_operator():
    """
    function that returns a random choice from a list
    returs: ["+", "-", "*"]
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, o):
    """
    function that returns the result of a calculation based on the choice
    n1: number 1
    n2: number 2
    o: operator
    returns: result of the calculation
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    function that runs the math quiz
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    print("You will earn 3 points for each correct answer, and lose 1 point for each wrong answer.")

    for _ in range(total_questions):
        n1 = get_random_int(1, 10)
        n2 = get_random_int(1, 10)
        o = get_random_operator()

        PROBLEM, ANSWER = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 3
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            score -= 1

    print(f"\nGame over! Your score is: {score}/{total_questions*3}")

if __name__ == "__main__":
    math_quiz()
