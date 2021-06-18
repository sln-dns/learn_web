from db import db_session
from models import User


user = User(name='Мария Сидорова', salary=4321, email='msidorova@example.com' )
db_session.add(user)
db_session.commit()