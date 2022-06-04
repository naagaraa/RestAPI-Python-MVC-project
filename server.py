from app import app  # import app dari package app yang kita buat
from dotenv import load_dotenv
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

""" 
------------------------------------------------------------------
Boostraping run di server port 8080
------------------------------------------------------------------
import file __init__py
"""
load_dotenv()
app.run(port=8080)
