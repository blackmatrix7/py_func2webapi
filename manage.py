#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/28 20:48
# @Author  : Matrix
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
import os
from app import create_app
from app.database import db
from app.database.models import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

__author__ = 'blackmatrix'


cfg_name = os.environ.get('APIZEN_CFG', 'default')
flask_app = create_app(cfg_name)
migrate = Migrate(flask_app, db)
manager = Manager(flask_app)
manager.add_command('db', MigrateCommand)


@manager.command
def devserver():
    flask_app.run()


@manager.command
def initadmin(name, password):
    admin = User(user_name=name)
    admin.password = password
    temp = dict(admin)
    admin.upsert_and_commit()


@manager.command
def createdb():
    db.create_all()


@manager.command
def dropdb():
    db.drop_all()

if __name__ == '__main__':
    manager.run()
