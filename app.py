import os
os.environ["NLS_LANG"] = "American_America.AL32UTF8"
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import cx_Oracle

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():

    return render_template('base.html', title='Главная')

@app.route('/incidents')
def incidents():
    posts = []
    engine = cx_Oracle.connect('hack', '123456', '192.168.137.49:1521/gdb')
    cur = engine.cursor()
    result = cur.execute(
        "SELECT ID, PRIORITY, CDATE, EDATE, SPEECH_TO_TEXT, IDESC, AGENT_NAME, SMS_TEXT FROM HACK.INCIDENT ORDER BY ID DESC").fetchall()
    for record in result:
        record = {'id': record[0],
                'priority': record[1],
                'cdate': record[2],
                'edate': record[3],
                'speech_to_text': record[4],
                'idesc': record[5],
                'agent_name': record[6],
                'sms_text': record[7]}
        posts.append(record)
    print(posts)
    return render_template('incident.html', posts=posts)


if __name__ == '__main__':
    app.run()

