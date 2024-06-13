from flask import Blueprint, render_template, redirect, url_for, request
from apps.chat.forms import LoginForm, ChatForm
from apps.app import db
from apps.chat.models import ChatMessage
from datetime import datetime

chat = Blueprint(
    "chat",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@chat.route("/chat_list")
def chat_list():
    return render_template("chat/chat_list.html")

@chat.route("/friend")
def friends_list():
    return render_template("chat/friend_list.html")


@chat.route("/chatting_room", methods=["GET", "POST"])
def chatting_room():
    form = ChatForm()
    if form.validate_on_submit():
        # 폼에서 제출된 데이터로 새로운 채팅 메시지를 생성하고 데이터베이스에 추가합니다.
        new_message = ChatMessage(
            content=form.chat.data
        )
        db.session.add(new_message)
        db.session.commit()

        # 메시지를 추가한 후, 같은 채팅방 페이지로 리디렉션합니다.
        return redirect(url_for("chat.chatting_room"))

    # 모든 채팅 메시지를 시간 역순으로 가져옵니다.
    messages = ChatMessage.query.order_by(ChatMessage.sent_at.desc()).all()

    return render_template("chat/chatting_room.html", messages=messages, form=form)


@chat.route("/")
def login():
    form = LoginForm()
    return render_template("chat/login.html", form=form)