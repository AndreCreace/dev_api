# Let´s import the Python extensions
from flask import Flask, request
from flask_restful import Resource, Api
import json

# Let´s import our classes
from skills import Skills_CR, Skills_UD

# Let´s create the our app
app = Flask(__name__)

# Let´s instantiate the Api object
api = Api(app)

# Let´s create a list of developers
developers = [
    {"id":0, "name":"Andre", "skills":["Python","Django","Flask","Pandas","sql"]},
    {"id":1, "name":"Gabi", "skills":["Python","Sql","Oracle","Git"]},
    {"id":2, "name":"Weverton", "skills":["VBA","Sql","Oracle",".Net"]}
]

# Let´s create the developer class
class Developer(Resource):

    # Method GET
    def get(self, id):
        try:
            response = developers[id]

        except IndexError as e:
            message = "There isn´t developer for the ID {}".format(id)  # Let´s define the return´s message
            response = {"status":"error", "message":message}

        except Exception as e:
            message = "{}".format(str(e))  # Let´s define the return´s message
            response = {"status":"error", "message":message}

        return response

    # Method PUT
    def put(self, id):
        data = json.loads(request.data) # Let´s catch the request
        developers[id] = data # Let´s update the developers list values
        return data

    # Method DELETE
    def delete(self, id):
        developers.pop(id) # Let´s delete the list´s developers item
        return {"return": "success",
                "message": "Register was deleted!"}

    # method DELETE
    def delete(self, id):
        developers.pop(id)  # Let´s delete the list´s developers item
        return {"return": "success",
                "message": "Register was deleted!"}

# Let´s create a class for create new developers, and retur a list of all them
class List_Developers(Resource):

    # Method POST (Add new developer)
    def post(self):
        try:
            data = json.loads(request.data) # Let´s recive the requets body
            newID = len(developers) # Let´s define the new developer´s id
            data["id"] = newID # Let´s set id
            developers.append(data) # Let´s add the new developer in the list
            return {"status":"success",
                    "message": developers[newID]}

        except Exception as e:
            message = "{}".format(str(e))  # Let´s define the message returns
            return {"status": "failure",
                    "message": message}

    # Method GET, to retur the list of all developers
    def get(self):
        try:
            return {"status":"success",
                    "message": developers} # Let´s return a list all the developers

        except Exception as e:
            message = "{}".format(str(e)) # Let´s define the message of return

            return {"staus":"Failure",
                    "message":message}

# Let´s add the resources and define the routes
api.add_resource(Developer,"/dev/<int:id>")
api.add_resource(List_Developers,"/dev")
api.add_resource(Skills_CR,"/dev_skills_CR")
api.add_resource(Skills_UD,"/dev_skills_UD/<int:position_list>")

# Let´s check who´s calling the app
if __name__ == "__main__":
    app.run(debug=True)