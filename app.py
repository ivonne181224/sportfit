Python 3.15.2 (tags/v3.15.2:5e58eaa, Oct 25 2026, 17:27:03) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, render_template
... 
... app = Flask(__name__)
... 
... @app.route('/')
... def inicio():
...     return render_template('index.html')
... 
... if __name__ == '__main__':
