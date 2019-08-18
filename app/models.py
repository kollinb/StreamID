from app import db


class Clip(db.Model):
    id = db.Column(db.String(70), primary_key=True)
    title = db.Column(db.String(120))
    broadcaster_name = db.Column(db.String(70))
    thumb_url = db.Column(db.String(200))

    def __repr__(self):
        return '<Clip {}>'.format(self.id)