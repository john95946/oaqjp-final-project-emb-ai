'''
emotion detector web application
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    '''display the index template'''
    return render_template('index.html')

@app.route('/emotionDetector')
def get_the_emotion():
    '''detect the emotions'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    if dominant is None:
        return '<b>Invalid text! Please try again!</b>'

    return f"For the given statement, the system response is 'anger': {anger}, " + \
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.  " + \
        f"The dominant emotion is <b>{dominant}</b>."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
