from textblob import TextBlob
import streamlit as st

# Defining the sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Streamlit Code
st.title("Saybee Analyzer")
user_input = st.text_input("Enter text to analyze:")
if not user_input:
    st.write("Please enter text")
else:
    sentiment = analyze_sentiment(user_input)
    st.write("Sentiment: ", sentiment)