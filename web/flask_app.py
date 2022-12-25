
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, url_for, render_template, request,jsonify
from flask import make_response
from flask_cors import CORS, cross_origin

from sanskrit_tools.panini import dhaatus as dh
from sanskrit_tools.panini import pratyaya as pr


"""


# python anywhere
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello from Flask!'
"""


def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='images/' + filename), code=301)


def query_sanskrit():
    response = None
    if request.method=="GET":
        try :
            rtype = str(request.args.get('type'))
            response_dict = {'dhaatus': lambda : make_response({'Data': dh.get_all_dhaatus() }),
                    'pratyayas': lambda : make_response(jsonify(pr.get_all_suffixes()))
                    }
            func = response_dict.get(rtype, lambda : make_response(jsonify({'Error':"UNKNOWN type"+str(rtype)})) )
            response = func()

        except Exception as e:
            print(e)
            response = make_response(jsonify({'Error':"Exception" +str(e)}))




    else:
        resonse =make_response (jsonify(''))

    response.headers.add('Content-Type','application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 
    #return "<html><head/><body> sanskrit request="+request_method+" </body></html>"

def display_sanskrit():
    return render_template('sanskrit.html')

def display_index():
    #dat =""
    #with open('/home/anuragr/research_persona/index.html') as fh:
    #    dat = fh.read()
    #return dat
    return render_template('index.html')


# EB looks for an 'app' callable by default.
app = Flask(__name__)

# add a rule for the index page.
app.add_url_rule('/', 'index', (lambda: display_index()) )
app.add_url_rule('/display/<filename>', view_func=display_image )
app.add_url_rule('/sanskrit/', 'sanskrit', (lambda: display_sanskrit()) )
app.add_url_rule('/query_sanskrit/', 'query_sanskrit', (lambda: query_sanskrit()) )

# add a rule when the page is accessed with a name appended to the site
# URL.
#app.add_url_rule('/<username>', 'hello', (lambda username: header_text + say_hello(username) + home_link + footer_text))

# Add cors configuration
cors = CORS(app)
#CORS(app, resources=r'/api/*')
app.config['CORS_HEADERS'] = 'Content-Type'


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    run_console = False
    if run_console:
        print(display_index())
    else:
        app.debug = False
        app.run()


