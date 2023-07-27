from flask import Flask, render_template, request
import plotly.graph_objects as go
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Replace with your actual database URL
db_url = "mysql+pymysql://username:password@localhost/finance_nifty50"
engine = create_engine(db_url)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        df = pd.read_sql(f"SELECT Date, Close FROM StockPrices WHERE Symbol = '{ticker}'", engine)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close'))

        graph_json = fig.to_json()

        return render_template('graph.html', graph_json=graph_json)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
