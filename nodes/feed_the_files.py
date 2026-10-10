from others.state import State
from pathlib import Path
import frontmatter

def __compare(A: list, B: list) -> float:
    setA = set(A)
    setB = set(B)
    overlap = setA.intersection(setB)
    total_unique = setA.union(setB)

    similarity = (len(overlap)/len(total_unique))*100
    return similarity


def feed_the_files(state : State):
    listA = state['tag'] #first list #type: ignore
    best_similarity = -1.0
    selected_file: Path | None = None
    dir_path = Path(__file__).resolve().parent.parent / "knowledge_base"
    #loop to iteratively check the second list
    for item in dir_path.rglob("*.md"):
        if item.is_file():
            #get the tag of the second file
            with open(item, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            metadata = post.metadata
            listB = metadata['tags']
            #time to check the similarity
            similarity = __compare(listA, listB) #type: ignore
            #store the simiraity and the item if the number is the highest
            if similarity >= best_similarity:
                best_similarity = similarity
                selected_file = item
    #now maxx has the file that we need to send to the llm for the query
    if selected_file is None:
        raise FileNotFoundError(f"No Markdown knowledge-base files found in {dir_path}")
    return {"selected_file" : str(selected_file)}
