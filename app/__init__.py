""" 
------------------------------------------------------------------
Documentation MVC Python Rest
@autor : nagara
------------------------------------------------------------------
project ini dibuat dengan libraries flask sebagai belajar backend
webservice dengan pattern MVC model, view, controller

"""

from flask import Flask ## import Flask dari package flask

""" 
------------------------------------------------------------------
Buat Object baru dari Flask
------------------------------------------------------------------

"""

app = Flask(__name__)

""" 
------------------------------------------------------------------
Import semua file pada folder routes
------------------------------------------------------------------
import semua file dari object app pada folder routes __init__.py

"""
from app.routes import  *