from st2common.runners.base_action import Action
import json, base64

from apiclient import discovery
from google.oauth2 import service_account

class Clear(Action):
    def __init__(self, config=None, action_service=None):
        super(Clear, self).__init__(
            config=config, action_service=action_service
        )
        client_secret = json.loads(base64.b64decode(config.get('service_account_key')))
        credentials = service_account.Credentials.from_service_account_info(client_secret)
        self._service = discovery.build('sheets', 'v4', credentials=credentials)

    def run(self, spreadsheet_id, range):
        self._service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=range).execute()

