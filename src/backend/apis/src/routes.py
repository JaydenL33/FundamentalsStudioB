from flask import Blueprint, jsonify, request, Response, current_app
from datetime import datetime
import json
import math
import environConfig
import sqlalchemy

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
def dataCall(constructedData):
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
        engine = sqlalchemy.create_engine(URI_str)
        return engine
 
    engine = dbConnect()
    BP_06 = db.Table("BP_06", db.MetaData(), autoload=True, autoload_with=engine)
    queryset = db.select([BP_06]).limit(100)
    ResultProxy = connection.execute(queryset)
 
    return ResultProxy.fetchall()


@api.route("/")
def serverCheck():
    """Return a friendly HTTP greeting."""
    return "Server Running"

