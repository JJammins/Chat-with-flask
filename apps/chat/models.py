from apps.app import db
from datetime import datetime

class ChatMessage(db.Model):
    __tablename__ = "chat_message"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<ChatMessage {self.id}>"
