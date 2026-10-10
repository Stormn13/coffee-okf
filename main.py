from langgraph.graph import StateGraph, START, END
from others.state import State
from nodes.input_question import input_question
from nodes.filter_tag import filter_tag
from nodes.feed_the_files import feed_the_files
from nodes.final_ouput import final_output
graph = StateGraph(State)

#define nodes
graph.add_node('input_question', input_question)
graph.add_node('filter_tag', filter_tag)
graph.add_node('feed_the_files', feed_the_files)
graph.add_node('final_output', final_output)
#define edges
graph.add_edge(START, 'input_question')
graph.add_edge('input_questions', 'filter_tag')
graph.add_edge('filter_tag', 'final_output')
graph.add_edge('final_output', END)

workflow = graph.compile()

initial_state : State = {"initial_question": "how much is a latte?"}