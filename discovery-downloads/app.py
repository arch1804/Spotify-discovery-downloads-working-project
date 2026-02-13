from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Dummy track data (hardcoded for Day 1)
DUMMY_TRACKS = [
    {
        'id': 1,
        'name': 'Blinding Lights',
        'artist': 'The Weeknd',
        'album': 'After Hours',
        'duration': '3:20'
    },
    {
        'id': 2,
        'name': 'Levitating',
        'artist': 'Dua Lipa',
        'album': 'Future Nostalgia',
        'duration': '3:23'
    },
    {
        'id': 3,
        'name': 'Save Your Tears',
        'artist': 'The Weeknd',
        'album': 'After Hours',
        'duration': '3:35'
    },
    {
        'id': 4,
        'name': 'Good 4 U',
        'artist': 'Olivia Rodrigo',
        'album': 'SOUR',
        'duration': '2:58'
    },
    {
        'id': 5,
        'name': 'Heat Waves',
        'artist': 'Glass Animals',
        'album': 'Dreamland',
        'duration': '3:58'
    }
]

@app.route('/')
def home():
    """Homepage route - displays the track list"""
    return render_template('home.html', tracks=DUMMY_TRACKS)

if __name__ == '__main__':
    app.run(debug=True)
