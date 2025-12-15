import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

# -----------------------------
# TEXT CLEANING
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    return text

# -----------------------------
# NLP FEATURES
# -----------------------------
def analyze_text(text):
    cleaned = clean_text(text)

    # Tokenization
    tokens = word_tokenize(cleaned)

    # Remove stopwords
    filtered_tokens = [w for w in tokens if w not in stop_words]

    # Word Count
    word_count = len(filtered_tokens)

    # Character Count
    char_count = len(text)

    # Most Common Words
    word_freq = Counter(filtered_tokens).most_common(10)

    # Basic sentiment using lexicons (not ML)
    positive_words = ['good', 'great', 'love', 'happy', 'excellent']
    negative_words = ['bad', 'poor', 'hate', 'sad', 'terrible']

    sentiment_score = (
        sum(1 for w in filtered_tokens if w in positive_words)
        - sum(1 for w in filtered_tokens if w in negative_words)
    )

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "cleaned": cleaned,
        "tokens": filtered_tokens,
        "word_count": word_count,
        "char_count": char_count,
        "word_freq": word_freq,
        "sentiment": sentiment
    }