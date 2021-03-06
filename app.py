from flask import Flask, render_template, request, make_response, jsonify
import pickle

app = Flask(__name__)

def init():
    global model
    model = pickle.load(open('/home/hb/PROJECT/Chatbot_project/model2.pkl', 'rb'))

@app.route('/', methods =['GET'])
def home():
    if request.method == 'GET':
        return render_template('base.html')

@app.route('/predict', methods =['POST'])
def predict():
    # model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        user_input = request.form.get('question')
        user_input = str(user_input)
        prediction = model.predict(user_input)
    else:
        prediction = ""
    return make_response({
        "error": False,
        "data": {
            'Accuracy': prediction[3],
            'Answer': prediction[0]
        }
    }, 200)

if __name__ == '__main__':
    init()
    app.run(debug=True)