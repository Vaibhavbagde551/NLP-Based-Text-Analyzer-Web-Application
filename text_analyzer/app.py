from flask import Flask, render_template, request
from text_analysis import analyze_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    user_text = request.form["input_text"]
    result = analyze_text(user_text)

    return render_template("result.html", 
                           text=user_text,
                           cleaned=result["cleaned"],
                           tokens=result["tokens"],
                           word_count=result["word_count"],
                           char_count=result["char_count"],
                           word_freq=result["word_freq"],
                           sentiment=result["sentiment"])

if __name__ == "__main__":
    app.run(debug=True)