from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Role, Users, Category, Item, Comments_Item, Base

engine = create_engine('postgresql:///model')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session =DBSession()

print "Success!"



#USER TABLE

# try:
# 	no_users = len(session.query(Users).all())
# 	print"START: There are current %s users in dt." %(no_users)

# 	session.query(Users).delete()
# 	session.commmit()

# 	no_users = len(session.query(Users).all())
# 	print"END: There are current %s users in dt." %(no_users)


# except:
# 	session.rollback()
# 	print "Unsuccessful attempt."


no_users = len(session.query(Users).all())
print "START: There are current %s users in dt." %(no_users)

# delete_rows = session.query(Users).all()
# session.delete(delete_rows)
# session.commmit()




no_users = len(session.query(Users).all())
print "END: There are current %s users in dt." %(no_users)
