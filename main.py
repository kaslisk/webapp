from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sup():
    if request.method == "GET":
        return render_template("index.html")
    else:
        fbacktype = request.form.get('fbacktype')
        y5class = request.form.get('class')
        name = request.form.get('name')
        email = request.form.get('email')
        suggestion = request.form.get('suggestion')
        fout = open("INFO.txt", 'a')
        fout.write(fbacktype + ',' + y5class + ',' + name + ',' + email+ ',' + suggestion + '\n')
        fout.close()
        fin = open("INFO.txt", 'r')
        lines = fin.readlines()
        fin.close()
        if name == "jesus christ" and fbacktype == "others" and y5class == "5C35":
          return redirect("https://www.youtube.com/watch?v=bSiEB64FyF8&list=LLPTHdfqWJp0bimnuq1pKlww&index=27")
        else:
          return render_template("page.html", name=name, email=email,  fbacktype=fbacktype, y5class=y5class, suggestion=suggestion, lines=lines)


@app.context_processor
def date():
    return {'now': datetime.now()}


app.run(host='0.0.0.0', port=8080)
