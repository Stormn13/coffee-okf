from others.state import State

def input_question(state: State):
    question = input('What do u wanna ask?')

    return {'input_question' : question}
