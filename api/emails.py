from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app

conn = http.client.HTTPSConnection("rapidprod-sendgrid-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
    'X-RapidAPI-Host': "rapidprod-sendgrid-v1.p.rapidapi.com"
    }

conn.request("GET", "/suppression/invalid_emails", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

