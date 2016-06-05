import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    phones = []
    has_result = False

    if request.method == "POST":
        text_input = request.form['text-input']
        compiled_result = re.compile('([8|9|7]\d{2})\D*(\d{3})\D*(\d{4})').findall(text_input)

        if len(compiled_result):
            has_result = True

        for itm in compiled_result:
            phones.append('('+itm[0]+') '+itm[1]+' - '+itm[2])

    return render_template('index.html', result=phones, has_result=has_result)

if __name__ == '__main__':
    app.run()
