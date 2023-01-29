from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
while True:
    r = input('> ')

    sequence_to_classify = r
    candidate_labels = ['travel', 'sports', 'movies']
    a = classifier(sequence_to_classify, candidate_labels)
    
    #{'labels': ['travel', 'dancing', 'cooking'],
    # 'scores': [0.9938651323318481, 0.0032737774308770895, 0.002861034357920289],
    # 'sequence': 'one day I will see the world'}

    print(a['labels'][0])