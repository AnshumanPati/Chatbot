#generation_rules
import smtplib
def sendemail(from_addr = 'rexbotbphc@gmail.com', to_addr_list = 'workdeptbot@gmail.com', subject = 'str(variables["newdfState"]["type_of_complaint"])', message = 'You have got a complaint from ID Number: variables["newdfState"]["id"], Name: variables["newdfState"]["username"] regarding variables["newdfState"]["type_of_complaint"]',
    login = 'Bot REX', password = '1234567809',
    smtpserver = 'smtp.gmail.com:587'):
    header = 'From: %s' % 'from_addr'
    header += 'To: %s' % ','.join(to_addr_list)
    header += 'Subject: %s' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


def main_function(variables):
    templateKey = ""

    if variables["newdfState"]["remind"] and (
        variables["newdfState"]["time"] or variables["newdfState"]["interval"]) and (
                            variables["newdfState"]["username"] and variables["newdfState"]["id"] and
                        variables["newdfState"]["type_of_complaint"] and variables["newdfState"]["room_number"] and
                variables["newdfState"]["hostel_complaint"] and variables["newdfState"]["food_mess"] and
        variables["newdfState"]["campus_complaint"]):
        templateKey = "pushreminder"
        messageStore = {
            "endflow": True
        }
    else:
        templateKey = "give_time_interval"
        messageStore = {
            "endflow": True
        }

    output = {
        "templateKey": templateKey
    }
    if variables["newdfState"]["hostel_complaint"]:
        templateKey = "ask_room_number"

    if variables["newdfState"]["hostel_complaint"]:
        templateKey = "hostel_options"
        templateKey = "confirmation"
        sendemail()

    if variables["newdfState"]["food_mess"]:
        templateKey = "food_options"
        templateKey = "confirmation"
        sendemail()

    if variables["newdfState"]["campus_complaint"]:
        templateKey = "campus_options"
        templateKey = "confirmation"
        sendemail()
        templateKey = "ask_user"
        if variables["newdfState"]["user_choice"] == 'yes':
            templateKey = "generic_template"
        if variables["newdfState"]["user_choice"] == 'no':
            templateKey = "user_end"

    return output
