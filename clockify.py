import argparse
import requests
import datetime
import json

parser = argparse.ArgumentParser()
parser.add_argument('auth', type=str)
parser.add_argument('work', type=str)
parser.add_argument('startdate', type=datetime.date.fromisoformat)
parser.add_argument('enddate', type=datetime.date.fromisoformat)


def main():
    args = parser.parse_args()

    startdate = datetime.datetime(args.startdate.year, args.startdate.month,
                                  args.startdate.day).isoformat()
    enddate = datetime.datetime(args.enddate.year, args.enddate.month,
                                args.enddate.day).isoformat()

    auth_api_key = args.auth
    workspace_id = args.work

    url = "https://reports.api.clockify.me/v1/workspaces/" \
          f"{workspace_id}/reports/detailed"

    headers = {"X-Api-Key": auth_api_key}

    payload = {"dateRangeStart": f'{startdate}',
               "dateRangeEnd": f'{enddate}',
               "detailedFilter": {
                                    "page": 1,
                                    "pageSize": 50,
                                    "sortColumn": "DATE"}}

    response = requests.post(url, headers=headers, json=payload)

    print(response.json())

    with open('report.txt', 'w', encoding='utf8') as outfile:
        json.dump(response.json(), outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
