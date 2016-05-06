from flask import Flask, make_response, abort, redirect

app = Flask(__name__);
#adding route for the main webpage and linking to the webpage
@app.route('/')
def hello_world():
    return redirect('https://preview.c9users.io/aleksandarkasabov/final/assignment/index.html?_c9_id=livepreview4&_c9_host=https://ide.c9.io')

#adding route for giving an error and linking to the error page    
@app.route('/error')
@app.route('/errors')
def error():
    return redirect('https://preview.c9users.io/aleksandarkasabov/final/assignment/error.html?_c9_id=livepreview5&_c9_host=https://ide.c9.io')


@app.route('/unexpected')
def unexpected():
    abort(404)
    return True

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)