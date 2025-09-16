from email.mime import image
import os
from flask import  Flask, flash,render_template,request,redirect, session,url_for
import sqlite3
app = Flask(__name__)

# ::::::: HOME PAGE :::::::


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



# ::::::: ABOUTS ::::::::

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')


# ::::::: JOB LISTNG :::::::
@app.route('/jl',methods=['GET'])
def jl():
   return render_template('job-listings.html') 
# :::: JOB SINGEL ::::

@app.route('/job-single', methods=['GET'])
def job_single():
    return render_template('job-single.html')


# :::: JOB POST ::::

@app.route("/job_post", methods=["POST","GET"])
def job_post():
    if request.method== "POST":
        job_title = request.form ['job_title'] 
        company_name = request.form ['company_name']
        job_location = request.form ['job_location']
        job_region = request.form ['job_region']
        job_type = request.form ['job_type']
        job_description = request.form ['job_description']

        conn = sqlite3.connect('jp.db')
        c = conn.cursor()
        c.execute("INSERT INTO jobs (job_title, company_name, job_location, job_region, job_type, job_description) VALUES (?,?,?,?,?,?)",(job_title,company_name,job_location,job_region,job_type,job_description))
        conn.commit()
        flash('Job Posted Successfully!')
        return redirect(url_for('job_listing'))
    return render_template ('post-job.html')


# :::::: pages :::::::

    
@app.route('/services',methods=['GET','POST'])
def services():
    return render_template('services.html')


@app.route('/servicesingle',methods=['GET','POST'])
def servicesingle():
    return render_template('service-single.html')


@app.route('/blogsingle',methods=['GET','POST'])
def blogsingle():
    return render_template('blog-single.html')


@app.route('/portfolio',methods=['GET','POST'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/portfoliosingle',methods=['GET','POST'])
def portfoliosingle():
    return render_template('portfolio-single.html')



@app.route('/testimonials',methods=['GET','POST'])
def testimonials():
    return render_template('testimonials.html')


@app.route('/faq',methods=['GET','POST'])
def faq():
    return render_template('faq.html')




@app.route('/gallery',methods=['GET','POST'])
def gallery():
    return render_template('gallery.html')


# :::::: BLOG :::::::

@app.route('/blog',methods=['GET','POST'])
def blog():
    return render_template('blog.html')



# :::::: CONTACT :::::::

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')



# ::::::: PORT JOB :::::::

@app.route('/postjob',methods=['GET','POST'])
def postjob():
        if request.method== "POST":
            job_title = request.form ['jt'] 
            company_name = request.form ['cn']
            job_location = request.form ['jl']
            job_region = request.form ['jr']
            job_type = request.form ['jtype']
            job_description = request.form['jd']

            conn = sqlite3.connect('jp.db')
            c = conn.cursor()
            c.execute("INSERT INTO jobs (job_title, company_name, job_location, job_region, job_type, job_description) VALUES (?,?,?,?,?,?)",(job_title,company_name,job_location,job_region,job_type,job_description))
            conn.commit()
            flash('Job Posted Successfully!')
            return redirect(url_for('jl'))
        return render_template ('post-job.html')



# :::::: SIGNUP ::::::::

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    return filename.replace('\\', '/').replace('?', '').replace('"', "'").replace('<', '').replace('>', '').replace('|', '').replace('*', '').replace(':', '').replace(' ', '_')

def check_user(email):
    conn = sqlite3.connect('jp.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    user = c.fetchone()
    conn.close()  # Close the database connection after use
    return True if user else False

# def save_resume(file):
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         print("File path:", filepath)  # Debugging statement
#         try:
#             file.save(filepath)
#             return filepath
#         except Exception as e:
#             print(f"Error saving file: {e}")
#             return None
#     return None
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        name = request.form['name'] 
        email = request.form['email']
        pwd = request.form['pwd']
        phone = request.form['phone']
        gender = request.form['gender']
        addrs = request.form['addrs']
        resume_file = request.form['resume']
        
        # if resume_file.filename == '':
        #     flash('Please upload your resume')
        #     return render_template('login.html')

        # if not allowed_file(resume_file.filename):
        #     flash('Allowed file types are pdf, doc, docx')
        #     return render_template('login.html')

        # filename = secure_filename(resume_file.filename)
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # try:
        #     resume_file.save(filepath)
        #     flash('Resume uploaded successfully')
        # except Exception as e:
        #     flash(f'Error uploading resume: {e}')
        #     return render_template('login.html')

        conn = sqlite3.connect('jp.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, pwd, phone, gender, addrs, resume) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (name, email, pwd, phone, gender, addrs, resume_file))
        
        conn.commit()
        c.execute("INSERT INTO login (u_name,password) VALUES (?, ?)",(name, pwd))
        conn.commit()
        conn.close()

        flash('Registration Successful! You can now login.')
        return redirect(url_for('index'))

    return redirect(url_for('login'))



# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         name = request.form['name'] 
#         email = request.form['email']
#         pwd = request.form['pwd']
#         phone = request.form['phone']
#         gender = request.form['gender']
#         addrs = request.form['addrs']
#         resume_file = request.files['resume']
        
#         if check_user(email):
#             flash("User Already Exists! Please Login.")
#             return redirect(url_for("signin"))

#         resume_path = save_resume(resume_file)
#         if not resume_path:
#             flash("Invalid resume file format! Allowed formats: pdf, doc, docx.")
#             return redirect(url_for("signup"))  # Redirect to signup page if file format is invalid

#         conn = sqlite3.connect('jp.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO users (name, email, pwd, phone, gender, addrs, resume) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                   (name, email, pwd, phone, gender, addrs, resume_path))
#         conn.commit()
#         conn.close()  # Close the database connection after use
#         flash('Registration Successful! You can now login.')
#         return redirect(url_for('index'))

#     return render_template('login.html')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# :::::: LOGIN ::::::::
app.secret_key = 'your_secret_key'

# def check_password(username, password):
#     conn = sqlite3.connect('jp.db')
#     c = conn.cursor()

#     c.execute("SELECT * FROM users WHERE name=?", (username,))
#     user = c.fetchone()

#     if user and user[1] == password:
#         return True
#     else:
#         return False

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pwd']

        conn = sqlite3.connect('jp.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE name=? AND pwd=?", (username, password))
        user = c.fetchone()

        if user:
            session['loggedin'] = True
            session['user'] = user[0]
            session['username'] = user[1]
            session['resume'] = user[7]
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')

# :::::: LOGOUT ::::::::
@app.route('/logout')
def logout() :
    if 'loggedin' in session:
        flash("You have been successfully logged out")
        del session['loggedin']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))  
# :::::: apply button ::::::
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

@app.route('/apply', methods=["POST", "GET"])
def apply():
    if request.method == "GET":
        return render_template('job-single.html')
    
    if session.get('loggedin') != True:
        return redirect(url_for('login'))

    if request.method == "POST" and session.get('loggedin') == True:
        userId = session['user']
        conn = sqlite3.connect('jp.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id=?", (userId,))
        user = cur.fetchone()

        # Get user details
        user_id = user[0]
        applicantEmail = user[2]
        applicantName = session['username']

        # Get job details
        jid = int('1')  # Assuming job_id 1
        cur.execute("SELECT * FROM jobs WHERE job_id=?", (jid,))
        job = cur.fetchone()
        jt = job[1]
        cn = job[2]

        # Insert application into the database
        cur.execute("INSERT INTO applications (application_date, status, job_id, user_id) VALUES (?, NULL, ?, ?)", 
                    (datetime.now(), jid, user_id))
        conn.commit()

        # Send email to applicant
        send_email(applicantEmail, f'Application Submitted - {jt}', 
                   f'Dear {applicantName},\nYour application for the job {jt} at {cn} has been submitted successfully.\nBest regards,\nYour Company Name')

        # Send email to company employer
        send_email('company-employer-email@example.com', f'New Application Received - {jt}', 
                   f'Dear Employer,\nA new application for the job {jt} at {cn} has been received.\nBest regards,\nYour Company Name')

        flash('Application Submitted Successfully!')
        return redirect(url_for('jl'))

def send_email(recipient, subject, body):
    server = None
    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = 'your-email@example.com'
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the body to the MIME message
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server details
        server.starttls()
        server.login("your-email@example.com", "your-password")
        server.sendmail("your-email@example.com", recipient, msg.as_string())
        flash('Email Sent Successfully!')
    except Exception as e:
        flash(f'Error sending email: {e}')
    finally:
        if server is not None:
            server.quit()  # Quit the server only if it was initialized
    
@app.route('/search',methods=["POST","GET"])
def search():
    if request.method=="POST":
        jobtitle=request.form['jt']
        conn = sqlite3.connect('jp.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM jobs WHERE job_title=?", (jobtitle,))
        job = cur.fetchone()
        jt = job[1]
        return render_template('job-single.html')#jt=jt

        
# def sign():
#     if request.method=="GET":
#         return render_template('login.html')
#     if request.method=="POST":
#         email = request.form['email']
#         password = request.form['password']
#         repass=request.form['repass']
#         # Insert data into the database
#         conn = sqlite3.connect('database.db')
#         c = conn.cursor()
        
        
#         c.execute("SELECT * FROM users WHERE email=?", (email,))
#         existing_user = c.fetchone()
#         if existing_user:
#             message = flash('Email already registered. Please use a different email.', 'error')
#             return render_template('/sign.html',message=message)
#         else:
#             # Add the new user to the database
#             c.execute('''INSERT INTO users (full_name, address, gender, state, pincode, email, password)
#                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
#                   (full_name, address, gender, state, pincode, email, password))
#             conn.commit()
#             flash('Sign up successful! Welcome aboard!', 'success')
#             return redirect('/')
#     conn.commit()
#     conn.close()

#     return redirect(url_for('index'))


if  __name__ == '__main__':
    app.run(debug=True,port=8000)