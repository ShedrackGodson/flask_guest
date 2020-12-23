from . import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    comment = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.name}-{self.comment[:10]}...."

    class Meta:
        ordering = [
            "-id"
        ]
