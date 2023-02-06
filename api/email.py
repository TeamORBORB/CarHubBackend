
from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app

# all invalids
import requests

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/suppression/invalid_emails"

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
#deleting invalids
import requests

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/suppression/invalid_emails/%7Bemail%7D"

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.request("DELETE", url, headers=headers)

print(response.text)

#btw thinking of adding an subsciption send maybe but if I want to add that I may have to create a unsubscribe so it isnt a spam
#sending emails to specific accounts
import requests

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/alerts/%7Balert_id%7D"

payload = {
	"type": "stats_notification",
	"email_to": "example@test.com",
	"frequency": "daily"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.request("PATCH", url, json=payload, headers=headers)

print(response.text)