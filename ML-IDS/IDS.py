from flask import Flask, render_template, request, redirect, url_for
import output

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def home():
    return render_template('home.html', val = 0, tab = (0, 0, 0, ""), num = 0)
@app.route("/home")
def hello():
    return render_template('home.html', val = 0, tab = (0, 0, 0, ""), num = 0)
@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['slid_val']
        model_number = request.form['optradio']
        
        return redirect(url_for('user', usr=user, mod_number = model_number))
    else:
        return render_template('home.html')
    
@app.route('/<usr>/<mod_number>', methods=["POST", "GET"])
def user(usr, mod_number = 0):
    tab = output.table(int(usr), int(mod_number))
    return render_template('home.html', val = usr, tab = tab, num = mod_number)   

@app.route("/about")
def about():
    return load_model.code()

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == '__main__':
    app.run(debug=True)