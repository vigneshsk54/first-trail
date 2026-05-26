import os
import sys
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='www')

@app.route('/')
def root():
    return send_from_directory('www', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('www', path)

if __name__ == '__main__':
    print("🚀 Starting development server...")
    print("📁 Serving files from: www/")
    print("🌐 Server will be available at: http://localhost:8080")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
