from jobapp import create_app
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    app = create_app()
    if os.getenv("FLASK_ENV") == 'dev':
        app.run(debug=True)
    else:
        app.run()