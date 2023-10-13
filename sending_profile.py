from gophish import Gophish
from gophish.models import *
import config_api
import pandas as pd
from tabulate import tabulate

# Config API
api = config_api.api

# Add Sending Profile
def add_profile():
    print("Add Sending Profile")
    profile = SMTP()
    profile.name = input("Profile name: ")
    profile.host = input("Host: ")
    profile.from_address = input("SMTP From: ")
    profile.username = input("Username: ")
    profile.password = input("Password: ")
    profile.ignore_cert_errors = True
    profile.interface_type = "SMTP"
    result = api.smtp.post(profile)
    print(result.id)
    print("DONE")

# View Sending Profile
def view_profile():
    print("---------- LIST OF PROFILE ----------")
    profiles = api.smtp.get()
    profile_lst = []
    for profile in profiles:
        profile_lst.append(profile.as_dict())
    id_lst = [d['id'] for d in profile_lst]
    name_lst = [d['name'] for d in profile_lst]
    profile_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(profile_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Profile id to view details: ")
    select_profile = api.smtp.get(smtp_id=id)
    print(select_profile.as_dict())

# Delete Sending Profile
def delete_profile():
    print("---------- LIST OF PROFILE ----------")
    profiles = api.smtp.get()
    profile_lst = []
    for profile in profiles:
        profile_lst.append(profile.as_dict())
    id_lst = [d['id'] for d in profile_lst]
    name_lst = [d['name'] for d in profile_lst]
    profile_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(profile_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Profile id to delete: ")
    status = api.smtp.delete(smtp_id=id)
    print(status.as_dict())
