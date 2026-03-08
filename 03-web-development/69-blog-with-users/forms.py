# ==========================================================
# Forms Configuration
# 69 - Upgraded Blog with Authentication
# Structured, validated, production-ready forms
# ==========================================================

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# ----------------------------------------------------------
# Blog Post Form
# Used for Creating & Editing Posts
# ----------------------------------------------------------

class CreatePostForm(FlaskForm):
    title = StringField(
        "Post Title",
        validators=[DataRequired(), Length(max=250)]
    )

    subtitle = StringField(
        "Post Subtitle",
        validators=[DataRequired(), Length(max=250)]
    )

    img_url = StringField(
        "Image URL",
        validators=[DataRequired(), URL()]
    )

    body = CKEditorField(
        "Post Content",
        validators=[DataRequired()]
    )

    submit = SubmitField("Publish Post")


# ----------------------------------------------------------
# User Registration Form
# ----------------------------------------------------------

class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )

    name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(max=250)]
    )

    submit = SubmitField("Register")


# ----------------------------------------------------------
# User Login Form
# ----------------------------------------------------------

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


# ----------------------------------------------------------
# Comment Form
# ----------------------------------------------------------

class CommentForm(FlaskForm):
    comment_text = CKEditorField(
        "Leave a Comment",
        validators=[DataRequired()]
    )

    submit = SubmitField("Submit Comment")