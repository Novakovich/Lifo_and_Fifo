import json
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template('index.html')

#@app.route('/donate')
#def donate():
#    return 'Hello World! '

@app.route('/request/donation')
def donation():
    with open ('data.json', 'r', encoding='utf-8') as data:
        data_list = json.load(data)
        item = data_list.pop()
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
