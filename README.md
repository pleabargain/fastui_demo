# code
https://github.com/pleabargain/fastui_demo

# demo of fastui
This is proof that the sample code from 
* https://github.com/pydantic/FastUI

works as advertised.

# requirements

fastapi

fastui

uvicorn

```pip install -r requirements.txt```


# inspiration
* https://www.youtube.com/watch?v=eBWrnSyN2iw&t=6s

and

* https://github.com/pydantic/FastUI


# run the code
uvicorn main:app --reload

if everything works then you should see something in the terminal like this:

```INFO:     Will watch for changes in these directories: ['C:\\Users\\denni\\OneDrive\\Documents\\fastui_demo']     
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15824] using StatReload
INFO:     Started server process [1352]
INFO:     Waiting for application startup.
INFO:     Application startup complete.```

# notes
I tried to get ChatGPT to rewrite the code for me to take a JS array convert it to JSON but no joy. that's the badmain.py

# o.py
is the original working code

# main.py
I asked GPT4 to generate sample python objects and then to rewrite o.py to match my data. It worked.
