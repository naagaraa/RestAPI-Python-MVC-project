""" 
------------------------------------------------------------------
Documentation MVC Python RestApi
@autor : nagara
------------------------------------------------------------------
project ini dibuat dengan libraries flask sebagai belajar backend
webservice dengan pattern MVC model, view, controller

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


class User:
    def __init__(self):
        self.nama = "Nagara"

    def getName(self):
        return {
            "name": self.nama,
            "hobbi": "coding",
            "lainnya": "belajar"
        }
