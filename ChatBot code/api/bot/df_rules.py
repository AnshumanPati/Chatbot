#df_rules
def main_function(variables):
    df = {
    "username":None,
	"id":None,
	"type_of_complaint":None,
	"room_number":None,
	"hostel_complaint": None,
	"food_mess": None,
	"campus_complaint": None,
	"remind":None,
	"user_hostel":None,
   	"time":None,
   	"interval":None,
  	"user_choice":None,
    "message":None
    }

    if "dataStore" in variables and variables["dataStore"] and "endflow" in variables["dataStore"] and \
            variables["dataStore"]["endflow"]:
        datastore = variables["dataStore"]
    else:
        datastore = {"endflow": True}

    if datastore["endflow"]:
        newdf = df
    else:
        newdf = variables["lastdfState"]

    if "custom_ners" in variables["nlp"] and "remind" in variables["nlp"]["custom_ners"]:
        newdf["remind"] = True
    if "datetime" in variables["nlp"] and variables["nlp"]["datetime"]:
        newdf["time"] = variables["nlp"]["datetime"]["time"]
    if "numbers" in variables["nlp"] and variables["nlp"]["numbers"]:
        newdf["interval"] = variables["nlp"]["numbers"][0]


    output={"df":newdf,"dataStore":datastore}
    return output