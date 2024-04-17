from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST", "GET"])
def predict():
    try:
        if request.method == "POST":
            data = request.get_json()
            text = data.get("message")
            
            # TODO: Check if text is valid or not
            response = get_response(text)
            
            message = {"answer": response}
            return jsonify(message)
        elif request.method == "GET":
            # Assuming you want to check if the response on the webpage is "Welcome"
            webpage_response = "Welcome"  # Replace this with the actual response you expect
            
            # You can customize this condition based on your needs
            if webpage_response == "Welcome":
                return jsonify({"status": "Success"})
            else:
                return jsonify({"status": "Not Welcome"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
