import numpy as np 
import tensorflow as tf 
from tensorflow.keras.datasets import imdb 
from tensorflow.keras.preprocessing import sequence 
from keras.models import Sequential 
from tensorflow.keras.layers import Embedding,SimpleRNN, Dense  
import numpy as np 
import tensorflow as tf 
from tensorflow.keras.datasets import imdb 
from tensorflow.keras.preprocessing import sequence 
from tensorflow.keras.models import load_model 

#load imdb dataset word index 
word_index=imdb.get_word_index() 
reverse_word_index={value: key for key, value in word_index.items()}


model=load_model("C:\\Users\\shaikr4\\Desktop\\Personla\\Python\\DeepLearning\\NLP\\SimpleRNN\\SimpleRNN_imdb.h5")



print(model.summary())
##step 2 Helper function 
## function to decode the reviews 

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])



#function to preprocess the usr input 
def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review



### prediction function 
def predict_sentiment(review):
    preprocessed_input=preprocess_text(review)
    prediction=model.predict(preprocessed_input)
    sentiment ="Positive " if prediction[0][0]>0.5 else 'Negative'
    return sentiment,prediction[0][0]



import streamlit as st 
st.title('IMBD Movie Review Sentiment Analysis ')

st.write('Enter a movie review to classify it as positive or negative .')

#userinput 
usr_input=st.text_area('Moview review')


if st.button('Classify'):
    preprocess_input=preprocess_text(usr_input)

    #make prediction 
    prediction=model.predict(preprocess_input)
    sentiment='Positve ' if prediction[0][0] >0.5 else 'Negative'
   

   #display the result 
    st.write(f'Sentiment ; {sentiment}')
    st.write(f'Prediction score :{prediction[0][0]}')
else:
    st.write('Please enter a movie review')

