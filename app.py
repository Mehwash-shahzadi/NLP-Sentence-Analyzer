import streamlit as st
from textblob import TextBlob

st.title("The Comprehensive Sentence Analysis Tool")

sentence = st.text_input("Enter a sentence to analyze:")

# Sentiment Analysis
if st.button("Sentiment Analysis Only"):
    if sentence:
        try:
            blob = TextBlob(sentence)
            sentiment = blob.sentiment
            st.subheader("Sentiment Analysis")
            st.write(f"Polarity (Emotion): {sentiment.polarity}")
            st.write(f"Subjectivity (Opinion): {sentiment.subjectivity}")
        except Exception as e:
            st.error(f"An error occurred: {e}. Please check your input.")
    else:
        st.write("Please enter a sentence to analyze!")

# Part-of-Speech Tagging
if st.button("Part-of-Speech Tagging Only"):
    if sentence:
        try:
            blob = TextBlob(sentence)
            tags = blob.tags
            st.subheader("Part-of-Speech Tagging")
            st.write("Word Tags:", tags)
        except Exception as e:
            st.error(f"An error occurred: {e}. Please check your input.")
    else:
        st.write("Please enter a sentence to analyze!")

# Word Frequency Analysis
if st.button("Word Frequency"):
    if sentence:
        try:
            blob = TextBlob(sentence)
            words = blob.words
            word_freq = {}
            for word in words:
                word_lower = word.lower()
                if word_lower not in word_freq:
                    word_freq[word_lower] = 1
                else:
                    word_freq[word_lower] = word_freq[word_lower] + 1
            st.subheader("Word Frequency Analysis")
            st.write("Word Frequencies:", word_freq)
        except Exception as e:
            st.error(f"An error occurred: {e}. Please check your input.")
    else:
        st.write("Please enter a sentence to analyze!")

# Full Analysis
if st.button("Full Analysis"):
    if sentence:
        try:
            blob = TextBlob(sentence)
            # Sentiment Analysis
            sentiment = blob.sentiment
            st.subheader("Sentiment Analysis")
            st.write(f"Polarity (Emotion): {sentiment.polarity}")
            st.write(f"Subjectivity (Opinion): {sentiment.subjectivity}")

            # Part-of-Speech Tagging
            tags = blob.tags
            st.subheader("Part-of-Speech Tagging")
            st.write("Word Tags:", tags)


            # Word Frequency Analysis
            words = blob.words
            word_freq = {}
            for word in words:
                word_lower = word.lower()
                if word_lower not in word_freq:
                    word_freq[word_lower] = 1
                else:
                    word_freq[word_lower] = word_freq[word_lower] + 1
            st.subheader("Word Frequency Analysis")
            st.write("Word Frequencies:", word_freq)
        except Exception as e:
            st.error(f"An error occurred: {e}. Please check your input.")
    else:
        st.write("Please enter a sentence to analyze!")
