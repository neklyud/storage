from tortoise import fields, models
from uuid import uuid4
from datetime import datetime


class Wallets(models.Model):
    guid = fields.UUIDField(pk=True, default=uuid4)
    name = fields.TextField(null=True)
    address = fields.TextField(null=False)
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.utcnow)
    updated_at = fields.DatetimeField(auto_now_add=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.guid}|{self.name}'