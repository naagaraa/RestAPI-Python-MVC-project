import os
from dotenv import dotenv_values

""" 
------------------------------------------------------------------
Documentation MVC Python Rest
@autor : nagara
------------------------------------------------------------------
project ini dibuat dengan libraries flask sebagai belajar backend
webservice dengan pattern MVC model, view, controller

"""

""" 
------------------------------------------------------------------
Import app dari folder app
------------------------------------------------------------------
import file __init__py
"""
from app import app ## import app dari package app yang kita buat

""" 
------------------------------------------------------------------
Boostraping run di server port 8080
------------------------------------------------------------------
import file __init__py
"""
config = dotenv_values(".env")
app.run(port=8080)
