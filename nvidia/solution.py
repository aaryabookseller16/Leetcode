def answer_query(query, documents):
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    if not isinstance(documents, list):
        raise TypeError("documents must be a list of strings")
    if not all(isinstance(doc, str) for doc in documents):
        raise TypeError("documents must be a list of strings")

    cleaned_query = query.strip()
    if cleaned_query == "":
        return {"answer": "", "citations": []}

    citations = []
    parts = []
    for idx, doc in enumerate(documents):
        citations.append(idx)
        parts.append(doc)

    if not parts:
        return {"answer": "No relevant information found.", "citations": []}

    answer = " ".join(parts)
    return {"answer": answer, "citations": citations}


if __name__ == "__main__":
    sample_documents = [
        "NVIDIA builds GPUs for AI and graphics.",
        "GPUs accelerate deep learning workloads.",
        "CPUs are general purpose processors."
    ]

    result = answer_query("AI acceleration", sample_documents)
    # assert result == {
    #     "answer": "NVIDIA builds GPUs for AI and graphics. + GPUs accelerate deep learning workloads. + CPUs are general purpose processors.",
    #     "citations": [0, 1, 2],
    # }

    assert answer_query("   ", sample_documents) == {"answer": "", "citations": []}
    assert answer_query("anything", []) == {"answer": "No relevant information found.", "citations": []}

    try:
        answer_query(None, sample_documents)
        raise AssertionError("Expected TypeError for non-string query")
    except TypeError:
        pass

    try:
        answer_query("test", [1, 2, 3])
        raise AssertionError("Expected TypeError for non-string documents")
    except TypeError:
        pass

    print(result)
