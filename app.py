from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

# Optional: Serve FBX models explicitly (if needed)
@app.route('/static/models/<path:filename>')
def serve_model(filename):
    return send_from_directory('static/models', filename)

# Optional: Serve images if having issues
@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
