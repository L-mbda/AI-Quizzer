import google.generativeai as genie
KEY = "KE"
genie.configure(api_key=KEY)
points = 0
print("TRIVIA SYSTEM.")
sessionpl = True

while sessionpl:
    prompt = "Make a trivia question with multiple choice. Do not put any of your response in, just the question itself and the multiple choice. Thanks!"

    m = genie.GenerativeModel(model_name='gemini-1.0-pro')
    r = m.generate_content(prompt, stream=True)

    l = []
    for c in r:
        for p in c.parts:
            l.append(p.text)
    response = ''.join(l)

    print(response)
    choice = input("What is your answer?: ")
    scorer_system = f"""
    Hello!
    You must assume the role of an all numbers scoring system. You must also be correct with your response.
    You must say this code: 'U24HF' if the answer is correct, if not, then code 'OJUBJ32'

    YOU MUST BE ACCURATE AND CORRECT

    Please just have the code in the format: code, correct_answer, explanation, no other response.

    Here are some hyperparameters for explanation, please provide the explanation as simple, do not provide any other thing.

    Here is the question:
    {response}

    Here is the user response:
    {choice}
    """
    r = m.generate_content(scorer_system, stream=True)

    l = []
    for c in r:
        for p in c.parts:
            l.append(p.text)
    response = ''.join(''.join(l))
    response = response.split(',')
    if response[0] == 'OJUBJ32':
        print(f"Incorrect answer! The correct answer is {response[1]}")
        print(f"Explanation: {response[1]}")
        points -= 1
    else:
        print("Correct answer! You have been awarded one point.")
        points += 1
    if points == 5 or points == -5:
        print("The game is over.")
        sessionpl == False