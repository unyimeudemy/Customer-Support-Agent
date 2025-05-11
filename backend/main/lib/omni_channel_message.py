from typing import List, Dict, Optional
from datetime import datetime

class OmniChannelMessage1:
    def __init__(self,
                channel: str,
                sender_id: str,
                sender_name: str,
                timestamp: Optional[datetime] = None,
                content: str = ""):
        self.channel = channel
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.content = content
        self.timestamp = timestamp or datetime.now()
    
    def __repr__(self):
        return (f"OmniChannelMessage1(channel='{self.channel}', "
                f"sender_id='{self.sender_id}', sender_name='{self.sender_name}', "
                f"timestamp='{self.timestamp}', content='{self.content}')")





# class OmniChannelMessage:
#     def __init__(self,
#                  message_id: str,
#                  channel: str,
#                  sender_id: str,
#                  sender_name: str,
#                  receiver_id: str,
#                  receiver_name: Optional[str] = None,
#                  content: str = "",
#                  timestamp: Optional[datetime] = None,
#                  message_type: str = "text",
#                  status: str = "sent",
#                  platform_specific_fields: Optional[Dict[str, str]] = None,
#                  attachments: Optional[List[str]] = None,
#                  is_group_message: bool = False,
#                  priority: str = "medium",
#                  metadata: Optional[Dict[str, str]] = None,
#                  is_read: bool = False):
#         self.message_id = message_id
#         self.channel = channel
#         self.sender_id = sender_id
#         self.sender_name = sender_name
#         self.receiver_id = receiver_id
#         self.receiver_name = receiver_name
#         self.content = content
#         self.timestamp = timestamp or datetime.now()
#         self.message_type = message_type
#         self.status = status
#         self.platform_specific_fields = platform_specific_fields or {}
#         self.attachments = attachments or []
#         self.is_group_message = is_group_message
#         self.priority = priority
#         self.metadata = metadata or {}
#         self.is_read = is_read

#     def __repr__(self):
#         return (f"OmniChannelMessage(message_id={self.message_id}, channel={self.channel}, "
#                 f"sender_id={self.sender_id}, receiver_id={self.receiver_id}, content={self.content}, "
#                 f"timestamp={self.timestamp}, status={self.status}, is_read={self.is_read})")

#     def mark_as_read(self):
#         self.is_read = True

#     def mark_as_unread(self):
#         self.is_read = False