"""initial_db

Revision ID: 90f9f35c14d5
Revises:
Create Date: 2024-06-12 08:05:27.079019

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel  # noqa


# revision identifiers, used by Alembic.
revision: str = "90f9f35c14d5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "client",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone_number", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone_number", sa.BigInteger(), nullable=False),
        sa.Column(
            "login_code", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_session",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column(
            "last_read", sa.DateTime(), server_default="now()", nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["client.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "client_properties",
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["client.id"],
        ),
        sa.PrimaryKeyConstraint("client_id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "user_properties",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "chat",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("chat_session_id", sa.Integer(), nullable=False),
        sa.Column(
            "message", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "sender",
            sa.Enum(
                "USER", "CLIENT", "ASSISTANT", "SYSTEM", name="chat_sender"
            ),
            nullable=False,
        ),
        sa.Column(
            "created_at", sa.DateTime(), server_default="now()", nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["chat_session_id"],
            ["chat_session.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("chat")
    op.drop_table("user_properties")
    op.drop_table("client_properties")
    op.drop_table("chat_session")
    op.drop_table("user")
    op.drop_table("client")
    # ### end Alembic commands ###
