from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, ValidationError


# def imageurl(form, field):
#     image_url = field.data
#     print(image_url, '=================================================')
#     if image_url and not image_url.endswith(('.jpg', '.png', '.jpeg','.gif')):
#         raise ValidationError("Enter valid image url ending with .jpg, .png, .jpeg, or .gif")
#     if image_url and not image_url.startswith('https'):
#         raise ValidationError("Enter valid image url")

class CommentForm(FlaskForm):


    image = TextField('image')
    comment = TextField('tweet', validators=[DataRequired(message='Must insert a reply')])
    user_id = IntegerField('user_id')
    post_id = IntegerField('post_id')
    username = StringField('username')
    profile_pic = TextField('profile_pic')
    created_at = DateTimeField('created_at')
