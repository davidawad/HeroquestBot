from app import app
import dataset

# Connnect to database
db = dataset.connect('sqlite:///file.db')

# create your guests table
table = db['guests']

# when someone sends a GET to / render sign_form.html
@app.route('/', methods=['GET'])
def sign_form():
    return render_template('sign_form.html')

# when someone sends a GET to /guest_book render guest_book.html
@app.route('/guest_book', methods=['GET'])
def guest_book():
    signatures = table.find()
    return render_template('guest_book.html', signatures=signatures)

# when someone sends  POST to /submit, take the name and message from the body
# of the POST, store it in the database, and redirect them to the guest_book
@app.route('/submit', methods=['POST'])
def submit():
    signature = dict(name=request.form['name'], message=request.form['message'])
    table.insert(signature)
    return redirect(url_for('guest_book'))

'''
def request(hostname):
 //this is actually node but I threw it in here. sue me. 
	var http = require('http'); 
	setInterval(function () {
	  http.request({host: 'myapp.herokuapp.com', path: '/'}, function (resp) {
	    resp.on('data', console.log);
	  }).end()
	}, 1800000)
	return True
'''
