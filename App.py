from flask import Flask, request, render_template, redirect, url_for 
app = Flask(__name__, template_folder='template') 
@app.route('/') 
def home(): 
    return render_template('home.html')   
@app.route('/register', methods=['GET', 'POST']) 
def register(): 
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email'] 
        phone = request.form['phone'] 
        dob = request.form['dob'] 
        gender = request.form['gender'] 
        username = request.form['username'] 
        password = request.form['password'] 
        confirmpassword = request.form['confirmpassword']         
        if password != confirmpassword: 
            return render_template('register.html', error="Passwords do not match.")    
        return render_template('Success.html')     
    return render_template('register.html') 
if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=7000)