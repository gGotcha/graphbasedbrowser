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
	for row in engine.execute('select * from nodes where id !=2'):
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

    arr =[]
    for row in engine.execute('select target,source from edges'):
        #for k,v in dict(row):
        #    print (k,v)




        arr.append(dict(row))
        dc = dict(row)
        for k,v in dc.items():
            print (k,v)

    return jsonify(arr); 



@app.route('/links/up',methods = ['POST'])
def updateLinks():
 

    if not request.json or not 'lks' in request.json:
        abort(400)
    task = {
 
        'lks': request.json['lks']

       
    }

    re = request.json['lks']
    print (request.json['lks'])


    print ('UUUUUUUUUUUUUUU')
    engine.execute(" delete from edges")
    for i in re:
        print (i['source']['id'])
        src = i['source']['id']
        tgt = i['target']['id']


        engine.execute("INSERT INTO public.edges(source, target) values (" + str(src) + "," + str(tgt) +")")
        #engine.execute("insert into edges (source,target) values (" + str(src) + "," + str(tgt) +")")


@app.route('/links/delete',methods = ['POST'])
def deleteLinks():
 

    if not request.json or not 'lks' in request.json:
        abort(400)
    task = {
 
        'lks': request.json['lks']

       
    }

    re = request.json['lks']
    print (request.json['lks'])

    engine.execute(" delete from edges")

    engine.execute(" delete from nodes")
"""  

@app.route('/links/create',methods = ['POST'])
def createLinks():

    if not request.json or not 'src' in request.json:
        abort(400)
    task = {
 
        'source': request.json['src'],
        'target': request.json['tgt']
       
    }

     engine.execute("INSERT INTO public.edges(source, target) values (" + str(src) + "," + str(tgt) +")")

    #engine.execute('insert into edges (source,target) values (2,3)')
    #engine.execute("insert into edges (source,target) values (" +str(request.json['src'])+ "," + "'" + str(request.json['tgt'])+"')")
"""


@app.route('/getquery',methods = ['GET','POST'])
def get_by_post():

    def cook():
        #got string 'select * from winners'
        print(">>>>>>>>>>>>>>>>>>>>ALL       " + str(request.args))
        #failed#print(">>>>>>>>>>>>>>>>>>>>ARG[0]       " + str(request.args[0]))
        print(">>>>>>>>>>>>>>>>>>>>ARGtoDICT       " + str(dict(request.args)))
        got = dict(request.args)
        gotstr = ''

        for k,v in got.items():
            print ('KKKKKKKKKKKKKKKKKkk' + str(k))
            print ('VVVVVVVVVVVVVVVV' + str(type(v[0])))
            
            if v[0] == '':
                print ('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFff')
                gotstr = str(k)
                break

            gotstr = str(k) + '=' + str(v[0])

        print ('GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTTTTTTTTTTt' + gotstr)

        al = []
        
        #for row in engine.execute('select id,txt from nodes where id != 0'):
        for row in engine.execute(gotstr):
        #for row in engine.execute('select id from winners where year is 1921'):         
            al.append(dict(row))
            #print(dict(row))
        return al
        
    #failed
    #return get_from_db_by_request();
    #return jsonify(dict(str(get_from_db_by_request()));

    #OK
    #print('jsonify JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ' +   str(jsonify(get_from_db_by_request())))
    

    return jsonify(cook());
    #return jsonify(str(get_from_db_by_request())); #bad, d3 gets arr[0] ('f,gghh,fhfh,')



"""
app.route('/todo/api/v1.0/tasks/win',methods = ['GET','POST'])
def get_by_post():

    def get_from_db_by_request():
        #got string 'select * from winners'
        print(">>>>>>>>>>>>>>>>>>>>ARG       " + str(request.args))
        print(">>>>>>>>>>>>>>>>>>>>ARG       " + str(dict(request.args)))

        gotarg = str(list(dict(request.args).keys())[0])

        print(">>>>>>>>>>>>>>>>>>>>ARG       " + gotarg)
        

        #print(">>>>>>>>>>>>>>>>>>>>>>GOTTTT" + str(engine.execute(gotarg)))

        al = []
        for row in engine.execute(gotarg):

        #for row in engine.execute('select id from winners where year is 1921'):
            
            al.append(dict(row))
            print(dict(row))
        
        #print(al)
        return al
        
    #failed
    #return get_from_db_by_request();
    #return jsonify(dict(str(get_from_db_by_request()));

    #OK
    print('jsonify JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ' +   str(jsonify(get_from_db_by_request())))
    

    return jsonify(get_from_db_by_request());
    #return jsonify(str(get_from_db_by_request())); #bad, d3 gets arr[0] ('f,gghh,fhfh,')

"""




if __name__ == "__main__":
    app.run(debug = True)