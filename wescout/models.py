from wescout import db


class Region(db.Model):
    # schema for the Region model
    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(30), unique=True, nullable=False)
    players = db.relationship("Player", backref="region", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.region_name


class Player(db.Model):
    # schema for the Player model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=True, nullable=False)
    last_name = db.Column(db.String(40), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    preferred_foot = db.Column(db.String(40), unique=True, nullable=False)
    national_team = db.Column(db.String(40), unique=True, nullable=False)
    domestic_club = db.Column(db.String(40), unique=True, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id}-First:{self.first_name}|Last:{self.last_name}"
        