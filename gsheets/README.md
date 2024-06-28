# Google Sheets Integration Pack

StackStorm integration with [Google Sheets](https://workspace.google.com/products/sheets/) platform.

## Usage

1. Create a [Google Cloud](https://cloud.google.com/) account if you don't have one already.
1. Go to [APIs and Services](https://console.cloud.google.com/apis/dashboard?project=messam-409712).
1. Enable Google Sheets API.
1. Go to [credentials](https://console.cloud.google.com/apis/credentials?project=messam-409712).
1. Create a service account for the integration.
1. Create a JSON key for the service account, convert it into base64 encoding.
1. Add the key into the pack configuration as service_account_key.
1. Note the email of the service account, and add the email as a collaborator on the sheet(s) you need it to access.

## Actions

* ``get`` - Get a range of values from a sheet, check [official Google documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.spreadsheets.values.html#get) for usage.
* ``clear`` - Clear a range of values from a sheet.
* ``update`` - Update a range of values in a sheet, check [docs](https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.spreadsheets.values.html#update) for usage.
