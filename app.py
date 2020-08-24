from flask import Flask, render_template, request, redirect, url_for, flash
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')
print ("server starting")
@app.route('/')
def index():
    print ("handling request")
    Todos = session.get_items()
    return render_template('index.html',Todos = Todos, name = 'Annas')

@app.route('/add_item', methods=["POST"])
def add_item():
    session.add_item(request.form.get('title'))
    print ("adding item")
    flash("Item successfully added")
    return redirect (url_for('index'))

if __name__ == '__main__':
    app.run()