from google.oauth2 import service_account
from pathlib import Path
from db_worker import get_key


BASE_DIR = Path(__file__).resolve().parent.parent

credentials = service_account.Credentials.from_service_account_file(str(BASE_DIR) + '/' + get_key())
