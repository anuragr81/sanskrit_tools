
import json

from flask import Flask, redirect, url_for, render_template, request,jsonify
from flask import make_response
from flask_cors import CORS, cross_origin

from panini import requesthandlers as rh
from panini import expressiontree as expt


"""


# python anywhere
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello from Flask!'
"""


def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename), code=301)


"""
the function to present the next set of suffixes corresponding to a given suffix sent as part of the request
"""
def respond_to_pratyayas_request(request):
    try:
        pratyaya = request.args.get('pratyaya')
        if pratyaya:
            nextSuffixes = rh.get_next_pratyayas(pratyaya)
            if nextSuffixes is None:
                nextSuffixes = json.dumps({})
            response = make_response({'Data':nextSuffixes})

        else:
            response = make_response(jsonify({'Error':"Missing Pratyaya"+str(request.args.get('type'))}))
    except Exception as e:
            response = make_response(jsonify({'Error':"Exception" +str(e)}))


    return response



"""
returns the list of all dhaatu suffixes
"""
def respond_to_dhaatupratyayas_request(request):
    try:
        response = make_response({'Data':rh.get_dhaatu_suffixes()})
    except Exception as e:
        response = make_response (jsonify({'Error':'Exception: '+str(e)}))

    return response


"""
creating a tree from the expression
"""
def respond_to_expression_request(request):
    try:
        expr = request.args.get('expr')
        typelist = request.args.get('typelist')
        if expr and typelist:
            response = make_response(jsonify({'Data':str(expt.get_expression_tree(expr,typelist))}))
        else:
            response = make_response(jsonify({'Error':"Missing expr or typelist ("+str(request.args.get('type')+")")}))
    except Exception as e:
            response = make_response(jsonify({'Error':"Exception ( " +str(e)+ " )"}))


    return response

"""
The main handler of te requests
"""
def query_sanskrit():
    response = None
    if request.method=="GET":
        try :
            rtype = str(request.args.get('type'))
            response_dict = {'dhaatus': lambda x : make_response({'Data': rh.get_all_dhaatus() }),
                    'pratyayas': respond_to_pratyayas_request,
                    'dhaatupratyayas': respond_to_dhaatupratyayas_request,
                    'expr': respond_to_expression_request
                    }
            func = response_dict.get(rtype, lambda x : make_response(jsonify({'Error':"UNKNOWN type"+str(rtype)})) )
            response = func(request)

        except Exception as e:
            response = make_response(jsonify({'Error':"Exception" +str(e)}))




    else:
        response =make_response (jsonify(''))

    ##response.headers.add('Content-Type','application/json')
    ##response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def display_sanskrit():
    return render_template('sanskrit.html')

def display_index():
    return render_template('index.html')


# EB looks for an 'app' callable by default.
app = Flask(__name__)

# add a rule for the index page.


app.add_url_rule('/', 'index', (lambda: display_index()) )


app.add_url_rule('/display/<filename>', view_func=display_image )
app.add_url_rule('/sanskrit/', 'sanskrit', (lambda: display_sanskrit()) )
app.add_url_rule('/query_sanskrit/', 'query_sanskrit', (lambda: query_sanskrit()) )


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


