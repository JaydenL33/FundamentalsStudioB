from flask import Blueprint, jsonify, request, Response, current_app
from datetime import datetime
import json
import math
import environConfig
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

api = Blueprint("api", __name__)

@api.route("/test", methods=["GET", "POST"])
def testFunction():

	req = request.json
	res = {
	"successful": True,
	"date": str(datetime.now()),
	"text": [],
	}

	for i in range(10):
		res["text"].append(
		{
		"name": "Jayden",
		"count": i,
		}
		)

	res = json.dumps(res)
	return Response(res, status=200, mimetype="application/json")

 
@api.route("/data", methods=["GET"])
def dataCall():
    # req = request.json
 
    res = {
    "successful": True,
    "data": [],
    }
 
    res["data"] = puller()
 
    # for i in range(len(constructedData)):
    #   res["data"].append(constructedData[i])
 
    res = json.dumps(res) # json serializer
    return Response(res, status=200, mimetype="application/json")
 
 
def puller():
    def dbConnect():
        # pull sensitive settings from local.env for database login
        env = environConfig.safe_environ()
        URI_str = env("DB_URI")
        engine = db.create_engine(URI_str)
        return engine
    
    # create a session with our engine
    engine = dbConnect()
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    # connect the engine
    connection = engine.connect()
    # create a query with the current session
    # Create a definition of the existing table for sqlalchemy
    COVID19 = db.Table("COVID19", db.MetaData(), autoload=True, autoload_with=engine)
    queryset = session.query(COVID19).limit(100).all()
    # queryset = db.select([BP_06]).limit(100)
    # ResultProxy = connection.execute(queryset)

    return queryset

@api.route("/")
def serverCheck():
    """Return a friendly HTTP greeting."""
    return "Server Running"