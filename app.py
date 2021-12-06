# Let´s import Flask
from flask import Flask, jsonify, request

# Let´s import json
import json

# Let´s create our app
app = Flask(__name__)

# Let´s create a list of developers
developers = [
    {"id":0, "name":"Andre", "skills":["Python","Django","Flask","Pandas","sql"]},
    {"id":1, "name":"Gabi", "skills":["Python","Sql","Oracle","Git"]},
    {"id":2, "name":"Weverton", "skills":["VBA","Sql","Oracle",".Net"]}
]

# Let´s create the function to return, update or delete some developer
# Let´s recive by parameter the developer´s id
@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def developer(id):

    # Let´s validate the request method (Get)
    if request.method == "GET":

        # Local variables
        message = ""
        response = ""
        status = ""

        try:
            # Let´s recive the developer´s information trought id (developers list position)
            response = developers[id]

        except IndexError as e:

            # Let´s define the return´s message
            message = "There isn´t developer for the ID {}".format(id)
            response = {"status":"error", "message":message}

        except Exception as e:

            # Let´s define the return´s message
            message = "{}".format(str(e))
            response = {"status":"error", "message":message}

        # Function return
        return jsonify(response)

    # The requets method is PUT (Update)
    elif request.method == "PUT":

        # Let´s catch the body request
        dataRequestJsonBody = json.loads(request.data)

        # Let´s update the lis developers values
        developers[id] = dataRequestJsonBody

        # Function return
        return jsonify(dataRequestJsonBody)

    # The request methodo is DELETE (Delete)
    elif request.method == "DELETE":

        # Let´s delete the list´s developers item
        developers.pop(id)

        # Let´s return
        return jsonify({"return":"success",
                        "message":"Register was deleted!"})


# Let´s create a function to create a new developer, and return a list of all them
@app.route("/dev/", methods=["POST", "GET"])
def list_developers():

    # Local variables
    dataRequestJsonBody = ""
    message= ""

    # Let´s check the request type
    if request.method == "POST":

        try:

            # Let´s recive the requets body
            dataRequestJsonBody = json.loads(request.data)

            # Let´s define the new developer´s id
            newID = len(developers)
            dataRequestJsonBody["id"] = newID

            # Let´s add the new developer in the list
            developers.append(dataRequestJsonBody)

            # Let´s define the message returns
            return jsonify(developers[newID])

        except Exception as e:

            # Let´s define the message returns
            message = "{}".format(str(e))

            # Let´s return
            return jsonify({"return":"failure",
                           "message": message})


    # Let´s make a list of developers
    elif request.method == "GET":

        try:

            # Let´s return a list all the developers
            return jsonify(developers)

        except Exception as e:

            # Let´s define the message of return
            message = "{}".format(str(e))

            return jsonify({"Staus":"Failure",
                           "message":message})

# Let´s validate who´s the call main
if __name__ == "__main__":

    # Let´s execute our app
    app.run(debug=True)