from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi import BackgroundTasks
from starlette.responses import JSONResponse
import os


conf = ConnectionConfig(
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD"),
    MAIL_FROM = os.environ.get("MAIL_FROM"),
    MAIL_PORT = os.environ.get("MAIL_PORT"),
    MAIL_SERVER = os.environ.get("MAIL_SERVER"),
    MAIL_FROM_NAME=os.environ.get("MAIL_FROM_NAME"),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

def sent_email(email:str, subject:str, message:str, background_tasks: BackgroundTasks):
    html = f"""<p>{message}</p> """

    message = MessageSchema(
        subject=subject,
        recipients=email,
        body=html,
        subtype=MessageType.plain)

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message,message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
