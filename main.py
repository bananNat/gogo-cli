from gophish import Gophish
from gophish.models import *
import sys
import help
import sending_profile
import landing_page
import email_template
import target_group
import campaign
import argparse

# Get args
usage = 'usage: %prog action [options]'
description = 'Gophish cli. Use this tool to quickly setup a phishing campaign using your gophish infrastructure.'
parser = argparse.ArgumentParser(description=description)


subparsers = parser.add_subparsers(dest='action')
# Groups
p_group_desc = '''\
Description:
    Config Target Group
'''

p_group = subparsers.add_parser('group', description=p_group_desc, formatter_class=argparse.RawDescriptionHelpFormatter, help='Manage groups.')
p_group_action = p_group.add_argument_group("Action")
p_group_action.add_argument('--add', '-a',action='store_true', dest='add', \
                     help='Add a group.')
p_group_action.add_argument('--delete', '-d' ,action='store_true', dest='delete', \
                     help='Delete a group.')
p_group_action.add_argument('--view', '-v', action='store_true', dest='view', \
                     help='View a group.')

# Pages
p_page_desc = '''\
Description:
    Config Landing Page
'''

p_page = subparsers.add_parser('page', description=p_page_desc, formatter_class=argparse.RawDescriptionHelpFormatter, help='Manage landing pages.')
p_page_action = p_page.add_argument_group("Action")
p_page_action.add_argument('--add', '-a',action='store_true', dest='add', \
                     help='Add a page.')
p_page_action.add_argument('--delete', '-d' ,action='store_true', dest='delete', \
                     help='Delete a page.')
p_page_action.add_argument('--view', '-v', action='store_true', dest='view', \
                     help='View a page.')

# Mail
p_mail_desc = '''\
Description:
    Config Email Template
'''

p_mail = subparsers.add_parser('template', description=p_mail_desc, formatter_class=argparse.RawDescriptionHelpFormatter, help='Manage email templates.')
p_mail_action = p_mail.add_argument_group("Action")
p_mail_action.add_argument('--add', '-a',action='store_true', dest='add', \
                     help='Add a template.')
p_mail_action.add_argument('--delete', '-d' ,action='store_true', dest='delete', \
                     help='Delete a template.')
p_mail_action.add_argument('--view', '-v', action='store_true', dest='view', \
                     help='View a template.')

# Profile
p_profile_desc = '''\
Description:
    Config Sending Profile
'''

p_profile = subparsers.add_parser('profile', description=p_profile_desc, formatter_class=argparse.RawDescriptionHelpFormatter, help='Manage sending profile.')
p_profile_action = p_profile.add_argument_group("Action")
p_profile_action.add_argument('--add', '-a',action='store_true', dest='add', \
                     help='Add a profile.')
p_profile_action.add_argument('--delete', '-d' ,action='store_true', dest='delete', \
                     help='Delete a profile.')
p_profile_action.add_argument('--view', '-v', action='store_true', dest='view', \
                     help='View a profile.')


# Campaign
p_campaign_desc = '''\
Description:
    Config Phishing Campaign
'''

p_campaign = subparsers.add_parser('campaign', description=p_profile_desc, formatter_class=argparse.RawDescriptionHelpFormatter, help='Manage phishing campaign.')
p_campaign_action = p_campaign.add_argument_group("Action")
p_campaign_action.add_argument('--add', '-a',action='store_true', dest='add', \
                     help='Add a campaign.')
p_campaign_action.add_argument('--delete', '-d' ,action='store_true', dest='delete', \
                     help='Delete a campaign.')
p_campaign_action.add_argument('--result', '-v', action='store_true', dest='result', \
                     help='View result of a campaign.')

args = parser.parse_args()

if( args.action == "profile" ):
    if( args.add ):
        sending_profile.add_profile()
    elif( args.view ):
        sending_profile.view_profile()
    elif( args.delete ):
        sending_profile.delete_profile()
elif( args.action == "page" ):
    if( args.add ):
        landing_page.add_page()
    elif( args.view ):
        landing_page.view_page()
    elif( args.delete ):
        landing_page.delete_page()
elif( args.action == "template" ):
    if( args.add ):
        email_template.add_template()
    elif( args.view ):
        email_template.view_template()
    elif( args.delete ):
        email_template.delete_template()
elif( args.action == "group" ):
    if( args.add ):
        target_group.add_target()
    elif( args.view ):
        target_group.view_target()
    elif( args.delete ):
        target_group.delete_target()
elif( args.action == "campaign" ):
    if( args.add ):
        campaign.add_campaign()
    elif( args.delete ):
        campaign.delete_campaign()
    elif( args.result ):
        campaign.result_campaign()
else:
    print('Type "python3 main.py -h" for more help')
