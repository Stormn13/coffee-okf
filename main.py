from langgraph.graph import StateGraph, START, END
from others.state import State


graph = StateGraph(State)

#define nodes
graph.add_node('input_question', input_question)
graph.add_node('filter_tags', filter_tags)
graph.add_node('feed_the_files', feed_the_files)
graph.add_node('final_output', final_output)
#define edges
graph.add_edge(START, 'input_question')
graph.add_edge('input_questions', 'filter_tags')
graph.add_edge('filter_tags', 'final_output')
graph.add_edge('final_output', END)

workflow = graph.compile()