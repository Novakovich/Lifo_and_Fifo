import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/donate', methods=["POST", "GET"])
def donate():
    with open ('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
        data_list.append(
            {"name": request.form["Donatation"], "amount": request.form["Amount"]}
        )
    with open('data.json', 'w') as data:
        json.dump(data_list, data)
    return f""" Thank you
            <html>
                <body>
                    <p>
                    <a href="/">Return main</a>
                    </p>
                </body>
            </html>"""

@app.route('/request/donation')
def donation():
    with open ('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
    if not data_list:
        return f""" here nothing for you 
            <html>
                <body>
                    <p>
                    <a href="/">Return main</a>
                    </p>
                </body>
            </html>"""
    item = data_list.pop()
    with open('data.json', 'w') as data:
        json.dump(data_list, data)
    return f""" here {item['name']} {item['amount']} 
    <html>
        <body>
            <p>
            <a href="/">Return main</a>
            </p>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True)
