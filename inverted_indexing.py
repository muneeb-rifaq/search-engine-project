def create_inverted_index(forward_index):
    """Creates the inverted index from the forward index."""
    inverted_index = {}
    
    # Iterate through the forward index and populate the inverted index
    for docID, word_ids in forward_index.items():
        for word_id in word_ids:
            if word_id not in inverted_index:
                inverted_index[word_id] = []
            inverted_index[word_id].append(docID)
    
    return inverted_index
