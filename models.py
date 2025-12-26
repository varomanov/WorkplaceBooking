from sqlalchemy import create_engine, String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship #, Session
from typing import List

engine = create_engine('sqlite:///booking.db')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(String(50))
    bookings: Mapped[List['Booking']] = relationship(
        back_populates='user', cascade='all, delete-orphan')


class Place(Base):
    __tablename__ = 'places'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    place: Mapped[str] = mapped_column(String(20))
    is_active: Mapped[bool] = mapped_column()
    bookings: Mapped[List['Booking']] = relationship(
        back_populates='place', cascade='all, delete-orphan')


class Booking(Base):
    __tablename__ = 'bookings'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[Date] = mapped_column(Date())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    place_id: Mapped[int] = mapped_column(ForeignKey('places.id'))

    user: Mapped['User'] = relationship(back_populates='bookings')
    place: Mapped['Place'] = relationship(back_populates='bookings')


Base.metadata.create_all(engine)
# with Session(engine) as session:
#     u1 = User(user_name='John Doe')
#     u2 = User(user_name='Alex Pushkin')
#     p1 = Place(place='822/01', is_active=True)
#     p2 = Place(place='822/02', is_active=True)
#     p3 = Place(place='822/03', is_active=True)
#     session.add_all([u1, u2, p1, p2, p3])
#     session.commit()