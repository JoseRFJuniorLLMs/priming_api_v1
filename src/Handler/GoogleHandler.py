import json

from fastapi import Depends, HTTPException, status
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from starlette.requests import Request
from google.auth.transport import requests
from google.oauth2 import id_token


class GoogleHandler:
    CLIENT_SECRETS = {"web": {"client_id": "495734453317-eevu5fq6rbqm376i58d39n27aai1l953.apps.googleusercontent.com",
                              "project_id": "primingv1", "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                              "token_uri": "https://oauth2.googleapis.com/token",
                              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                              "client_secret": "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",
                              "redirect_uris": ["https://priming-1532995a3138.herokuapp.com/callback"]}}
    SCOPES = ['https://www.googleapis.com/auth/userinfo.email',
              'https://www.googleapis.com/auth/userinfo.profile',
              'openid']
    REDIRECT_URI = 'https://priming-1532995a3138.herokuapp.com/callback'
    FLOW = Flow.from_client_config(

        client_config=CLIENT_SECRETS,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )

    @staticmethod
    def verify_token(token):
        """Verifica o token Google e retorna o usuário."""
        try:

            payload = id_token.verify_token(token['token'], requests.Request())
            return payload

        except Exception as e:

            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED,

                detail="Invalid Google authentication token",

            )
