from flask import Flask, render_template, request

app = Flask(__name__)

comments = []  # Store the submitted comments

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', comments=comments)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    comments.append(comment)  # Add the comment to the list
    return render_template('index.html', comments=comments)

if __name__ == "__main__":
    pass  # No need for app.run() on PythonAnywhere
