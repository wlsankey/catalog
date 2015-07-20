from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Role, Users, Category, Item, Comments_Item, Base

engine = create_engine('postgresql:///model')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session =DBSession()

# Restoring Database to Empty start condition before populating with test data

#USER table
try:
	delete_all_User = session.query(Users).all()
	number = 0
	length = len(delete_all_User)
	for x in delete_all_User:
		session.delete(x)
		session.commit()
		number = number +1
	if length == (number) and length !=0:
		print "1. Everything deleted from User table."
		print "Total of %s items deleted" %(number)
	if length == 0:
		print "1. No rows in data table USERS!"	
	
except:
	session.rollback()
	print "1. There was a problem and the USERS table was NOT deleted."

#ROLE table
try:
	delete_all_Role = session.query(Role).all()
	number = 0
	length = len(delete_all_Role)
	for x in delete_all_Role:
		session.delete(x)
		session.commit()
		number = number +1
	if length == (number) and length !=0:
		print "2. Everything deleted from ROLE table."
		print "Total of %s items deleted" %(number)
	if length == 0:
		print "2. No rows in data table ROLE!"	
	
except:
	session.rollback()
	print "2. There was a problem and the ROLE table was NOT deleted."

#CATEGORY table

#print "CATEGORY THREE REVIEW START"
#try:
	delete_all_Category = session.query(Category).all()
	number = 0
	length = len(delete_all_Category)
	#print "Total number of items in database to start is %s" %(length)
	for x in delete_all_Category:
		#print x.name
		session.delete(x)
		session.commit()
		#print length
		number = number +1
		#print "Number equals %s)" %(number)
		print "LENGTH EQUALS %s" %length
		if length == (number) and length !=0:
			print "3. Everything deleted from CATEGORY table."
			print "Total of %s items deleted" %(number)
	if length == 0:
		print "3. No rows in data table CATEGORY!"	
	
#except:
	#pass
#	session.rollback()
#	print "3. There was a problem and the CATEGORY table was NOT deleted."

#rint 'CATEGORY THREE REVIEW END'


#ITEM table
try:
	delete_all_Item = session.query(Item).all()
	number = 0
	length = len(delete_all_Item)
	for x in delete_all_Item:
		session.delete(x)
		session.commit()
		number = number +1
	if length == (number) and length !=0:
		print "4. Everything deleted from ITEM table."
		print "Total of %s items deleted" %(number)
	if length == 0:
		print "4. No rows in data table ITEM!"	
	
except:
	session.rollback()
	print "4. There was a problem and the ITEM table was NOT deleted."


#Population data below:

#ROLE Table

Role1 = Role(name= "General user")
Role2 = Role(name= "Adminstrator")
session.add(Role1)
session.commit()
session.add(Role2)
session.commit()

#USER Table


User1 = Users(name="William Sankey", email="william.sankey@gmail.com",no_of_visits= 0, no_of_likes= 0, role=Role1)
User2= Users(name="Jamie Fox", email="JayFox@gmail.com",no_of_visits= 0, no_of_likes= 0, role=Role1)
session.add(User1)
session.commit()
session.add(User2)
session.commit()


#CATEGORY


Category1 = Category(name="Camping", no_of_visits=0)
Category2 = Category(name="Music production", no_of_visits=0)
Category3 = Category(name="Ecological urbanism", no_of_visits=0)
Category4 = Category(name="Books", no_of_visits=0)
Category5 = Category(name="Kitchenware", no_of_visits=0)

session.add(Category1)
session.commit()
session.add(Category2)
session.commit()
session.add(Category3)
session.commit()
session.add(Category4)
session.commit()
session.add(Category5)
session.commit()




#ITEM table



Item1=Item(name="Coleman Sundrome Tent", description= "Easily fit two queen-sized airbeds in the Coleman Sundome 6 Person Tent for you and five friends. This durable TC fabric tent has a rainfly and WeatherTec System to keep the rain at bay. Its continuous Insta-Clip poles make for easy setup in just 10 minutes. This tent even has a breathable ventilation system to keep the air flowing and the bugs out", picture_1= "http://ecx.images-amazon.com/images/I/61C7%2B9C-kAL._SL1500_.jpg", picture_2="http://ecx.images-amazon.com/images/I/81Ca8csoD6L._SL1500_.jpg", picture_3="http://r1.coleman.com/ProductImages/Full/2000007822_500c.jpg", picture_4="http://media.thesimplygroup.com/stockimages/Coleman_Sundome_Beach_Shelter/81542/2/3/391/500.jpg", no_of_likes=0, no_of_visits=0, category=Category1)

Item2=Item(name="LE LED Headlamp", description="A head-mounted flashlight with 18 White LED and 2 Red LED bulbs. Powered by 3 AAA Batteries.", picture_1="http://ecx.images-amazon.com/images/I/61pujMjiEQL._SL1200_.jpg", picture_2="http://ecx.images-amazon.com/images/I/61anFoqXqZL._SL1200_.jpg", picture_3="http://ecx.images-amazon.com/images/I/618-l6Zu17L._SL1200_.jpg", no_of_visits=0, no_of_likes=0, category=Category1)

Item3= Item(name="Rainforest" ,description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum justo eu risus tristique, a tempor dolor luctus. Maecenas bibendum metus risus, at feugiat elit laoreet ac. Proin ut massa viverra justo elementum pulvinar. Donec blandit in lacus ut dignissim. Sed quam risus, suscipit in ornare eget, consequat eget lacus. Vivamus condimentum consectetur est, a accumsan tortor placerat ut. Suspendisse commodo gravida semper. Phasellus pretium ac mi et pharetra. Curabitur ac neque lobortis ligula semper sodales non varius libero. Integer quis facilisis nibh. Nam non dui non nibh porta euismod ut ut urna. Sed in nibh ut lorem aliquet mollis vel sit amet ipsum. In fringilla pulvinar urna ac porttitor. Morbi tincidunt ultrices lorem sit amet aliquet. M", picture_1="http://lorempixel.com/output/nature-q-c-640-640-1.jpg", picture_2="http://lorempixel.com/output/nature-q-c-640-640-1.jpg", picture_3="http://lorempixel.com/output/nature-q-c-640-640-1.jpg", picture_4="http://lorempixel.com/output/nature-q-c-640-640-1.jpg", no_of_likes=0, no_of_visits=0, category=Category3)

session.add(Item1)
session.commit()

session.add(Item2)
session.commit()

session.add(Item3)
session.commit()


print "Database populated with test data!"