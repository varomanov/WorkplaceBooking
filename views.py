from models import engine, Booking, User, Place
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date


def add_booking(user, place):
    try:
        with Session(engine) as session:
            selected_user = session.execute(
                select(User).where(User.user_name == user)).scalar()
            selected_place = session.execute(
                select(Place).where(Place.place == place)).scalar()
            book = Booking(
                date=date.today(),
                user=selected_user,
                place=selected_place,
            )
            session.add(book)
            session.commit()
    except Exception as e:
        session.rollback()
        print(e)


def get_places():
    with Session(engine) as session:
        stmt = select(Place).where(Place.is_active == True)
        result = [x.place for x in session.execute(stmt).scalars()]
        return result


def get_users():
    with Session(engine) as session:
        stmt = select(User)
        result = [x.user_name for x in session.execute(stmt).scalars()]
        return result


def get_journal():
    with Session(engine) as session:
        stmt = select(Booking)
        result = [{'name': x.user.user_name, 'place': x.place.place} for x in session.scalars(stmt)]
        return result
    
# add_booking('Alex Pushkin', '822/02')