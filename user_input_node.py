from typing_extensions import TypedDict

def user_input_node(state: TypedDict):
    return {'topic': state['topic']}