from flask import Flask,redirect,url_for,request

app = Flask(__name__)


@app.route('/hello/<name>') ##modelled as an input from html
def hello_world(name):  # put application's code here
    return 'Hello %s :)))!' % name  ##val assigned just like C
app.add_url_rule('/','hello',hello_world)
    ##binds this function to the URL 'hello'
    #which is http://localhost:5000/hello
@app.route('/admin')
def sup_admin():
    return 'Hello Admin'
@app.route('/guest/<guest>')
def sup_guest(guest):
    if guest =='Admin':
        return redirect(url_for('sup_admin'))
    else:
        return 'Hello %s' %guest
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
@app.route('/login',methods =['POST','GET'])
def login():
    if request.method =='POST':
        user=request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
@app.route('/user/<name>')
def sup_user(name):
    if name == 'admin':
        return redirect(url_for('sup_admin'))
    else:
        return redirect(url_for('sup_guest', guest=name))
@app.route('/canonical/<float:attitude>')
def get_attitude(attitude):

    if attitude <-60:
        return 'Pull up, your attitude is %f' %attitude
    elif attitude >60:
        return 'Stall warning, your attitude is %f!!' %attitude
    else:
        return '%f attitude' %attitude
##this is taken into account here but /canonical/ allows for both / canonical
# and /canonical/ in the URL
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)


