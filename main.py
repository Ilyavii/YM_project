from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route("/")
def main():
    df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

    return render_template("example.html",
                           tables=[df.to_html()], titles=df.columns.values)

# план работ 
# flask table with select and buttom 
# save file with rows which was select
# Golang
# open file and send to Yandex by api. 
# maybe And send 200 to python.

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    

"""
{% extends "table_Yandex_Metriki.html" %}
{% block content %}
<h1>{{title}}</h1>
{{data | safe}}
{% endblock %}"""