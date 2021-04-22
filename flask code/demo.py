from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/<name>", methods=['GET'])
def home(name):
  
    return jsonify({"message": f"Hello! {name}"})
  
if __name__ == "__main__":
    app.run(debug=True)