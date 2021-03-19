# clockify

## API key

For generating your Clockify API key, got to [https://clockify.me/user/settings](clockify.me/user/settings), find "API Key" section and click 'Generate'

## Workspace 

For checking your workspaces and receiving it's ID, run following command:

```
curl -H "content-type: application/json" -H "X-Api-Key: YOUR API KEY" -X GET https://api.clockify.me/api/v1/user
```
and look for following attribute:

```
    "activeWorkspace": "XXXXXXXXXXXXXXXXXXXXXXXX",
    "defaultWorkspace": "XXXXXXXXXXXXXXXXXXXXXXXXX",

```
## Running script  

Only external library for Python we would need is ``` requests ```, so first run this command:

```
python3 pip install requests
```

To run ```clockify.py``` script, open terminal in location of script, and run following command:

```
python clockify.py YOUR_AUTH_API_KEY WORKSPACE_ID YYYY-MM-DD YYYY-MM-DD
```
Last two arguments - start date and end date for report. If run successfully - ```report.txt``` should be generated in same folder where script is located
