# -*- coding: utf8 -*-

from flask_login import current_user
import hashlib

def hashPassword(pasw):
	return hashlib.sha256(pasw).hexdigest()

def assertLogin():
	if current_user.is_anonymous: raise Exception(u'로그인 되어있지 않습니다')