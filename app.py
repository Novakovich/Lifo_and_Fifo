import json
from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)
app.debug = True
BASE_DIR = Path(__file__).resolve().parent.parent


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate():
    with open('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
        data_list.append(
            {"name": request.form["name"], "amount": request.form["amount"]}
        )
    with open('data.json', 'w') as data:
        json.dump(data_list, data)
    return render_template('donte.html')

@app.route('/request/donation')
def donation():
    with open('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
    if not data_list:
        return render_template('request.html')
    item = data_list.pop()
    with open('data.json', 'w') as data:
        json.dump(data_list, data)
    return f""" 
    {render_template('donation.html')}
    here {item['name']} {item['amount']} 
    """

if __name__ == '__main__':
    app.run(debug=True)
