from core import app, mail, cache, mail_html
from flask import redirect, url_for, request, render_template
from flask_mail import Message

# URLS


@app.route('/')
@cache.cached(timeout=300)
def index():
    return render_template('index.html', name='index')


@app.route('/contact', methods=['POST', 'GET'])
@cache.cached(timeout=300)
def contact():
    if request.method == 'POST':
        msg = Message("Contact ME",
                      recipients=["tommaso2001.pero@gmail.com"])
        msg.html = mail_html.format(
            request.form['name'], request.form['message'], request.form['email'], request.form['phone'])
        mail.send(msg)
        return ('', 204)
    else:
        return redirect(url_for('index'))

# ERROR HANDLERS


@app.errorhandler(404)
def page_not_found(e):
    return '404 - Not Found', 404


@app.errorhandler(500)
def page_not_found(e):
    return '500 - Internal Server Error', 500
