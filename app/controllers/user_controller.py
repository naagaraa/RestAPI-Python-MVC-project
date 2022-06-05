""" 
------------------------------------------------------------------
Documentation MVC Python Rest
@autor : nagara
------------------------------------------------------------------
project ini dibuat dengan libraries flask sebagai belajar backend
webservice dengan pattern MVC model, view, controller

"""

from app import app
from app.models.user import User  # import kelas User dari model

""" 
------------------------------------------------------------------
import module
------------------------------------------------------------------
from app.models.user ini import file user dari folder models
import User ini class dari file User.py

"""

# next step

""" 
------------------------------------------------------------------
Buat class
------------------------------------------------------------------


------------------------------------------------------------------
Buat contructor
------------------------------------------------------------------


------------------------------------------------------------------
Buat method
------------------------------------------------------------------
"""


class UserController:
    def getData(self):  # method untuk mengambil data
        user = User()
        nama = user.getName()
        return nama

    def testData(self):
        user = User()
        return user.getrowData()
