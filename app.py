# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, make_response

app = Flask(__name__)


@app.route('/testMainUrl')
def test_main_url():
    resp = make_response(make_content_main())
    resp.set_cookie('node', 'node1')
    resp.set_cookie('name', 'john')
    resp.set_cookie('sid', '123')
    return resp


@app.route('/testRedirect')
def test_redirect():
    print "redirect cookie", request.cookies
    return redirect("/testRedirectedUrl/success", code=302)


@app.route('/testRedirectedUrl/success')
def test_redirected():
    print "redirected cookie", request.cookies
    return make_content_redirect()


def make_content_main():
    return "main content"

def make_content_redirect():
    return "redirected content"


if __name__ == '__main__':
    app.run(debug=True)
