from db import db
from models.incidents import IncidentDB, User
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///humanchain_incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = 'SPARKLEHOOD'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ## kuch karna hai
        email    = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email']    = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid!!')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        ## kuch karna hai
        name     = request.form['name']
        email    = request.form['email']
        password = request.form['password']

        try:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            redirect('/login')

        except:
            db.session.rollback()  # Rollback changes to avoid breaking the session
            print("Error: bhai this email is already registered.")
            return render_template('signup.html', error='Invalid!!')

    return render_template('signup.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    incident = IncidentDB.query.filter_by(id=id).first()
    if request.method == 'POST':
        ## update karo
        allowed_severity = ['LOW', 'MEDIUM', 'HIGH']
        title = request.form['title']
        description = request.form['description']
        severity = request.form['severity'].upper()

        if severity not in allowed_severity:
            return render_template('update.html',failure='sahi severity fill karo bhai!!', incident=incident)
        
        incident.title = title
        incident.description = description
        incident.severity = severity

        db.session.add(incident)
        db.session.commit()
        
        return render_template('update.html', success='Successfully updated', incident=incident)

    
    return render_template('update.html', incident=incident)

@app.route('/delete/<int:id>')
def delete(id):
    incident = IncidentDB.query.filter_by(id=id).first()
    db.session.delete(incident)
    db.session.commit()

    return redirect('/dashboard')

@app.route('/incident', methods=['GET', 'POST'])
def incident():
    if request.method == 'POST':
        allowed_severity = ['LOW', 'MEDIUM', 'HIGH']
        title = request.form['title']
        description = request.form['description']
        severity = request.form['severity'].upper()

        if severity not in allowed_severity:
            return render_template('incident.html', failure='sahi severity fill karo bhai!!')
        
        try:
            incidents_db = IncidentDB(title=title, description=description, severity=severity)
            db.session.add(incidents_db)
            db.session.commit()
        except Exception as e:
            return render_template('incident.html', failure=e)
        
        all_incidents = IncidentDB.query.all()

        return render_template('incident.html', success='Your query has been successfully added. Now you can click show incidents to see all incidents')

    return render_template('incident.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
    if request.method == 'POST':
        id = request.form['search']
        incident = IncidentDB.query.filter_by(id=id).first()
        if id == "" or incident is None:
            return render_template('dashboard.html', id_not_found='Please give correct id!!', user=user)

        return render_template('dashboard.html', incident=incident, user=user)


@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()

    all_incidents = IncidentDB.query.all()
    return render_template('dashboard.html', all_incidents=all_incidents, user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('DB Setup Successfully!!')
    
    app.run(debug=True, port=8000)