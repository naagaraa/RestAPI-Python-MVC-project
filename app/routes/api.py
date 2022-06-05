""" 
------------------------------------------------------------------
Documentation MVC Python Rest
@autor : nagara
------------------------------------------------------------------
project ini dibuat dengan libraries flask sebagai belajar backend
webservice dengan pattern MVC model, view, controller

"""

from app import app
from app.controllers.user_controller import UserController
from werkzeug.exceptions import HTTPException

""" 
------------------------------------------------------------------
import module 
------------------------------------------------------------------
from app import app untuk call __init__py
form app.controllers.user_controller ini nama file pada folder controller
import UserController ini nama class pada user_controller.py

"""
""" 
------------------------------------------------------------------
Routing
------------------------------------------------------------------
untuk membuat routing melakukan deklaras seperti ini
@app.route('path', methods=['GET','POST])

"""
# break line

""" 
------------------------------------------------------------------
Function Handling
------------------------------------------------------------------
setiap routng di handling oleh masing masing function
@app.route('path', methods=['GET','POST])

"""

# break line

""" 
------------------------------------------------------------------
Call Controller dan Method
------------------------------------------------------------------
buat object baru dari class, lalu baru panggil methodnya

"""

# routing here


@app.route('/')
async def index():

    user = UserController()
    data = user.getData()
    return data


@app.route('/test')
async def tests():

    user = UserController()
    data = user.testData()
    print(data)

# errpr handler


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
