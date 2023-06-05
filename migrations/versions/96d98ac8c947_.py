"""empty message

Revision ID: 96d98ac8c947
Revises: 
Create Date: 2023-06-01 04:02:19.858348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "96d98ac8c947"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "account",
        sa.Column("id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("balance", sa.Integer(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="account_pkey"),
    )


def downgrade():
    op.drop_table("account")
