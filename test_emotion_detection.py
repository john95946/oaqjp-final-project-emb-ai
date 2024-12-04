import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    '''class to test the emotion_detector function'''
    def test_emotion_detector(self):
        text = "I am glad this happened"
        dominant = 'joy'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], dominant)

        text = "I am really mad about this"
        dominant = 'anger'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], dominant)

        text = "I feel disgusted just hearing about this"
        dominant = 'disgust'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], dominant)

        text = "I am so sad about this"
        dominant = 'sadness'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], dominant)

        text = "I am really afraid that this will happen"
        dominant = 'fear'
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], dominant)


if __name__ == '__main__':
    unittest.main()