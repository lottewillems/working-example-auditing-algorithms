from flask import Flask, render_template, request
from transformers import pipeline
from transformers import RobertaTokenizer, RobertaForSequenceClassification
tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robBERT-base")
model = RobertaForSequenceClassification.from_pretrained("dbrd_model2_copy")

app = Flask('NLP')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    sentence_clasf = pipeline('sentiment-analysis', model = model, tokenizer = tokenizer)
    if request.method == 'POST':
        input_sent = request.form['message']
        output = sentence_clasf(input_sent)
        pred_label = output[0]['label']
        if pred_label == "LABEL_1":
            prediction = "Positive"
        elif pred_label == "LABEL_0":
            prediction = "Negative"
        else:
            prediction = "Unable to classify"
        probability = round((output[0]['score'] * 100), 2)
    return render_template('result.html', content = input_sent, prediction = prediction, prob = probability)

if __name__ == '__main__':
	app.run(debug=True)
