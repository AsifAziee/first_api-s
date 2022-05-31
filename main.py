from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


@app.route('/home', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		# return jsonify ({'name': 'Jimit',
		#   'address': 'India'})
		return '<h1>Mohammed Asif <br> Alappuzha</h1>'


@app.route('/nextapi', methods=['GET'])
def nxt_api():
	if(request.method == 'GET'):
		return '<h1>Asif <br> Alappuzha</h1>'



@app.route('/array', methods=['POST'])
def addition_array():
    inputdata = request.json
    sum = 0
    for number in inputdata['num']:
        sum = sum + number
    return str(sum)





if __name__ == '__main__':
	app.run(debug=True)
