**Run API**

* install requirements -> pip3 install -r requirements.txt
* open 3 terminal
 * Terminal 1: python3 app.py
 * Terminal 2: celery -A app.celery worker -l info
 * Terminal 3: curl -i -X POST -d "[{'name': 'ali', 'email': 'aliilteriskeskin@gmail.com'}, {'name': 'selo', 'email': 'selamet96@gmail.com'}, {'name': 'ugi', 'email': 'uguryuce93@gmail.com'}]" localhost:5000

**Error Note:**
If don't send mail open [this page](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PDhuVhH0KP69GqDIXQ5QCkDEPc7A6WMEoFzw6BrC94cmeyM7xx2ae6F6T4e8cnIvFqtKdcRYnPqLWgs7Pv8Ayiy09yEQ) and enable less secure apps.