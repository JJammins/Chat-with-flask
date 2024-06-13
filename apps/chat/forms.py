from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateTimeField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime


class LoginForm(FlaskForm):
    email = StringField(
        "이메일",
        validators=[
            DataRequired("이메일을 입력해주세요."),
            Email("이메일 형식이 잘못되었습니다.")
        ]
    )
    password = PasswordField("비밀번호", validators=[DataRequired("비밀번호를 입력해주세요.")])
    submit = SubmitField("로그인")

class ChatForm(FlaskForm):
    chat = TextAreaField("메시지", validators=[DataRequired()])
    submit = SubmitField("전송")
