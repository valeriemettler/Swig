#!/usr/bin/env python
from flask import Flask, redirect, request
import json

app = Flask(__name__)

count = {}

@app.route("/")
def state():
    global count
    return json.dumps(count)

@app.route("/<user>")
def inc(user):
    global count
    if user in count.keys():
        count[user] += 1
    else:
        count[user] = 1
    return """Hello {0} <br /> 
    <b>{1}!</b>
    <form method="get" action="/set/{0}">
    <input type="text" name="cnt" />
    <input type="submit">
    </form>
    <hr />
    <form method="get" action="/{0}">
    <button type="submit"> Inc </button>
    </form>
    """.format(user, count[user])

@app.route("/<user>/<cnt>")
def set_count(user, cnt):
    global count
    count[user] = int(cnt)
    return redirect("/{}".format(user))

@app.route("/set/<user>")
def set_it(user):
    global count
    cnt = request.args.get('cnt')
    count[user] = int(cnt)
    return redirect("/{}".format(user))


if __name__ == "__main__":
    app.run()

