from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load your CSV data using pandas
    df = pd.read_csv('deliverables/stock_screener_grouped_for_AMKR,FORM,RMBS,LSCC,MTSI,ALGM,WOLF,QRVO,IPGP,POWI,SYNA.csv')

    # Convert the DataFrame to JSON for easier manipulation in JavaScript
    data_json = df.to_json(orient='records')

    return render_template('index.html', data_json=data_json)

if __name__ == '__main__':
    app.run(debug=True)