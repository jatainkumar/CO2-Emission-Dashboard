from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

DATA_PATH = 'data/final_report.csv'

def calculate_total_emissions():
    df = pd.read_csv(DATA_PATH)
    total_emissions = df['CO2 Total'].mean()
    return round(total_emissions, 2)

@app.route('/')
def index():
    total_emissions = calculate_total_emissions()
    return render_template('index.html', total_emissions=total_emissions)

if __name__ == '__main__':
    app.run(debug=True)
