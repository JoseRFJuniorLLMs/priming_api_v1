from fastapi import APIRouter, HTTPException, Depends, status
from datetime import timedelta

from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.Model.Login import Login
from src.Service.LoginService import LoginService
from src.Handler.GoogleHandler import GoogleHandler

app = APIRouter()

"""
fastapi: Módulos essenciais para construir a API com o framework FastAPI.
datetime: timedelta será usado para gerenciar as durações dos tokens de acesso.
starlette: Permite gerenciar as requests HTTP e suas respostas.
src.Model.Login: Provavelmente contém a definição do modelo de dados "Login", representando as credenciais de usuário.
src.Service.LoginService: Provavelmente um serviço com métodos para autenticação, criação de tokens e logout.
src.Handler.GoogleHandler: Provavelmente contém a lógica de integração com a autenticação do Google (OAuth).
"""


"""
/login (POST):
Recebe as credenciais do usuário (login_data).
Chama a função LoginService.login() para validar o login.
Se bem-sucedido:
Gera um token de acesso usando LoginService.create_access_token().
Armazena o token na sessão do usuário.
Retorna o token de acesso e o tipo de token.
Se não for bem-sucedido:
Lança uma HTTPException (com status 401 - Unauthorized).
"""
@app.post("/login")
async def login(login_data: Login, request: Request):
    user = await LoginService.login(login_data)

    if user:
        access_token_expires = timedelta(days=LoginService().ACCESS_TOKEN_EXPIRE_DAYS)
        access_token = LoginService().create_access_token(data={"sub": login_data.username},
                                                          expires_delta=access_token_expires)
        request.session["Authorization"] = access_token
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


""""
/logout (GET):

Chama a função LoginService.logout() para invalidar a sessão do usuário.
"""


@app.get("/logout")
async def logout(request: Request):
    return await LoginService.logout(request=request)


"""
/auth (GET):

Inicia o processo de autenticação no Google OAuth:
Usa a função GoogleHandler.FLOW.authorization_url() para gerar o URL de autorização do Google.
Armazena o "state" (valor aleatório) na sessão para mitigar ataques CSRF.
Redireciona o usuário para o URL de autorização do Google.
"""


@app.get("/auth")
async def start_google_auth(request: Request):
    authorization_url, state = GoogleHandler.FLOW.authorization_url()
    request.session["state"] = state
    return RedirectResponse(authorization_url)


"""
/callback (GET):

Endpoint de retorno do Google OAuth, chamado após o usuário autenticar com sucesso.
Compara o "state" recebido com aquele da sessão para validação.
Usa o GoogleHandler.FLOW.fetch_token() para trocar o código de autorização pelo token de acesso do Google.
Armazena o token na sessão do usuário.
Retorna uma mensagem de sucesso.
"""


@app.get("/callback")
async def google_auth_callback(request: Request, state: str, code: str):
    if state != request.session.get("state"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid state",
        )

    GoogleHandler.FLOW.fetch_token(code=code)
    credentials = GoogleHandler.FLOW.credentials

    request.session["token"] = credentials.to_json()

    return {"message": "Authentication successful"}


"""
/ (GET):

Rota "raiz", provavelmente apenas para teste. Retorna uma mensagem simples.
"""


@app.get("/")
async def index():
    log().info("Welcome!!")
    return {"message": "hello world"}
