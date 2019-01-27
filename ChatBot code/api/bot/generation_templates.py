#generation_templates
def main_function(variables):
    if variables['templateKey'] == 'pushreminder':
        output = [{"include": ["web"], "text": [""]}]
    elif (variables['templateKey'] == "give_time_interval"):
        output = [{"include": ["web"], "text": ["Give me a valid time interval"]}]
    # CAROUSAL
    {
        'include': ['facebook', 'skype'],
        "generic_template": [
            {
                "elements": [
                    {
                        "image_url": "http://www.scetwah.edu.pk/images/hostel.jpg",
                        "button": [
                            {
                                "type": "element_share"
                            }
                        ],
                        "image_url": "http://recipes.timesofindia.com/thumb/msid-49183777,width-400,resizemode-4/49183777.jpg",
                        "button": [
                            {
                                "type": "element_share"
                            }
                        ],
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQehAY4ALZlPbIP57PjwrMNSvofUW4sXylYqyN6gUH6NSn5RgWl",
                        "button": [
                            {
                                "type": "element_share"
                            }
                        ],
                        "subtitle": "subtitle text",
                        "title": "Student Complaint"
                    }
                ]
            }
        ]
    }

    # QUICK REPLY
    {
        'include': ['facebook', 'skype'],
        "text": "I am sorry to hear that. What can I help you with?",
        "quick_reply": [
            {
                "text": "Electricity",
                "quick_replies": [
                    {
                        "payload": "Electricity",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Furniture",
                "quick_replies": [
                    {
                        "payload": "Furniture",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Pests",
                "quick_replies": [
                    {
                        "payload": "Pests",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Water Filter",
                "quick_replies": [
                    {
                        "payload": "Water_Filter",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "QT Grounds",
                "quick_replies": [
                    {
                        "payload": "QT_Grounds",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Damp Walls",
                "quick_replies": [
                    {
                        "payload": "Damp_Walls",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Plumbing Issues",
                "quick_replies": [
                    {
                        "payload": "Plumbing_Issues",
                        "content_type": "text",
                        "title": "Hostel Complaint",
                        "image_url": "url"
                    }
                ]
            }
        ]
    }
    {
        'include': ['facebook', 'skype'],
        "text": "I am sorry to hear that. What can I help you with?",
        "quick_reply": [
            {
                "text": "Mess Food",
                "quick_replies": [
                    {
                        "payload": "Mess_Food",
                        "content_type": "text",
                        "title": "Mess Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Drinking Water",
                "quick_replies": [
                    {
                        "payload": "Mess_Water",
                        "content_type": "text",
                        "title": "Mess Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Food Stalls",
                "quick_replies": [
                    {
                        "payload": "Food_Stalls",
                        "content_type": "text",
                        "title": "Mess Complaint",
                        "image_url": "url"
                    }
                ]
            }
        ]
    }
    {
        'include': ['facebook', 'skype'],
        "text": "I am sorry to hear that. What can I help you with?",
        "quick_reply": [
            {
                "text": "Animals",
                "quick_replies": [
                    {
                        "payload": "Animals",
                        "content_type": "text",
                        "title": "Campus Complaint",
                        "image_url": "url"
                    }
                ],
                "text": "Internet Issues",
                "quick_replies": [
                    {
                        "payload": "Internet",
                        "content_type": "text",
                        "title": "Campus Complaint",
                        "image_url": "url"
                    }
                ]

            }
        ]
    }

    if variables['templateKey'] == 'ask_room_number':
        output = [{"text": ["Can you tell me your room number?"]}]
    if variables['templateKey'] == 'hostel_options':
        output = [{"text": ["I am sorry to hear that you are facing problems in the Hostel. What can I help you with?"]}]
    if variables['templateKey'] == 'food_options':
            output = [{"text": ["I am sorry to hear that you are facing problems in the food facilities available here. What can I help you with?"]}]
    if variables['templateKey'] == 'campus_options':
                output = [{"text": ["I am sorry to hear that you are facing problems. What can I help you with?"]}]
    if variables['templateKey'] == 'confirmation':
            output = [{"text": ["We have sent an email to the concerned authority. We regret the inconvenience caused. Would you like to lodge any more complaint?"]}]
    if variables['templateKey'] == 'user_end':
            output = [{"text": ["Thank you! Have a nice day."]}]

    return output