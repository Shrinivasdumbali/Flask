from flask import Flask, render_template, jsonify  #(html is jsonifyed!!)

app = Flask(
    __name__)  #flask variable "app" is used further while deploying over cloud

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}, {
    'id': 5,
    'title': 'SDE III',
    'location': 'Pune, India'
}]


@app.route("/")  #route one
def shrini():
    return render_template("home.html", jobs=JOBS,
                           company_name="Shrini's")  #attribute


#route 2(api_route)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)  #api called json


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
