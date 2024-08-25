from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
    {
        'id':'1',
        'title':'Data 1',
        'location':'Johannesburg',
        'salery':'R1200'
    },
    {
        'id':'2',
        'title':'Data 2',
        'location':'Durban',
        'salery':'R1500'
    },
    {
        'id':'3',
        'title':'Data 3',
        'location':'Cape Town',
        'salery':'R2400'
    }
]
@app.route("/")
def helo():
    # to add the list dynamically into the html temolate add an argument for example job and pass the list (job = JOBS)
    return render_template('home.html', job=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)