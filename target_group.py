from gophish import Gophish
from gophish.models import *
import config_api
import csv
import pandas as pd
from tabulate import tabulate

# Config API
api = config_api.api

# Read csv file
def read_csv_file(filename):
    rows = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            rows.append(tuple(row))
    return rows

# Add Target Group
def add_target():
    print("Add Group Target")
    group = Group()
    group.name = input("Group name: ")
    group_path = input("Input Target Group CSV file path: ")
    group_content = read_csv_file(group_path)
    targets = []
    for target in group_content:
        targets.append(User(first_name=target[0], last_name=target[1], email=target[2]))
    group.targets = targets
    result = api.groups.post(group)
    print(result.id)
    print("DONE")

# View Sending Profile
def view_target():
    print("---------- LIST OF TARGET ----------")
    groups = api.groups.get()
    group_lst = []
    for group in groups:
        group_lst.append(group.as_dict())
    id_lst = [d['id'] for d in group_lst]
    name_lst = [d['name'] for d in group_lst]
    group_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(group_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Group id to view details: ")
    select_group = api.groups.get(group_id=id)
    print(select_group.as_dict())

# Delete Sending Profile
def delete_target():
    print("---------- LIST OF TARGET ----------")
    groups = api.groups.get()
    group_lst = []
    for group in groups:
        group_lst.append(group.as_dict())
    id_lst = [d['id'] for d in group_lst]
    name_lst = [d['name'] for d in group_lst]
    group_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(group_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Group id to delete: ")
    status = api.groups.delete(group_id=id)
    print(status.as_dict())
