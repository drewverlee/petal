from petalapp import db

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
    last_name = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    email = db.Column(db.String(150), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    hospitals = db.relationship('Hospital', secondary=hospitals,
        backref=db.backref('users', lazy='dynamic'))



    def __init__(self, last_name="NONE", first_name="NONE", role=ROLE_USER,
            email="NONE"):
        self.last_name = last_name
        self.first_name = first_name
        self.role = role
        self.email = email

    #TODO what information to show?
    def __repr__(self):
        return '<Name : %r, %r >' % (self.last_name ,self.first_name)

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

    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))

    def __init__(self, standard_form, marketing_education,
        record_availability, family_centerdness,
        pc_networking, education_and_training, team_funding,
        coverage, pc_for_expired_pts, hospital_pc_screening,
        pc_follow_up, post_discharge_services, bereavement_contacts,
        certification, team_wellness, care_coordination):

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

    def __repr__(self):
        return """
    {standard_form : %r}
    {marketing_education : %r}
    {record_availability : %r}
    {family_centerdness : %r}
    {pc_networking : %r}
    {education_and_training : %r}
    {team_funding : %r}
    {coverage : %r}
    {pc_for_expired_pts : %r}
    {hospital_pc_screening  : %r}
    {pc_follow_up : %r}
    {post_discharge_services : %r}
    {bereavement_contacts : %r}
    {certification : %r}
    {team_wellness : %r}
    {care_coordination : %r}""" % (
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
    self.care_coordination)
