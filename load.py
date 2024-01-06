import json


questions = [
    {
        "index": 49,
        "area": "Realistic",
        "text": "Set up and operate machines to make products"
    },
    {
        "index": 50,
        "area": "Realistic",
        "text": "Put out forest fires"
    },
    {
        "index": 51,
        "area": "Investigative",
        "text": "Invent a replacement for sugar"
    },
    {
        "index": 52,
        "area": "Investigative",
        "text": "Do laboratory tests to identify diseases"
    },
    {
        "index": 53,
        "area": "Artistic",
        "text": "Sing in a band"
    },
    {
        "index": 54,
        "area": "Artistic",
        "text": "Edit movies"
    },
    {
        "index": 55,
        "area": "Social",
        "text": "Take care of children at a day-care center"
    },
    {
        "index": 56,
        "area": "Social",
        "text": "Teach a high-school class"
    },
    {
        "index": 57,
        "area": "Enterprising",
        "text": "Sell merchandise at a department store"
    },
    {
        "index": 58,
        "area": "Enterprising",
        "text": "Manage a clothing store"
    },
    {
        "index": 59,
        "area": "Conventional",
        "text": "Keep inventory records"
    },
    {
        "index": 60,
        "area": "Conventional",
        "text": "Stamp, sort, and distribute mail for an organization"
    }
]

choices = "1, Strongly Dislike\r\n2, Dislike\r\n3, Unsure\r\n4, Like\r\n5, Strongly Like"

form_dict = {
    "name": "Form5",
    "slug": "form5",
    "is_public": False,
    "active_date_from": "2023-11-27T15:00:00Z",
    "active_date_to": "2023-12-25T15:00:00Z",
    "inactive_page_title": "Inativo",
    "inactive_page_message": "Formulário Inativo",
    "is_cloneable": True,
    "success_page_title": "Sucesso",
    "success_page_message": "Sucesso",
    "action": None,
    "form_elements": [

    ],
    "form_handlers": [
        {
            "plugin_uid": "db_store",
            "plugin_data": None
        }
    ]
}

question_to_import = []

for question in questions:
    question_to_import.append({
        "label": question["text"],
        "name": question["text"].replace(" ", "_").toLowerCase(),
        "choices": choices,
        "help_text": "",
        "initial": "",
        "required": 'true'})


with open("file2.json", "w") as file:
    # write to file
    file.write(json.dumps(question_to_import))


count = 1

for question in question_to_import:
    element = {
        "plugin_uid": "radio",
        "position": count,
        "plugin_data": json.dumps(question)
    }

    form_dict["form_elements"].append(element)

    count += 1


with open("file3.json", "w") as file:
    # write to file
    file.write(json.dumps(form_dict))
