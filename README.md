# Delete Mastodon Toots
As you know there is a limitation for deleting your toots in Mastodon (https://mastodon.social/) platform. So I just wanted to make the process a little easier. 

## Get toots IDs:
open Inspect element and click on "Consol" tab and enter following lines one by one:
```
toots=document.querySelectorAll('article[data-id]');
[...toots].forEach(btn => console.log(btn.getAttribute('data-id')))
```

Just keep the IDs and delete the rest of the information. Finally you will have a list of IDs. Save the file (your_file.txt).

## Find the auth token
In Inspect element, open network tab then delete one toot from Mastodon and you can get the Auth Token from request header. It's something like: `Bearer YOUTR_TOKEN`

## Run the script
Make sure you have installed python3 on your machine. Then run it: `python3 delete_toots_mastodon.py`

## Cron job
You need to create a cron job that runs the script every 30 minute :
```
*/30 * * * * /bin/python3 /PATH/delete_toots_mastodon.py >> /PATH/delete_toots_mastodon_log
```

It will run the script every 30 minutes and keep logs in a file (delete_toots_mastodon_log).
