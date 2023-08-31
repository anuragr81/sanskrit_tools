
import json

from flask import Flask, redirect, url_for, render_template, request,jsonify
from flask import make_response
from flask_cors import CORS, cross_origin

from panini import dhaatus as dh
from panini import pratyaya as pr
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

def respond_to_pratyayas_request(request):
    try:
        pratyaya = request.args.get('pratyaya')
        if pratyaya:
            if pr.is_suptingant(pratyaya):
                response = make_response(jsonify({'Data':json.dumps({})}))
            else:
                nextSuffixes = pr.get_next_pratyayas(pratyaya)
                if nextSuffixes is None:
                    nextSuffixes = json.dumps({}) 
                response = make_response({'Data':nextSuffixes})

        else:
            response = make_response(jsonify({'Error':"Missing Pratyaya"+str(request.args.get('type'))}))
    except Exception as e:
            response = make_response(jsonify({'Error':"Exception" +str(e)}))


    return response


def respond_to_dhaatupratyayas_request(request):
    try:
        dhaatu = request.args.get('dhaatu')
        # currently the same pratyayas apply to all dhaatus
        response = make_response({'Data':pr.get_dhaatu_suffixes()})
    except Exception as e:
        response = make_response (jsonify({'Error':'Exception: '+str(e)}))

    return response


def respond_to_expression_request(request):
    try:
        expr = request.args.get('expr')
        if expr:
            response = make_response(jsonify({'Data':str(expt.get_expression_tree(expr))}))
        else:
            response = make_response(jsonify({'Error':"Missing expr"+str(request.args.get('type'))}))
    except Exception as e:
            response = make_response(jsonify({'Error':"Exception" +str(e)}))


    return response


def query_sanskrit():
    response = None
    if request.method=="GET":
        try :
            rtype = str(request.args.get('type'))
            response_dict = {'dhaatus': lambda x : make_response({'Data': dh.get_all_dhaatus() }),
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


