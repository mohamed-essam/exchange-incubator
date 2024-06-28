from st2common.runners.base_action import Action
import json, base64

from apiclient import discovery
from google.oauth2 import service_account

class Append(Action):
    def __init__(self, config=None, action_service=None):
        super(Append, self).__init__(
            config=config, action_service=action_service
        )
        client_secret = json.loads(base64.b64decode(config.get('service_account_key')))
        credentials = service_account.Credentials.from_service_account_info(client_secret)
        self._service = discovery.build('sheets', 'v4', credentials=credentials)

    def run(self, spreadsheet_id, range, values, value_input_option, insert_data_option=None, major_dimension=None, response_value_render_option=None, include_values_in_response=False):
        data = self._service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range, body={
            "majorDimension": major_dimension,
            "range": range,
            "values": values
        }, includeValuesInResponse=include_values_in_response, insertDataOption=insert_data_option, valueInputOption=value_input_option, responseValueRenderOption=response_value_render_option).execute()
        return {"data": data}
