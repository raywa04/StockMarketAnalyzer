from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

# Load processed data
def load_data(symbol):
    file_path = f"data/{symbol}_data.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

@app.route('/data', methods=['GET'])
def get_data():
    symbol = request.args.get('symbol', 'AAPL')
    data = load_data(symbol)
    return data.to_json()

@app.route('/visualize', methods=['GET'])
def visualize_data():
    symbol = request.args.get('symbol', 'AAPL')
    data = load_data(symbol)
    if data.empty:
        return "No data available for this stock symbol.", 404
    
    img = io.BytesIO()
    data.plot(x='date', y='close', kind='line')
    plt.title(f"{symbol} Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return jsonify({'image_url': f"data:image/png;base64,{plot_url}"})

@app.route('/update_dashboard', methods=['POST'])
def update_dashboard():
    symbol = request.form.get('symbol', 'AAPL')
    from scripts.data_processing import fetch_stock_data, process_data
    df = fetch_stock_data(symbol)
    if not df.empty:
        process_data(df, symbol)
        return jsonify({'message': f"Dashboard updated successfully for {symbol}!"})
    else:
        return jsonify({'message': f"Failed to update dashboard for {symbol}."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
