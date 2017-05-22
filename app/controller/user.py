# -*- coding: utf8 -*-

from flask import Blueprint, request, jsonify
from flask_login import current_user
from app.service import assertLogin

import app.service.user as service

app = Blueprint('user', __name__)

@app.route('/whoami', methods=['GET'])
def controlWhoami():
	try:
		assertLogin()
		return jsonify({ 'success': 1, 'user': current_user.serialize })
	except Exception as e:
		print e
		return jsonify({'success': 0, 'error': str(e)})

@app.route('/signup', methods=['POST'])
def controlSignup():
	try:
		json = request.get_json()
		user = service.signup(json)
		return jsonify({'success':1, 'user': user.serialize})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

@app.route('/contact', methods=['POST'])
def controllPostContact():
	try:
		assertLogin()
		json = request.get_json()
		phoneNumber = json['phoneNumber']
		other = service.createContact(current_user, phoneNumber)
		return jsonify({'success':1, 'otherId': other.id})
	except Exception as e:
		print e
		return jsonify({'success':0, 'error': str(e)})

@app.route('/contacts/<int:page>', methods=['GET'])
def controlGetContacts(page):
	try:
		assertLogin()
		contacts = service.getContacts(current_user, page, **(request.args))
		return jsonify({'success': 1, 'contacts': [i.serialize for i in contacts]})
	except Exception as e:
		print e
		return jsonify({'success': 0, 'error': str(e)})

@app.route('/contact/<int:otherId>', methods=['DELETE'])
def controlDeletePutContact(otherId):
	try:
		assertLogin()
		if not service.removeContact(current_user, otherId): raise Exception(u'삭제에 실패했습니다')
		return jsonify({'success': 1})
	except Exception as e:
		print e
		return jsonify({'success': 0, 'error': str(e)})


