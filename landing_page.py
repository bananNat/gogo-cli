from gophish import Gophish
from gophish.models import *
import config_api
import pandas as pd
from tabulate import tabulate

# Config API
api = config_api.api

# Add Landing Page
def add_page():
    print("Add New Landing Page")
    page = Page()
    page.name = input("Page name: ")
    page_path = input("Landing page HTML path: ")
    with open(page_path, "r") as f:
        page_content = f.read()
    page.html = page_content
    page.capture_credentials = True
    page.capture_passwords = True
    page.redirect_url = input("Redirect to: ")
    result = api.pages.post(page)
    print(result.id)
    print("DONE")

# View Landing Page
def view_page():
    print("---------- LIST OF PAGE ----------")
    pages = api.pages.get()
    page_lst = []
    for page in pages:
        page_lst.append(page.as_dict())
    id_lst = [d['id'] for d in page_lst]
    name_lst = [d['name'] for d in page_lst]
    page_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(page_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Page id to view details: ")
    select_page = api.pages.get(page_id=id)
    print(select_page.as_dict())

# Delete Landing Page
def delete_page():
    print("---------- LIST OF PAGE ----------")
    pages = api.pages.get()
    page_lst = []
    for page in pages:
        page_lst.append(page.as_dict())
    id_lst = [d['id'] for d in page_lst]
    name_lst = [d['name'] for d in page_lst]
    page_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(page_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Page id to delete: ")
    status = api.pages.delete(page_id=id)
    print(status.as_dict())

