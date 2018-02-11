TEXT
{'text': ['Hi', 'Hey'],'include':['facebook','skype']}

IMAGE
{
'include':['facebook','skype'],
    "image": [
        {
            "url": "welcome.jpg"
        }
    ]
}


QUICK REPLY
{
'include':['facebook','skype'],
    "quick_reply": [
        {
            "text": "some text here",
            "quick_replies": [
                {
                    "payload": "payload string",
                    "content_type": "text",
                    "title": "title",
                    "image_url":"url"
                }
            ]
        }
    ]
}


CAROUSAL  
{
'include':['facebook','skype'],
    "generic_template": [
        {
            "elements": [
                {
                    "image_url": "url of image",			
                    "button": [			
                        {
                            "type": "element_share"
                        }
                    ],
                    "subtitle": "subtitle text",			
                    "title": "title"
                }
            ]
        }
    ]
}


FILE
{
    "file": [
        {
            "url": "url.now"
        }
    ]
}


AUDIO

{
    "audio": [
        {
            "url": "hi.mp3"
        },
        {
            "url": "hey.mp3"
        }
    ]
}

BUTTON TEMPLATE

{
	"button_template": [{
		"text": "your text goes here",
		"button": [{
			"type": "type of the button",
			"title": "title of the button",
			"payload": "payload goes here"
		}]
	}]
}