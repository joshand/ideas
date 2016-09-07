from flask import Flask

app = Flask(__name__)

@app.route("/")
def default_page():
    page = "<form action='/save'>\n"
    page = page + "<h5>Submit your idea here!</h5>\n"
    page = page + "Full Name: <input type='input' name='fullname'><br>\n"
    page = page + "Company: <input type='input' name='company'><br>\n"
    page = page + "Email Address: <input type='input' name='email'><br>\n"
    page = page + "Idea:<br><textarea name='idea' rows='25' cols='100'></textarea><br>\n"
    page = page + "<input type='submit' value='Submit'><br>\n"

    return page

@app.route("/save")
def save_page():
    vfn = request.form.get("fullname")
    vco = request.form.get("company")
    vem = request.form.get("email")
    vid = request.form.get("idea")
    
    retval =  "fullname=" + vfn + ";company=" + vco + ";email=" + vem + ";idea=" + vid

    return retval

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
