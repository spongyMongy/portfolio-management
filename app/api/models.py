from tortoise.models import Model
from tortoise import fields

class PortfolioItem(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
