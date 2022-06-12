from flask import Flask  
app = Flask(__name__)    
@app.route('/')                         
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
  return "Dojo\n"*10 

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi, " + name



@app.route('/repeat/<number>/<name>') 
def repeat(name):
    print(name*10)
    return 
                                  
if __name__=="__main__":   
    app.run(debug=True)    