from flask_cors import CORS
from flask import Flask, request, jsonify
from flask.templating import render_template
import os
from converters.ConvertRomanToDecimal import ConvertRomanToDecimal
from converters.ConvertDecimalToRoman import ConvertDecimalToRoman
from amazon_textract.AwsImageToText import extract_text_from_image

app = Flask(__name__, template_folder='../front-end', static_folder='../front-end/static')
CORS(app)

# Main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert-to-decimal', methods=['POST'])
def to_decimal():
    user_input = request.json.get('word')
    
    if not user_input:
        return jsonify({"error": "No word or phrase provided"}, 400)
    
    converter = ConvertRomanToDecimal()
    response = converter.convert_to_decimal(user_input)
    
    print(response)
    return jsonify(response)

@app.route('/convert-to-roman', methods=['POST'])
def to_roman():
    user_input = request.json.get('word')
    
    if not user_input:
        return jsonify({"error": "No word or phrase provided"}, 400)
    
    converter = ConvertDecimalToRoman()
    response = converter.convert_to_roman_numeral(user_input)
    
    print(response)
    return jsonify(response)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}, 400)
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file provided"}, 400)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file.save(os.path.join(current_dir, file.filename))
    
    file_path = os.path.join(current_dir, file.filename)    
    
    response = extract_text_from_image(file_path)
    
    converter = ConvertRomanToDecimal()
    
    amazon_textract_dir = os.path.join(current_dir, 'amazon_textract')
    file_path = os.path.join(amazon_textract_dir, 'output.txt')
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # convert extracted text into decimals 
    result = []
    for line in lines:
        line = line.strip() 
        print(line) 
        output = converter.convert_to_decimal(line)
        result.append(output)
    
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)