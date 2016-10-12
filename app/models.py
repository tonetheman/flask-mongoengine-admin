import mongoengine
from app import db
import datetime


class Category(db.Document):
    title = db.StringField(default='')

class Tag(db.Document):
    title = db.StringField(default='')

class Item(db.Document):
    title = db.StringField(default='')
    description = db.StringField(default='')
    category = db.ReferenceField('Category')
    tags = db.ListField(db.ReferenceField('Tag', reverse_delete_rule=mongoengine.PULL))
    created_at = db.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = datetime.datetime.now()
        return super(Item, self).save(*args, **kwargs)
