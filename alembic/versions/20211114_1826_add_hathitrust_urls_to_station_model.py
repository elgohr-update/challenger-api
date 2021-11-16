"""Add hathitrust_urls to Station model

Revision ID: 8f41b2548bee
Revises: 0f3b86567b26
Create Date: 2021-11-14 18:26:16.846065+00:00

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8f41b2548bee"
down_revision = "0f3b86567b26"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("stations", sa.Column("hathitrust_urls", sa.JSON(), nullable=True))
    op.execute("UPDATE stations SET hathitrust_urls = '[]'::json")
    op.alter_column("stations", "hathitrust_urls", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("stations", "hathitrust_urls")
    # ### end Alembic commands ###
