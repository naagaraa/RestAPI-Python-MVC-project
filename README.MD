<!-- title -->
# RestAPI PYTHON FLASK PROJECT-Self

<!-- Description -->
<p>indoneisa : </p>
<p>Hi, Project ini dibuat dari latihan saya belajar web programing dari berbagai sumber di internet seperti youtube, stackoverflow dan github. project ini merupakan project open source saya yang ketiga setelah mini mvc , DVM atau prosedural, latar belakang pembuatan, karena saya menghadapi masalah untuk mix tensor flow dan ML untuk thesis dengan php, basic saya mengenal php sebagai primary jika harus ganti envirotment ke bahasa berbeda rada males, dan say thx buat mas Lazuardy buat referensi basic</p>

<p>English : </p>
<p>Hi, this project was made from my practice learning web programming from various sources on the internet such as youtube, stackoverflow and github. This project is my third open source project after mini mvc, DVM or procedural, my background in making, because I have a problem with mix tensor flow and ML for my thesis with php, my basic is to know php as primary if I have to change environment to a different language rather lazy, and say thx to lazuardy for reference basic </p>

---

<!-- table of content YT -->
#### Fork repo
<p>jika mau clone repo ini ke github kalian, kalian tinggal klik forked di pojok kanan atas. thx</p>


## Author dan Contribution

* **Naagaraa Mahasiswa Darma Persada dan Content Creator**  [ instagram ](https://www.instagram.com/naagaraa/)


## Installation manual
description or requretment
- python3
- pip3

1. git clone 
2. ..\\> pip install requiretment.txt or anything hahaha
3. ..\\> venv\scripts\activate
4. ..\\> run server python -m flask run
5. open di browser


## Basic Penjelasan 
basic guide ini adalah penjelasan dasar tentang structur yang akan saya bahas. project ini terdiri dari 2 folder, yaitu apps, venv. apps berisi semua fungsi dan konsept MVC ada di dalamannya. folder venv sebagai envirotmentnya.

* app
	* controller
	* models
	* routes
* venv
	* boostraps
* server.py

## Folder App

folder apps terdiri dari beberapa bagian yaitu :
* controller
* models
* routes

## Database Config 
* on development

<br><br>

## Autoloading


<p>contoh untuk autoloading </p>
**exmpale** :


```

from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


```

<br><br>

## Boostraping


<p>contoh untuk bootstraping </p>
**exmpale** :


```

app = Flask(__name__)

import semua file dari object app pada folder routes __init__.py


```

<br><br>

## Controller


<p>contoh untuk membuat controller.py </p>
**exmpale** :


```

from app import app
from app.models.user import User  

class UserController:
    def getData(self):  # method untuk mengambil data
        user = User()
        nama = user.getName()
        return nama


```

<br><br>

## Models

<p>contoh untuk membuat models.py </p>
**exmpale** :


```
class User:
    def __init__(self):
        self.nama = "Nagara"

    def getName(self):
        return {
            "name": self.nama,
            "hobbi": "coding",
            "lainnya": "belajar"
        }
```

<br><br>


## Routes

<p>contoh untuk deklarasi sebuah path routing </p>
**exmpale** :


```
from app import app
from app.controllers.user_controller import UserController

@app.route('/')
def index():

    user = UserController()
    test = user.getData()
    return test

```

<br><br>

## support Me
<br>
<!-- description -->
hi, kamu bisa support gue dengan cara follow account sosial media di bawah atau traktir bakso pada link di bio social media mereka dibawah ini. thx,

<br>
<br>

<!-- Links -->
**Please support me :**

*Youtube Channel* : 

* Naagaraa : [ YT Naagaraa ](https://www.youtube.com/channel/UCYsZhw6Mlk23Q-nUPP9t1YA?view_as=subscriber)

 *instagram* : 

* Naagaraa : [ IG Naagaraa ](https://www.instagram.com/naagaraa/)

 *Donasi ?* : 
* Naagaraa : [ Traktir baso aja ](https://saweria.co/naagaraa) gak banyak gpp