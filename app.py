from flask import Flask, request, jsonify
import requests
import os
import simplejson

def GetFileContents(fn):
    d = ""
    if os.path.isfile(fn):
        with open(fn, 'r') as infile:
            d = simplejson.load(infile)

    return d

app = Flask(__name__)

@app.route("/")
def default_page():
    page = "<form action='/save' method='post'>\n"
    page = page + "<h5>Submit your idea here!</h5>\n"
    page = page + "Full Name: <input type='input' name='fullname'><br>\n"
    page = page + "Company: <input type='input' name='company'><br>\n"
    page = page + "Email Address: <input type='input' name='email'><br>\n"
    page = page + "Idea:<br><textarea name='idea' rows='25' cols='100'></textarea><br>\n"
    page = page + "<input type='submit' value='Submit'><br>\n"

    return page

@app.route("/save", methods = ['POST'])
def save_page():
    vfn = request.form["fullname"]
    vco = request.form["company"]
    vem = request.form["email"]
    vid = request.form["idea"]
    
    retval =  "fullname=" + vfn + ";company=" + vco + ";email=" + vem + ";idea=" + vid
    savedict = {"name":vfn,"company":vco,"email":vem,"idea":vid}
    newlist = GetFileContents('data.json')
    if type(newlist) is list:
        newlist.append(savedict)
    else:
        newlist = [savedict]
    with open('data.json', 'w') as outfile:
        simplejson.dump(newlist,outfile)

    return retval
    
@app.route("/view")
def view_page():
    return jsonify(GetFileContents('data.json'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
