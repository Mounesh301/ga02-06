import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

data =[
    {
        "name": "76CScRD",
        "marks": 68
    },
    {
        "name": "5rsez0E",
        "marks": 58
    },
    {
        "name": "g5f9xs",
        "marks": 72
    },
    {
        "name": "G",
        "marks": 40
    },
    {
        "name": "4KdO8sBMSJ",
        "marks": 67
    },
    {
        "name": "dY1Hd",
        "marks": 58
    },
    {
        "name": "U0du6",
        "marks": 20
    },
    {
        "name": "jIs",
        "marks": 14
    },
    {
        "name": "V",
        "marks": 7
    },
    {
        "name": "oi935h07",
        "marks": 66
    },
    {
        "name": "M",
        "marks": 53
    },
    {
        "name": "il4Oc",
        "marks": 84
    },
    {
        "name": "ggttt",
        "marks": 7
    },
    {
        "name": "yUdCxge",
        "marks": 97
    },
    {
        "name": "DiGuG1Wdo",
        "marks": 66
    },
    {
        "name": "guiEGoYojP",
        "marks": 78
    },
    {
        "name": "iZhbMLR",
        "marks": 54
    },
    {
        "name": "MrBZd1",
        "marks": 97
    },
    {
        "name": "8",
        "marks": 98
    },
    {
        "name": "T423A",
        "marks": 22
    },
    {
        "name": "9dgI",
        "marks": 79
    },
    {
        "name": "xvZRd0ZfP",
        "marks": 36
    },
    {
        "name": "ctG6gVK8bk",
        "marks": 28
    },
    {
        "name": "l0",
        "marks": 38
    },
    {
        "name": "sTSbQ",
        "marks": 57
    },
    {
        "name": "gkcwCZ",
        "marks": 5
    },
    {
        "name": "F",
        "marks": 17
    },
    {
        "name": "qWIW",
        "marks": 1
    },
    {
        "name": "N2x",
        "marks": 78
    },
    {
        "name": "09TeM",
        "marks": 80
    },
    {
        "name": "FG3sBDA",
        "marks": 83
    },
    {
        "name": "n7ruE3fof",
        "marks": 43
    },
    {
        "name": "OSVYPZRJdj",
        "marks": 0
    },
    {
        "name": "7I6Y9MDg",
        "marks": 15
    },
    {
        "name": "9lSJCeOy5I",
        "marks": 62
    },
    {
        "name": "jZYFEkNU8h",
        "marks": 64
    },
    {
        "name": "alBh",
        "marks": 80
    },
    {
        "name": "iQAIRs23IU",
        "marks": 48
    },
    {
        "name": "NBuM",
        "marks": 68
    },
    {
        "name": "FD1r",
        "marks": 30
    },
    {
        "name": "9EDFuQ",
        "marks": 26
    },
    {
        "name": "FdcLTfC8E",
        "marks": 47
    },
    {
        "name": "qQMd",
        "marks": 74
    },
    {
        "name": "SC",
        "marks": 0
    },
    {
        "name": "1NUH2dLJG",
        "marks": 46
    },
    {
        "name": "pp8v",
        "marks": 21
    },
    {
        "name": "UfZ",
        "marks": 0
    },
    {
        "name": "04",
        "marks": 94
    },
    {
        "name": "um5t",
        "marks": 11
    },
    {
        "name": "J7Vz",
        "marks": 52
    },
    {
        "name": "Lc08uK2jvR",
        "marks": 52
    },
    {
        "name": "fI",
        "marks": 12
    },
    {
        "name": "nOD",
        "marks": 81
    },
    {
        "name": "0",
        "marks": 35
    },
    {
        "name": "SYT2g",
        "marks": 50
    },
    {
        "name": "UB",
        "marks": 75
    },
    {
        "name": "DGNtW1PWN",
        "marks": 10
    },
    {
        "name": "x9rvIMD3",
        "marks": 71
    },
    {
        "name": "Y",
        "marks": 61
    },
    {
        "name": "Ce7Bry",
        "marks": 56
    },
    {
        "name": "NbWK0j",
        "marks": 55
    },
    {
        "name": "wtDYZfgF",
        "marks": 77
    },
    {
        "name": "xuF1",
        "marks": 58
    },
    {
        "name": "h",
        "marks": 17
    },
    {
        "name": "8yviy",
        "marks": 91
    },
    {
        "name": "S04PO8Ltc",
        "marks": 92
    },
    {
        "name": "FhBpQSK",
        "marks": 22
    },
    {
        "name": "t0YWTmG",
        "marks": 41
    },
    {
        "name": "sBrOCkE",
        "marks": 15
    },
    {
        "name": "z",
        "marks": 15
    },
    {
        "name": "IsP73",
        "marks": 91
    },
    {
        "name": "uwEUj",
        "marks": 1
    },
    {
        "name": "Jhwd1UP",
        "marks": 64
    },
    {
        "name": "6",
        "marks": 27
    },
    {
        "name": "S",
        "marks": 44
    },
    {
        "name": "e",
        "marks": 39
    },
    {
        "name": "VVjJyzStU",
        "marks": 34
    },
    {
        "name": "K4",
        "marks": 78
    },
    {
        "name": "b3P",
        "marks": 62
    },
    {
        "name": "3lGNU",
        "marks": 92
    },
    {
        "name": "D",
        "marks": 38
    },
    {
        "name": "yjQj0e",
        "marks": 31
    },
    {
        "name": "5Ub8Z",
        "marks": 33
    },
    {
        "name": "ROWCQAo",
        "marks": 58
    },
    {
        "name": "p86",
        "marks": 19
    },
    {
        "name": "pWAEM8",
        "marks": 70
    },
    {
        "name": "WPUiDZeL",
        "marks": 42
    },
    {
        "name": "Ji03BgbJu",
        "marks": 2
    },
    {
        "name": "r",
        "marks": 98
    },
    {
        "name": "J",
        "marks": 76
    },
    {
        "name": "0TgByU5cKz",
        "marks": 17
    },
    {
        "name": "q",
        "marks": 97
    },
    {
        "name": "mSL4YbnL1",
        "marks": 58
    },
    {
        "name": "FmP6",
        "marks": 82
    },
    {
        "name": "v6v4",
        "marks": 18
    },
    {
        "name": "9dXfs",
        "marks": 0
    },
    {
        "name": "C",
        "marks": 7
    },
    {
        "name": "AZSz1T",
        "marks": 57
    },
    {
        "name": "55uz0wPza",
        "marks": 32
    },
    {
        "name": "7WJ2pCN",
        "marks": 18
    }
]
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters from the URL
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get('name', [])  # Extract 'name' parameters as a list

        # Filter and maintain order based on the 'name' parameters
        if names:
            filtered_data = []
            for name in names:
                for item in data:
                    if item['name'] == name:
                        filtered_data.append(item)
                        break
        else:
            filtered_data = data  # Return all data if no filter is provided

        # Extract marks into a list while maintaining the order
        marks_list = [item["marks"] for item in filtered_data]

        # Respond with only the JSON object
        response = {"marks": marks_list}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
