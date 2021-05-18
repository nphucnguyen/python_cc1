employee = {}
employee[1] = {
    'ID': 1,
    'Name': 'Ha',
    'Day of Birth' : '12/09/90',
    'Birthplace' : 'Ha'
}
employee[2] = {
    'ID': 2,
    'Name': 'Nguyen',
    'Day of Birth' : '25/04/95',
    'Birthplace' : 'Binh Dinh'
}
import json
s = json.dumps(employee)
print(s)
