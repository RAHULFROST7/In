import spacy
import nltk
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import numpy as np
from math import ceil
from typing import NewType

actualAnswer = NewType('actualAnswer' ,str) 
givenAnswer = NewType('givenAnswer' ,str)

def getScore( sentence1 : actualAnswer , sentence2 : givenAnswer ):
    
    
    def preprocess_sentence(text):
            
            text = text.lower()
            text = text.translate(str.maketrans("", "", string.punctuation))
            stop_words = set(stopwords.words("english"))
            words = text.split()
            words = [w for w in words if w not in stop_words]
            
            return " ".join(words)
        
        
    lenS1 = len(sentence1)
    lenS2 = len(sentence2)
    
    if((lenS1 and lenS2 != 0) and ((lenS1 * 1/7) < lenS2)):
        
        # print("Gets in")
        processed_sentence1 = preprocess_sentence(sentence1)
        processed_sentence2 = preprocess_sentence(sentence2)
        final_score = 0
        
        for i in range(1,3):
            
            nlp = spacy.load('en_core_web_lg' if i == 1 else 'en_core_web_md')

            # print(nlp.meta['name'], '\n')
            weighted_score = 0

            # Compute Spacy similarity score
            doc1 = nlp(processed_sentence1)
            doc2 = nlp(processed_sentence2)
            spacy_similarity_score = 0
            spacy_similarity_score = doc1.similarity(doc2)


            # Compute TF-IDF vector representation for each sentence
            vectorizer = TfidfVectorizer()
            sentence1_tfidf = vectorizer.fit_transform([processed_sentence1])
            sentence2_tfidf = vectorizer.transform([processed_sentence2])


            # Compute cosine similarity score using TF-IDF vectors
            cosine_similarity_score = 0
            cosine_similarity_score = cosine_similarity(sentence1_tfidf, sentence2_tfidf)[0][0]

            
            try:
                
                tokens1 = word_tokenize(processed_sentence1)
                tokens2 = word_tokenize(processed_sentence2)
                    
                # create word embeddings for each string
                model = gensim.models.Word2Vec([tokens1, tokens2], min_count=2)
                word_vectors = {word: model.wv[word] for word in model.wv.index_to_key}
                    
                # calculate the average vector for each string
                vector1 = np.mean([word_vectors[word] for word in tokens1 if word in word_vectors], axis=0)
                vector2 = np.mean([word_vectors[word] for word in tokens2 if word in word_vectors], axis=0)
                    
                # calculate cosine similarity between the vectors
                sim_score = 0
                sim_score = cosine_similarity([vector1], [vector2])[0][0]
                # print("ends within try")
                
            except:
                
                sim_score = 0
                # print("except")
                sim_score = weighted_score


            tokens1 = set(nltk.word_tokenize(sentence1.lower()))
            tokens2 = set(nltk.word_tokenize(sentence2.lower()))

            jaccard_similarity_score = 0
            jaccard_similarity_score = len(tokens1.intersection(tokens2)) / len(tokens1.union(tokens2))


            # Weighted average of the similarity scores
            weighted_score = (0.5 * spacy_similarity_score) + (0.3 * jaccard_similarity_score) + (0.2 * cosine_similarity_score)


            # Compute the average similarity score
            average_similarity_score = 0
            average_similarity_score = spacy_similarity_score * .15 + ( jaccard_similarity_score + cosine_similarity_score + ( weighted_score + sim_score ) * .15 ) / 2
            final_score += average_similarity_score
            # # Print the similarity scores
            # print("Spacy similarity score:", spacy_similarity_score)
            # print("Cosine similarity score:", cosine_similarity_score)
            # print("Jaccard similarity score:",jaccard_similarity_score)
            # print("Weighted similarity score:", weighted_score)
            # print("Gensim similarity score:", sim_score)
            # # print("average ",average_similarity_score)
            # print("\n\nAnswer score is :",average_similarity_score,"\n\n")
        res = ceil((final_score/2)*100)
        # print("Simalarity score is :",0 if ceil((final_score/2)*100) < 50 else (100 if ceil((final_score/2)*100) > 100 else ceil((final_score/2)*100)))
        return 0 if res < 50 else (100 if res > 100 else res) 
        # return average_similarity_score
    # print("Score :",getScore("rahul ate apple","the apple was eaten by rahul"))
    else:
        # print("Gets in else")
        return 0
