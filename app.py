from flask import Flask, render_template, request
import joblib

app = Flask(__name__)  # <-- fixed

# Load saved vectorizer and model
vectorizer = joblib.load("tfidf_vectorizer.pkl")
clf = joblib.load("logreg_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        article = request.form["news_text"]
        if article.strip():
            pred = clf.predict(vectorizer.transform([article]))[0]
            prediction = "Real" if pred == 1 else "Fake"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":  # <-- fixed
    app.run(debug=True)
