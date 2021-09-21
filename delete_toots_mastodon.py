import http.client
import sys,os


TOKEN = 'your_mostodon_token'
payload = ''
headers = {
  'Host': 'mastodon.social',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Authorization': 'Bearer '+ TOKEN,
}

# Path of file inculde lists of toot's ID
file_name=os.getcwd() + /TOOTS_LIST.txt

#Check if file is empty or not
if os.stat(file_name).st_size == 0:
    print("File is empty")
    exit()

# set counters
not_success = 1

# Read itmes from the txt file and create a list 
with open(file_name) as f:
    toots = f.read().splitlines()

# Delete itmes in the list
for item in toots:

    url = "/api/v1/statuses/" + item
    conn = http.client.HTTPSConnection("mastodon.social")
    conn.request("DELETE", url, payload, headers)
    res = conn.getresponse()

    if res.status == 200:
        toots.remove(item)
        not_success = 0
    else:
        not_success += 1

    print(item, res.status)

    conn.close()

    if not_success > 3:
        break
 

# Remove the current file and create a new one with updated list
os.remove(file_name) 
create_file = open(file_name,"w")
for item in toots:
    create_file.write(item +"\n")
