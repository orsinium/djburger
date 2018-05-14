from __main__ import djburger
import marshmallow


class PostMarshmallowBase(djburger.validators.bases.Marshmallow):
    name = marshmallow.fields.Str(required=True)
    mail = marshmallow.fields.Email(required=True)
    count = marshmallow.fields.Int(required=True)


@djburger.validators.wrappers.Marshmallow
class PostMarshmallowWrapped(marshmallow.Schema):
    name = marshmallow.fields.Str(required=True)
    mail = marshmallow.fields.Email(required=True)
    count = marshmallow.fields.Int(required=True)


postvalidators = [
    PostMarshmallowBase,
    PostMarshmallowWrapped,
]
