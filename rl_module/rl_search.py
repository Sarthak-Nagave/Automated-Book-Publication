from typing import List

def rl_based_search(documents: List[str], query: str) -> str:
    """
    Simple RL-inspired scoring to find the best match for the query from documents.
    """
    scores = []
    for doc in documents:
        # Reward based on the occurrence of the query keywords
        reward = sum([1 for word in query.lower().split() if word in doc.lower()])
        scores.append(reward)

    max_index = scores.index(max(scores)) if scores else 0
    return documents[max_index] if documents else ""
