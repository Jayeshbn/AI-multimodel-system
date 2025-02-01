from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage with the model showcase."""
    return render_template('index.html')

@app.route('/load_model/<model_name>')
def load_model(model_name):
    """Dynamically load a model's interface."""
    if model_name == "text_model":
        return render_template('text_model.html')
    elif model_name == "image_model":
        return render_template('image_model.html')
    else:
        return "<p>Model not found</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
