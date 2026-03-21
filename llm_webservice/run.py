from waitress import serve
from app import create_app

app = create_app()

print("✅ Backend setup complete. Server starting...")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)