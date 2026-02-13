import os

class Config:
    """Configuration class for Flask application"""
    
    # Secret key for session management (will be needed later)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration (SQLite)
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'discovery.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Logging
    LOG_DIR = os.path.join(BASEDIR, 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'app.log')
