'''
Suhana Kumar, Caden Khuu, Kevin Lin
Hello
SoftDev
Analyzing a basic flask app
0.3 
2024-09-23
'''

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. This creates an instance of the Flask class called app. This is also seen in instantiating classes in other languages.
1. / just means the root directory like you can see in the terminal, so the app is routed to the root directory. 
2, 3. This will print the name of the web app in the terminal, in this case, __main__ because it is the main module.
4. This will appear as text when you run the web app when the user accesses the / route.
5. This just runs the app, this syntax is usually used to run a function.
 ...

INVESTIGATIVE APPROACH:
<ran file to see results in terminal + on web>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?


@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



