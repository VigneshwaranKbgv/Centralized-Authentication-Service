from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from ..core.config import settings
from pathlib import Path
import ssl

# Create email templates directory if it doesn't exist
email_templates_dir = Path(__file__).parent / 'email_templates'
email_templates_dir.mkdir(parents=True, exist_ok=True)

# Create SSL context
ssl_context = ssl.create_default_context()

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD.replace(" ", ""),  # Remove spaces from password
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=465,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=str(email_templates_dir),
    TIMEOUT=60  # Increased timeout
)

async def send_reset_email(email: str, token: str):
    try:
        print(f"Attempting to send email to {email} with settings:")
        print(f"Username: {settings.MAIL_USERNAME}")
        print(f"Server: {settings.MAIL_SERVER}:{settings.MAIL_PORT}")
        
        reset_link = f"http://localhost:3000/reset-password/{token}"
        
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #4285f4;">Password Reset Request</h2>
                    <p>You have requested to reset your password. Click the button below to proceed:</p>
                    <a href="{reset_link}" 
                       style="display: inline-block; 
                              background-color: #4285f4; 
                              color: white; 
                              padding: 12px 24px; 
                              text-decoration: none; 
                              border-radius: 4px; 
                              margin: 20px 0;">
                        Reset Password
                    </a>
                    <p style="color: #666;">If you didn't request this, please ignore this email.</p>
                    <p style="color: #666;">This link will expire in 30 minutes.</p>
                </div>
            </body>
        </html>
        """
        
        message = MessageSchema(
            subject="Password Reset Request",
            recipients=[email],
            body=html_content,
            subtype="html"
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return False 

async def send_verification_code(email: str, code: str):
    try:
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #4285f4;">Password Reset Code</h2>
                    <p>Your verification code is:</p>
                    <h1 style="color: #4285f4; font-size: 32px; letter-spacing: 5px;">{code}</h1>
                    <p style="color: #666;">This code will expire in 10 minutes.</p>
                    <p style="color: #666;">If you didn't request this code, please ignore this email.</p>
                </div>
            </body>
        </html>
        """
        
        message = MessageSchema(
            subject="Password Reset Code",
            recipients=[email],
            body=html_content,
            subtype="html"
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False 