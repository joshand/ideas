from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    page = "<form action='app.py'><br>\n"
    page = page + "<h5>Submit your idea here!</h5><br>\n"
    page = page + "Full Name: <input type='input' name='fullname'><br>\n"
    page = page + "Company: <input type='input' name='company'><br>\n"
    page = page + "Email Address: <input type='input' name='email'><br>\n"
    page = page + "Idea: <textarea name='idea' rows='25' cols='100'></textarea><br>\n"
    page = page + "<input type='submit' value='Submit'><br>\n"

    return page


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
