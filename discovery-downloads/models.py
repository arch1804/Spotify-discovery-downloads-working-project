from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the SQLAlchemy instance here (initialized with the app in app.py)
db = SQLAlchemy()


class User(db.Model):
    """Represents a platform user with a download limit."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    download_limit = db.Column(db.Integer, default=3)

    # Relationship: a user can have many downloads
    downloads = db.relationship('Download', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'


class Track(db.Model):
    """Represents a music track available for download."""
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(200), nullable=False)
    is_emerging = db.Column(db.Boolean, default=False)

    # Relationship: a track can appear in many downloads
    downloads = db.relationship('Download', backref='track', lazy=True)

    def __repr__(self):
        return f'<Track {self.name} by {self.artist}>'


class Download(db.Model):
    """Represents a single download action linking a user to a track."""
    __tablename__ = 'downloads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    expiry_timestamp = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Download user={self.user_id} track={self.track_id}>'
