#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'mailtest'

@app.route('/')
def main():
    return render_template('contactform.html')


@app.route('/sendmessage.php')
def send(info=None):
    #return render_template('sendmessage.php')
    return render_template('sendmessagetest.html', info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
