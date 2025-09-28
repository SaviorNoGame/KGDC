from ... import db
from ...models import User

class commands():
    def admin(args):
        user = User.query.filter_by(username=args[0]).first()
        if not user is None:
            user.role = 'Admin'
            db.session.commit()

    def unadmin(args):
        user = User.query.filter_by(username=args[0]).first()
        if not user is None:
            user.role = 'Member'
            db.session.commit()

    def role(args):
        user = User.query.filter_by(username=args[0]).first()
        if not user is None:
            user.role = args[1]
            db.session.commit()

    def announce(args):
        pass

    def unannounce():
        pass

    cmd_list = dict(admin=admin, unadmin=unadmin, role=role)
