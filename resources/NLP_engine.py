import spacy
import nltk
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import numpy as np
from math import ceil , floor
import warnings
from typing import NewType

actualAnswer = NewType('actualAnswer' ,list) 
givenAnswer = NewType('givenAnswer' ,str)

def getScore( sentence1 : actualAnswer , sentence2 : givenAnswer ):
    
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    warnings.filterwarnings("ignore", category=UserWarning)
    def preprocess_sentence(text : str):
            
            text = text.lower()
            text = text.translate(str.maketrans("", "", string.punctuation))
            stop_words = set(stopwords.words("english"))
            words = text.split()
            words = [w for w in words if w not in stop_words]
            
            return " ".join(words)
        
        
    lenS1 = len(sentence1)
    lenS2 = len(sentence2)
    
    if((lenS1 and lenS2 != 0) and ((lenS1 * 1/7) < lenS2)):
        
        processed_sentence2 = preprocess_sentence(sentence2)
        nlp = spacy.load('en_core_web_lg')
        score_list = []
        tokens2 = set(nltk.word_tokenize(sentence2.lower()))
        
        
        for i in range(0,2):
            
            # print("Gets in")
            processed_sentence1 = preprocess_sentence(sentence1[i])
            final_score = 0
                
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


            tokens1 = set(nltk.word_tokenize(sentence1[i].lower()))

            jaccard_similarity_score = 0
            jaccard_similarity_score = len(tokens1.intersection(tokens2)) / len(tokens1.union(tokens2))


            # Weighted average of the similarity scores
            weighted_score = (0.5 * spacy_similarity_score) + (0.3 * jaccard_similarity_score) + (0.2 * cosine_similarity_score)
            

            # Compute the average similarity score
            
            average_similarity_score = 0
            average_similarity_score = spacy_similarity_score * .15 + ( jaccard_similarity_score + cosine_similarity_score + ( weighted_score + sim_score ) * .15 ) / 2
            final_score = ceil(average_similarity_score * 100)
            # print(final_score)
            score_list.append(final_score)
            # # Print the similarity scores
            # print("Spacy similarity score:", spacy_similarity_score)
            # print("Cosine similarity score:", cosine_similarity_score)
            # print("Jaccard similarity score:",jaccard_similarity_score)
            # print("Weighted similarity score:", weighted_score)
            # print("Gensim similarity score:", sim_score)
            # print("average ",average_similarity_score)
            # print("\n\nAnswer score is :",average_similarity_score,"\n\n")
            # res = ceil((final_score/2)*100)
            # print("Simalarity score is :",0 if ceil((final_score/2)*100) < 50 else (100 if ceil((final_score/2)*100) > 100 else ceil((final_score/2)*100)))
            # return 0 if res < 50 else (100 if res > 100 else res) 
        # return score_list
        result = max(score_list)
        return (np.random.randint(8,30)) if result < 50 and result > 10 else ((np.random.randint(93,100)) if result > 100 else (floor(result*1.10) if (result <75 and result > 60) else (floor(result * 0.6) if (result < 70 and result > 50) else ( 0 if result < 0 else result))))
        # return result
        # return (np.random.randint(8,30)) if result < 50 and result > 10 else ((np.random.randint(93,100)) if result > 100 else (floor(result*1.10) if result <75 and result > 60 else (floor(result * 0.8) if result < 70 and result > 50 else ( 0 if result < 0 else result))))
    else:

        return 0


# print(getScore(["ysf8y8uwejfiwoenhn8inh8euifer yveruh   btrerwb reuo fiuerhrbvyubvhvu vfyb r ebufbv dfbfdbfhuburfjernjhdbvhjdfnvjehjeriuhuehu hh uih fhiuerfh","iuwehfuowhg ucyudhcyu cyudsgcci7dciudshciu dhusc  sbcs yu wcwuwehfwwiufuer hriuu erb riurhrhfuhuof ldfjbdfkjuvhgerbjfbu hjsbj sdbc  dsiuo shbjdsbusydg iwdibv"],"Rdkjvnsdkjvnsdkjndi sdidjsiodj siodjdsi jids sdijcidscids idsjdilsiljsdfio sdiohip fdsij ioscj oisjiocjiodsjcio ds jcids jiodsjiods 9dj oids viojids fi9siodfijioew fidsj iods iodsjvidsjiodjdiov diovud iovhiubkdsbvaogbvyudbvkshdfdbqoduhfvbqei voqiuhbpviuq"))