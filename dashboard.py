import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("aljazeera_articles.csv")

# Page Title
st.title("Al Jazeera News Crawler Dashboard")
st.write("## Data Overview")
st.write(data.head())

# Crawlability Score (placeholder, update based on Member 1's findings)
st.metric("Crawlability Score", "8/10", help="Based on robots.txt & RSS analysis")

# Article count by Category (optional if you have 'category' column)
# st.bar_chart(data['category'].value_counts())

# Word Cloud of Headlines
st.write("### Word Cloud of Article Titles")
titles = " ".join(data['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Search functionality
st.write("### Search Articles by Keyword")
search_term = st.text_input("Enter a keyword")
if search_term:
    filtered = data[data['title'].str.contains(search_term, case=False, na=False)]
    st.write(filtered)

# Optional: Date filter (if date data gets added later)
# date_range = st.date_input("Filter by date", [])
