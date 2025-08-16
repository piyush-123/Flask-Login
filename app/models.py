from .extensions import db,login_manager
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)

    def set_password(self,password):
        from .extensions import bcrypt
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        from .extensions import bcrypt
        return bcrypt.check_password_hash(self.password_hash,password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


