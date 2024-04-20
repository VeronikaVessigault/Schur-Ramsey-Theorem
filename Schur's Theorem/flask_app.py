from math import remainder
from flask import Flask, render_template, request, redirect, url_for
import sys
import os
import csv
import old_schur
 
app = Flask(__name__, static_url_path = "/upload", static_folder = "upload")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/show-schur', methods=["GET"])
def visualization():
    return render_template('show_schur.html')

@app.route('/run-schur', methods =["GET", "POST"])
def bulk_random_walk():
    dim = -1
    steps = -1
    runs = -1
    if request.method == 'POST':
        dim = request.form['dim']
        steps = request.form['steps']
        runs = request.form['number of walks']

        #walks.set_valid_keys_by_steps()
        #walks.set_valid_keys_by_dimension()

        allowed_dim = [1,2,3,4,5,6,7,8]
        if int(dim) in allowed_dim and int(steps)>199 and int(steps)<15001 and int(runs) > 0 and int(runs) < 100001:
            if int(steps) < 7501 and int(steps) % 100 == 0:
                ending_vecs = []
                how_many_rec = []
                #print(ending_vecs)
                percent_rec = str(round(how_many_rec/int(runs)*100,4)) + "%"
                vectors = []
                return render_template('random_walk_bulk_w_stats.html', vectors = vectors, how_many_rec = how_many_rec, percent_rec = percent_rec, dim = dim, steps = steps, runs = runs)
            elif int(steps) % 500 == 0:
                ending_vecs = []
                how_many_rec = []
                percent_rec = str(round(how_many_rec/int(runs)*100,4)) + "%"
                vectors = []
                return render_template('show-schur.html', vectors = vectors, how_many_rec = how_many_rec, percent_rec = percent_rec, dim = dim, steps = steps, runs = runs)
        else:    
            dim_right = False
            steps_right = False
            runs_right = False
            if int(dim) in allowed_dim:
                dim_right = True
            if (int(steps) > 199 and int(steps) < 7501 and int(steps) % 100 == 0) or (int(steps) > 7499 and int(steps) < 15001 and int(steps) % 500 == 0):
                steps_right = True
            if int(runs) > 0 and int(runs) < 25001:
                runs_right = True
            if not (dim_right or steps_right or runs_right):
                return render_template('random_walk_bulk.html', error_message = "error_message_dim_steps_runs.html", dim = dim, steps = steps, runs = runs)
            elif not (dim_right or steps_right):
                return render_template('random_walk_bulk.html', error_message = "error_message_dim_steps.html", dim = dim, steps = steps)
            elif not (dim_right or runs_right):
                return render_template('random_walk_bulk.html', error_message = "error_message_dim_runs.html", dim = dim, runs = runs)
            elif not (steps_right or runs_right):
                return render_template('random_walk_bulk.html', error_message = "error_message_steps_runs.html", steps = steps, runs = runs)
            elif not dim_right:
                return render_template('random_walk_bulk.html', error_message = "error_message_dim.html", dim = dim)
            elif not steps_right:
                return render_template('random_walk_bulk.html', error_message = "error_message_steps.html", steps = steps)
            elif not runs_right:
                return render_template('random_walk_bulk.html', error_message = "error_message_runs.html", runs = runs)
    return render_template('run_schur.html', error_message = "empty.html")

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)
 
 
#app.run(host='localhost', port=5000)