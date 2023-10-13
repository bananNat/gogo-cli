from gophish import Gophish
from gophish.models import *
import config_api
import pandas as pd
from tabulate import tabulate

# Config API
api = config_api.api

# Add Email Template
def add_template():
    print("Add Email Template")
    template = Template()
    template.name = input("Template name: ")
    template.subject = input("Email subject: ")
    mail_path = input("Email template HTML path: ")
    with open(mail_path, "r") as f:
        email_content = f.read()
    template.html = email_content
    result = api.templates.post(template)
    print(result.id)
    print("DONE")

# View Email Template
def view_template():
    print("---------- LIST OF TEMPLATE ----------")
    templates = api.templates.get()
    template_lst = []
    for template in templates:
        template_lst.append(template.as_dict())
    id_lst = [d['id'] for d in template_lst]
    name_lst = [d['name'] for d in template_lst]
    template_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(template_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Template id to view details: ")
    select_template = api.templates.get(template_id=id)
    print(select_template.as_dict())

# Delete Email Template
def delete_template():
    print("---------- LIST OF TEMPLATE ----------")
    templates = api.templates.get()
    template_lst = []
    for template in templates:
        template_lst.append(template.as_dict())
    id_lst = [d['id'] for d in template_lst]
    name_lst = [d['name'] for d in template_lst]
    template_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(template_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Template id to delete: ")
    status = api.templates.delete(template_id=id)
    print(status.as_dict())