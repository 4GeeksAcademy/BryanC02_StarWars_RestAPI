from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)

    favorites = relationship("Favorite", back_populates="user", lazy=True)

    def serialize(self):
        return {"id": self.id,
                "email": self.email}


class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=True)

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "url": self.url}


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=True)

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "url": self.url}


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    planet_id: Mapped[int] = mapped_column(
        ForeignKey('planet.id'), nullable=True)
    person_id: Mapped[int] = mapped_column(
        ForeignKey('person.id'), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    person = relationship("Person")

    def serialize(self):
        data = {
            "id": self.id,
            "user_id": self.user_id,
        }

        if self.person:
            data["person"] = self.person.serialize()
        elif self.planet:
            data["planet"] = self.planet.serialize()

        return data
