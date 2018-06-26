from bottle import route, run, request, static_file, hook, response
import random, json

import DiceGame

@hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@route('/')
def hello():
	return "Hello ..Welcome to Dice Game...."


@route('/RollDice')
def BestDice():
	return DiceGame.Dice()

run(host='0.0.0.0', port=8080)
