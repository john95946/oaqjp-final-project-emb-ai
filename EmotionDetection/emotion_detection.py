'''
Emotion Prediction detector
'''
import json
import requests


def emotion_detector(text_to_analyze):
    '''emotion dectector function which analyzes the passed in text
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/' + \
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    json_data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=json_data,
                             headers=headers, timeout=5)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = json.loads(response.text)
    anger_score = disgust_score = fear_score = joy_score = sadness_score = 0
    for prediction in emotions['emotionPredictions']:
        anger_score += prediction['emotion']['anger']
        disgust_score += prediction['emotion']['disgust']
        fear_score += prediction['emotion']['fear']
        joy_score += prediction['emotion']['joy']
        sadness_score += prediction['emotion']['sadness']

    anger_score /= len(emotions['emotionPredictions'])
    disgust_score /= len(emotions['emotionPredictions'])
    fear_score /= len(emotions['emotionPredictions'])
    joy_score /= len(emotions['emotionPredictions'])
    sadness_score /= len(emotions['emotionPredictions'])

    dominant_score = 0
    dominant_emotion = None
    emotion_detector = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    for key, value in emotion_detector.items():
        if value > dominant_score:
            dominant_emotion = key
            dominant_score = value

    emotion_detector['dominant_emotion'] = dominant_emotion

    return emotion_detector
