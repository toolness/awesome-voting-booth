import sys
import csv
import json
import urllib
import urllib2
from optparse import OptionParser

usage = "%prog [options] yyyy-mm,yyyy-mm,... username password"
parser = OptionParser(usage=usage)
parser.add_option("", "--chapter-id", dest="chapter_id",
                  default="4", help="chapter id (default is 4 for SF)")

(options, args) = parser.parse_args()

url = "http://awesomefoundation.org/submissions.csv"

if len(args) != 3:
    parser.print_help()
    sys.exit(1)

(periods, username, password) = args

periods = periods.split(',')
periods.reverse()

passwords = urllib2.HTTPPasswordMgr()
passwords.add_password('Application', url, username, password)
handler = urllib2.HTTPBasicAuthHandler(passwords)
opener = urllib2.build_opener(handler)

rows = []

for period in periods:
    params = dict(period=period.strip(),
                  chapter_id=options.chapter_id,
                  exclude_unspecified='1')
    queryargs = urllib.urlencode(params)
    full_url = "%s?%s" % (url, queryargs)
    response = opener.open(full_url)
    reader = csv.DictReader(response)
    rows.extend([row for row in reader])

print json.dumps(rows, indent=2)
