# clockify

## API key

For generating your Clockify API key, got to [https://clockify.me/user/settings](clockify.me/user/settings), find "API Key" section and click 'Generate'

## Workspace 

For checking your workspaces and receiving it's ID, run following command:

```
curl -H "content-type: application/json" -H "X-Api-Key: YOUR API KEY" -X GET https://api.clockify.me/api/v1/user
```
and loock for following attribute:

```
    "activeWorkspace": "XXXXXXXXXXXXXXXXXXXXXXXX",
    "defaultWorkspace": "XXXXXXXXXXXXXXXXXXXXXXXXX",

```
## Project 

For checking your project and receiving it's ID, run following command:

```
curl -H "content-type: application/json" -H "X-Api-Key: YOUR API KEY" -X GET https://api.clockify.me/api/v1/workspaces/{YOUR WORKSPACE ID}/projects
```

and loock for following attribute:
```
        "id": "XXXXXXXXXXXXXXXXXXXXXXX",
        "name": "Тестове завдання Quintagroup",
```

## Tasks 

To check status of current tasks, run following command:
```
curl -H "content-type: application/json" -H "X-Api-Key: YOUR API KEY" -X GET https://api.clockify.me/api/v1/workspaces/{YOUR WORKSPACE ID}/projects/{YOUR PROJECT ID}/tasks
```

## Generating report 

To generate report summary, send POST request to  https://reports.api.clockify.me/v1/workspaces/{YOUR WORKSPACE ID}/reports/summary 
and body should contain following: 

```
{  "dateRangeStart": "{START DATE}",
  "dateRangeEnd": "{END DATE}",
  "summaryFilter": {
    "groups": [
      "USER",
      "PROJECT",
      "TIMEENTRY"
    ]}}

```

For this command you may use POSTMAN
