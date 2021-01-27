from main import createApp
import sys
import os

sys.dont_write_bytecode = True

# Initialise flask app
app = createApp(os.getenv("FLASK_ENV", "development"))

# Index Route
@app.route("/", methods=["GET"])
def home_route():
    return "Application is running fine"

if __name__ == '__main__':
    app.run()