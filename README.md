# DollarDock
API for personal finance expense tracking on web.
## Steps to run API
1. Download zip of file
2. Install python & run `pip install django`
3. run `pip install djangorestframework`
4. Go to main dollardock/ folder and open terminal
5. Run `python manage.py runserver`

## API Calls
- `localhost:8000/api/register/`: Use POST method with username, email and password in body.
example: 
`{
    "username": "john_doe",
    "email": "john.doe@example.com",
    "password": "pass123"
}`
Return: 201 (Success) | 400 (Failed)
- `localhost:8000/api/login/`: Use POST method with username and password in body.
example: 
`{
    "username": "john_doe",
    "password": "pass123"
}`
Return: 200 (Success), token: <token_id> | 400 (Failed)
- `localhost:8000/api/logout/`: Use POST method with "Authentication" : "Token token_id" in headers
Return: 200 (Success) | 400 (No credentials)
- `localhost:8000/api/account/`: Use GET method with "Authentication" : "Token token_id" in headers
Return: 200 (Success), json array of Accounts (should be one) | 404 (Account not found)
- `localhost:8000/api/account/<int:account_id>/transactions/`: Use GET method with "Authentication" : "Token token_id" in headers,
"""<int:account_id>""" replace with id of active account.
Return: 200 (Success), json array of Transactions | 404 (Account not found)
- `localhost:8000/api/account/<int:account_id>/transactions/create`: Use POST method with "Authentication" : "Token token_id" in headers,
new transaction data in body.
example:
`{
"name":"test1",
"amount":"122.00",
"date":"2023-05-16",
"payment_method":"bank_transfer",
"transaction_type":"expense"
}`
