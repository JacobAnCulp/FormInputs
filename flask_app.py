from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    Console = request.form.get('Console', '')
    Genre = request.form.get('Genre', '')
    Rating = request.form.get('Rating', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="With the search constraints of " + Console + ", " + Genre + ", and " + Rating + ", we have determined 0 games for you.")