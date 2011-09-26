import sys
import csv
import json
import urllib
import urllib2
from datetime import datetime
from optparse import OptionParser

dateformat = "%Y-%m-%d %H:%M:%S UTC"
usage = "%prog [options] yyyy-mm,yyyy-mm,... username password"
parser = OptionParser(usage=usage)
parser.add_option("", "--chapter-id", dest="chapter_id",
                  default="4", help="chapter id (default is 4 for SF)")
parser.add_option("", "--cutoff-start", dest="cutoff_start",
                  default="2000-01-01 00:00:01 UTC",
                  help="any submissions earlier than or equal to this "
                       "date will be culled. Use a format like "
                       "'2000-01-01 00:00:01 UTC'.")

(options, args) = parser.parse_args()

options.cutoff_start = datetime.strptime(options.cutoff_start, dateformat)

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
    params = dict(period_start=period.strip() + "-01",
                  period_end=period.strip() + "-01",
                  chapter_id=options.chapter_id,
                  exclude_unspecified='1')
    queryargs = urllib.urlencode(params)
    full_url = "%s?%s" % (url, queryargs)
    response = opener.open(full_url)
    reader = csv.DictReader(response)
    for row in reader:
        date = datetime.strptime(row['Date'], dateformat)
        if date > options.cutoff_start:
            rows.append(row)

print json.dumps(rows, indent=2)
