from sqlalchemy import Column, String, BigInteger
from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    phone_number: int = Field(sa_column=Column(BigInteger, unique=True))

    @property
    def phone_number(self):
        return f"+{self.phone_number}"

    # validate phone number to have a + sign
    @phone_number.setter
    def phone_number(self, phone_number: str):
        if phone_number[0] != "+":
            raise ValueError("Phone number must start with a + sign")
        self.phone_number = phone_number[1:]


class Client_Properties(SQLModel, table=True):
    client_id: int = Field(foreign_key="client.id", primary_key=True)
    name: str = Field(
        sa_column=Column(String, unique=True),
    )
