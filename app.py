from flask import Flask
from flask import Flask, jsonify, abort, request, make_response, url_for,render_template


import psycopg2
import psycopg2.extras
import sys
import os


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__, static_url_path = "")



engine = create_engine('postgres:///jive', echo=True)
#engine = create_engine(os.environ['DATABASE_URL'], echo=True)
connection = engine.connect()

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/test')
def test():

	arr =[]
	for row in engine.execute('select * from nodes'):
		arr.append(dict(row))
		print(row)
	return jsonify(arr); 


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/nodes',methods = ['GET','POST'])
def getNodes():
	arr =[]
	for row in engine.execute('select id,txt from nodes'):
		arr.append(dict(row))

	return jsonify(arr); 


@app.route('/nodes/create', methods = ['GET','POST'])
def createNode():
    if not request.json or not 'nodeId' in request.json:
        abort(400)
    task = {
 
        'nodeId': request.json['nodeId'],
        'text': request.json.get('text', "")
       
    }
    
    engine.execute("insert into nodes (id,txt) values (" +str(request.json['nodeId'])+ "," + "'" + str(request.json['text'])+"')")


@app.route('/nodes/update', methods = ['POST'])
def updateNode():
    if not request.json or not 'nodeId' in request.json:
        abort(400)
    task = {
        'nodeId': request.json['nodeId'],
        'text': request.json.get('text', "")
    }

    engine.execute("UPDATE nodes SET txt="  +"'" + str(request.json['text'])  +"'" + "WHERE id ="+ str(request.json['nodeId']))

@app.route('/nodes/delete', methods = ['POST'])
def deleteNode():
    if not request.json or not 'nodeId' in request.json:
        abort(400)
    task = {
 
        'nodeId': request.json['nodeId'],
        'text': request.json.get('text', "")
       
    }

    engine.execute('DELETE FROM nodes WHERE id = '+ str(request.json['nodeId']));


#LINKS

@app.route('/links',methods = ['GET'])
def getLinks():
    #failed:
    #a = {'target': 'nodes['+str(2)+']', 'source': 'nodes['+str(1)+']'}#, {'target': 3, 'source': 1}
    #a = "{target: id:0, 'source: id:1}"
    #a = {'target': 'id:0', 'source': 'id:1'}
    #a = "{source: nodes[0], target: nodes[1]}"
    
    #pass list 
    #a = [[0,1],[1,2]]

    #pass json OK
    #a = [{'s':0,'t':1},{'s':1,'t':2},{'s':0,'t':2}]
    #return jsonify(a)
    def cook():
        arr =[]
        for row in engine.execute('select target,source from edges'):
            #print (np.asarray(dict(row)))
            #arr.append((row))
            arr.append(dict(row))
            #arr.append(np.asarray((row)))
            #arr.append(eval("[" +row+"]"))
            #print (dict(row))
        
        print (arr)
        return arr

    return jsonify(cook()); 


	
if __name__ == "__main__":
    app.run(debug = True)