from flask import Flask,redirect,render_template,request
import sqlite3
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="GET":
        return render_template('flaskdb.html')
    if request.method=="POST":
        no=request.form['no']
        mail=request.form['mail']
        password=request.form['password']
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute('INSERT INTO users(id,name,email) VALUES(?,?,?)',(no,mail,password))
        conn.commit()
        conn.close()
        return 'User added successfully'
@app.route('/fetchrecord')
def fetchRecord():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template('showdata.html', users=users)
@app.route('/deleterecord',methods=['GET','POST'])
def deleteRecord():
        if request.method=="GET":
            return render_template('delete.html')
        if request.method == 'POST':
            record_id = request.form['no']
            conn = sqlite3.connect('example.db')
            c = conn.cursor()
            c.execute("DELETE FROM users WHERE id=?", (record_id,))
            conn.commit()
            conn.close()
            return 'user deleted successfully'
@app.route('/updaterecord',methods=['POST','GET'])
def updateRecord():
     if request.method=="GET":
            return render_template('update.html')
     if request.method == 'POST':
        record_id = request.form['no']
        new_name = request.form['mail']
        new_email = request.form['pass']
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("UPDATE users SET name=?, email=? WHERE id=?", (new_name, new_email, record_id))
        conn.commit()
        conn.close()
        return 'Record updated successfully'
if __name__=='__main__':
    app.run(debug=True)