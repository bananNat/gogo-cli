from gophish import Gophish
from gophish.models import *
import config_api
import pandas as pd
from tabulate import tabulate

# Config API
api = config_api.api

# Add Campaign
def add_campaign():
    print("Add Campaign")
    campaign = Campaign()
    campaign.name = input("Campaign name: ")
    campaign.page = Page(name=input("Landing Page name: "))
    campaign.template = Template(name=input("Email Template name: "))
    campaign.smtp = SMTP(name=input("Sending Profile name: "))
    campaign.url = input("URL: ")
    campaign.groups = [Group(name=input("Group name: "))]
    result = api.campaigns.post(campaign)
    print(result.id)
    print("DONE")

# Delete Delete Campaign
def delete_campaign():
    print("---------- LIST OF CAMPAIGN ----------")
    campaigns = api.campaigns.get()
    campaign_lst = []
    for campaign in campaigns:
        campaign_lst.append(campaign.as_dict())
    id_lst = [d['id'] for d in campaign_lst]
    name_lst = [d['name'] for d in campaign_lst]
    campaign_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(campaign_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Campaign id to delete: ")
    status = api.campaigns.delete(campaign_id=id)
    print(status.as_dict())


# View result
def result_campaign():
    print("---------- LIST OF CAMPAIGN ----------")
    campaigns = api.campaigns.get()
    campaign_lst = []
    for campaign in campaigns:
        campaign_lst.append(campaign.as_dict())
    id_lst = [d['id'] for d in campaign_lst]
    name_lst = [d['name'] for d in campaign_lst]
    campaign_dict = {'id': id_lst, 'name': name_lst}
    df = pd.DataFrame(campaign_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Select
    id = input("Select Campaign id to get result: ")
    select_campaign = api.campaigns.get(campaign_id=id)
    results = select_campaign.results
    timeline = select_campaign.timeline
    
    # Print Summary Result
    res_lst = []
    for res in results:
        res_lst.append(res.as_dict())
    id_lst = [d['id'] for d in res_lst]
    fname_lst = [d['first_name'] for d in res_lst]
    lname_lst = [d['last_name'] for d in res_lst]
    mail_lst = [d['email'] for d in res_lst]
    ip_lst = [d.get('ip') if 'ip' in d else None for d in res_lst]
    status_lst = [d['status'] for d in res_lst]
    res_dict = {'id': id_lst, 'first_name': fname_lst, 'last_name': lname_lst, 'email': mail_lst, 'ip': ip_lst, 'status': status_lst}
    df = pd.DataFrame(res_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Print Timeline
    timeline_lst = []
    for time in timeline:
        timeline_lst.append(time.as_dict())
    timeline_lst.pop(0)
    time_lst = [d.get('time') if 'time' in d else None for d in timeline_lst]
    email_lst = [d.get('email') if 'email' in d else None for d in timeline_lst]
    mess_lst = [d.get('message') if 'message' in d else None for d in timeline_lst]
    
    address_lst = []
    for d in timeline_lst:
        if( 'details' in d ):
            if('address' in d.get('details',{}).get('browser',{})):
                address_lst.append(d.get('details',{}).get('browser',{}).get('address'))
            else:
                address_lst.append(None)
        else:
            address_lst.append(None)
    
    useragent_lst = []
    for d in timeline_lst:
        if( 'details' in d ):
            if('user-agent' in d.get('details',{}).get('browser',{})):
                useragent_lst.append(d.get('details',{}).get('browser',{}).get('user-agent'))
            else:
                useragent_lst.append(None)
        else:
            useragent_lst.append(None)
    
    username_lst = []
    for d in timeline_lst:
        if( 'details' in d ):
            if('username' in d.get('details',{}).get('payload',{})):
                username_lst.append(d.get('details',{}).get('payload',{}).get('username'))
            else:
                username_lst.append(None)
        else:
            username_lst.append(None)

    password_lst = []
    for d in timeline_lst:
        if( 'details' in d ):
            if('password' in d.get('details',{}).get('payload',{})):
                password_lst.append(d.get('details',{}).get('payload',{}).get('password'))
            else:
                password_lst.append(None)
        else:
            password_lst.append(None)

    timeline_dict = {'time': time_lst, 'email': email_lst, 'message': mess_lst, 'ip address': address_lst, 'username': username_lst, 'password': password_lst}
    # timeline_dict = {'time': time_lst, 'email': email_lst, 'message': mess_lst, 'ip address': address_lst, 'user-agent': useragent_lst, 'username': username_lst, 'password': password_lst}
    df = pd.DataFrame(timeline_dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))
    print("DONE")
