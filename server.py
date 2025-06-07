#!/usr/bin/env python3
# server.py - Web server for Brain Tumor Detection

from app import create_flask_app

if __name__ == "__main__":
    app = create_flask_app()
    app.run(debug=True, port=5000, host='0.0.0.0')