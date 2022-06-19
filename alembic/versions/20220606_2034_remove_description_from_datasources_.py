"""remove description from datasources table

Revision ID: 8d3adfa65472
Revises: 986441aa7483
Create Date: 2022-06-06 20:34:04.295511+00:00

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8d3adfa65472"
down_revision = "986441aa7483"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("data_sources", "description")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "data_sources",
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
