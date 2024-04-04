from dotenv import load_dotenv
import os

load_dotenv()


CREDENTIAL = {
  "type": os.getenv('TYPE'),
  "project_id": str(os.getenv('PROJECT_ID')),
  "private_key_id": os.getenv('PRIVATE_KEY_ID'),
  "private_key": str(os.getenv('PRIVATE_KEY')),
  "client_email": os.getenv('CLIENT_EMAIL'),
  "client_id": os.getenv('CLIENT_ID'),
  "auth_uri": os.getenv('AUTH_URI'),
  "token_uri": os.getenv('TOKEN_URI'),
  "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
  "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL'),
  "universe_domain": os.getenv('UNIVERSE_DOMAIN')
}

