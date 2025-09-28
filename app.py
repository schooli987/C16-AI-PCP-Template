from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Target languages with full names
TARGET_LANGS = {
    'hi': 'Hindi',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German'
}

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    translations = {}

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            try:
                for code, name in TARGET_LANGS.items():
                    translations[name] = GoogleTranslator(source='auto', target=code).translate(text)
            except Exception as e:
                translations = {name: f"Error: {e}" for name in TARGET_LANGS.values()}

    return render_template(
        "index.html",
        text=text,
        translations=translations
    )

if __name__ == "__main__":
    app.run(debug=True)
