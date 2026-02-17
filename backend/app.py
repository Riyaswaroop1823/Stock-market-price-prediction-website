from flask import Flask, jsonify
from flask_cors import CORS
from stock_predictor import StockPredictor

app = Flask(__name__)
CORS(app)

predictor = StockPredictor()

@app.route("/")
def home():
    return "StockAI backend is running"


@app.route("/predict/<symbol>")
def predict(symbol):

    result = predictor.predict(symbol, future_days=30)

    predictions = result["predictions"]

    response = {
        "symbol": symbol,

        "current_price": result["historical_prices"][-1],

        "prediction_24h": predictions[0],

        "prediction_7d": predictions[6],

        "prediction_30d": predictions[29],

        "confidence_24h": result["confidence_scores"][0],

        "confidence_7d": result["confidence_scores"][6],

        "confidence_30d": result["confidence_scores"][29]
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)