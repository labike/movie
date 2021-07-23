'''
Author: your name
Date: 2021-07-15 19:47:49
LastEditTime: 2021-07-21 15:28:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /flask-movies/app/admin/forms.py
'''
# coding: utf8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

class LoginForm(FlaskForm):
    """
    登录
    """
    account = StringField(
        label='账号',
        validators=[DataRequired('请输入账号')],
        description='账号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号',
            # 'required': 'required'
        }
    )

    pwd = PasswordField(
        label='密码',
        validators=[DataRequired('请输入密码')],
        description='密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码',
            # 'required': 'required'
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat',
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('账号不存在')