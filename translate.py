# import required materials
from flask import Flask, render_template, request, jsonify
import boto3
from Language_list import language_list

app = Flask(__name__, template_folder='.')
client = boto3.client('translate')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the form data from the request
    source_lang = request.json['sourceLang']
    target_lang = request.json['targetLang']
    text = request.json['text']

    # Translation function
    def translation_function(user_input, source_lang, target_lang):
        translation = client.translate_text(Text=user_input, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
        return translation['TranslatedText']

    # Perform the translation
    translated_text = translation_function(text, source_lang, target_lang)

    # Return the translated text as JSON
    return jsonify({'translatedText': translated_text})

if __name__ == '__main__':
    app.run()
