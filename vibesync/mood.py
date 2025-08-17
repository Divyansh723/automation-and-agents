from type import BehaviorTracker
from emotion import get_transcript_result

def predict_mood(voice_sentiment, typing_data):
    # voice_sentiment: 'POSITIVE', 'NEUTRAL', 'NEGATIVE'
    # typing_data: dict with keys: keystrokes, backspaces, avg_key_interval_sec, mouse_moves

    mood_score = 0

    # Voice sentiment weight
    if voice_sentiment == 'POSITIVE':
        mood_score += 2
    elif voice_sentiment == 'NEUTRAL':
        mood_score += 1
    else:  # NEGATIVE
        mood_score -= 2

    # Typing behavior weight
    # More backspaces relative to keystrokes → negative mood
    backspace_ratio = typing_data['backspaces'] / typing_data['keystrokes']
    if backspace_ratio > 0.15:
        mood_score -= 2
    elif backspace_ratio > 0.05:
        mood_score -= 1

    # Avg key interval: longer intervals might indicate tiredness or distraction
    if typing_data['avg_key_interval_sec'] > 1.0:
        mood_score -= 1
    elif typing_data['avg_key_interval_sec'] < 0.4:
        mood_score += 1

    # Mouse movement: very low movement might mean boredom or tiredness
    mouse_moves_per_min = typing_data['mouse_moves'] / (typing_data['tracking_duration_sec'] / 60)
    if mouse_moves_per_min < 50:
        mood_score -= 1
    elif mouse_moves_per_min > 200:
        mood_score += 1

    # Final mood decision
    if mood_score >= 3:
        return 'Happy'
    elif mood_score >= 1:
        return 'Neutral'
    elif mood_score >= -1:
        return 'Tired'
    else:
        return 'Stressed'

# Example usage:
voice_sentiment = 'NEUTRAL'  # from AssemblyAI sentiment output
typing_data = {
    'keystrokes': 839,
    'backspaces': 80,
    'avg_key_interval_sec': 0.69,
    'mouse_moves': 12932,
    'tracking_duration_sec': 600
}

mood = predict_mood(voice_sentiment, typing_data)
print("Predicted Mood:", mood)
