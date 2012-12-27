from petalapp import db
from datetime import datetime
ROLE_USER = 0
ROLE_ADMIN = 1

#TODO:rename
hospitals = db.Table('hospitals',
    db.Column('hospital_id', db.Integer, db.ForeignKey('hospital.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
# tags bmarks time
class User(db.Model):
    """User has a many-to-many relationship with Hospital"""

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(150), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    hospitals = db.relationship('Hospital', secondary=hospitals,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, nickname, email, role=ROLE_USER):
        self.nickname= nickname
        self.role = role
        self.email = email

    #TODO what information to show?
    def __repr__(self):
        return '<Name : %r>' % (self.nickname)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @stacticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname


class Hospital(db.Model):
    """Hospital's has a one-to-many relationship with DATA and a
    many-to-many relationship with User"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    data = db.relationship('Data', backref='hospital', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name


class Data(db.Model):
    """Data has a many-to-one relationship with Hospital"""

    id = db.Column(db.Integer, primary_key=True)

    standard_form = db.Column(db.Integer)
    marketing_education = db.Column(db.Integer)
    record_availability = db.Column(db.Integer)
    family_centerdness = db.Column(db.Integer)
    pc_networking = db.Column(db.Integer)
    education_and_training = db.Column(db.Integer)
    team_funding = db.Column(db.Integer)
    coverage = db.Column(db.Integer)
    pc_for_expired_pts = db.Column(db.Integer)
    hospital_pc_screening  = db.Column(db.Integer)
    pc_follow_up = db.Column(db.Integer)
    post_discharge_services = db.Column(db.Integer)
    bereavement_contacts = db.Column(db.Integer)
    certification = db.Column(db.Integer)
    team_wellness = db.Column(db.Integer)
    care_coordination = db.Column(db.Integer)

    timestamp = db.Column(db.DateTime)

    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))

    def __init__(self, standard_form=0,
            marketing_education=0, record_availability=0, family_centerdness=0,
        pc_networking=0, education_and_training=0, team_funding=0,
        coverage=0, pc_for_expired_pts=0, hospital_pc_screening=0,
        pc_follow_up=0, post_discharge_services=0, bereavement_contacts=0,
        certification=0, team_wellness=0, care_coordination=0, timestamp=datetime.utcnow()):

            self.standard_form = standard_form
            self.marketing_education =  marketing_education
            self.record_availability = record_availability
            self.family_centerdness =  family_centerdness
            self.pc_networking =  pc_networking
            self.education_and_training =  education_and_training
            self.team_funding =  team_funding
            self.coverage =  coverage
            self.pc_for_expired_pts =  pc_for_expired_pts
            self.hospital_pc_screening  =  hospital_pc_screening
            self.pc_follow_up =  pc_follow_up
            self.post_discharge_services =  post_discharge_services
            self.bereavement_contacts =  bereavement_contacts
            self.certification =  certification
            self.team_wellness =  team_wellness
            self.care_coordination = care_coordination
            self.timestamp = timestamp

    def __repr__(self):
        return """
    <standard_form : %r>\n
    <marketing_education : %r>\n
    <record_availability : %r>\n
    <family_centerdness : %r>\n
    <pc_networking : %r>\n
    <education_and_training : %r>\n
    <team_funding : %r>\n
    <coverage : %r>\n
    <pc_for_expired_pts : %r>\n
    <hospital_pc_screening  : %r>\n
    <pc_follow_up : %r>\n
    <post_discharge_services : %r>\n
    <bereavement_contacts : %r>\n
    <certification : %r>\n
    <team_wellness : %r>\n
    <care_coordination : %r>\n
    <datetime_utc  : %r>""" % (
    self.standard_form,
    self.marketing_education,
    self.record_availability,
    self.family_centerdness,
    self.pc_networking,
    self.education_and_training,
    self.team_funding,
    self.coverage,
    self.pc_for_expired_pts,
    self.hospital_pc_screening ,
    self.pc_follow_up,
    self.post_discharge_services,
    self.bereavement_contacts,
    self.certification,
    self.team_wellness,
    self.care_coordination,
    self.timestamp)

