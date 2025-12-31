from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from db.models import User


class UserModelSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = False