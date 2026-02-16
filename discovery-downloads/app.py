from flask import Flask, render_template
from config import Config
from models import db, User, Track

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with this Flask app
db.init_app(app)


def seed_database():
    """Insert sample data only if the tables are empty."""
    if User.query.first() is None:
        test_user = User(name='Test User', download_limit=3)
        db.session.add(test_user)

    if Track.query.first() is None:
        tracks = [
            Track(name='Midnight Echoes', artist='Luna Wave', is_emerging=True),
            Track(name='Neon Drift', artist='Solar Flare', is_emerging=True),
            Track(name='Golden Hour', artist='The Weeknd', is_emerging=False),
        ]
        db.session.add_all(tracks)

    db.session.commit()


# Create tables and seed data on startup
with app.app_context():
    db.create_all()
    seed_database()


@app.route('/')
def home():
    """Homepage route - displays the track list from the database."""
    tracks = Track.query.all()
    return render_template('home.html', tracks=tracks)


if __name__ == '__main__':
    app.run(debug=True)
