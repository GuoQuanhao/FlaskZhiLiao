"""empty message

Revision ID: aa9831cf6c41
Revises: 7721230e05bd
Create Date: 2023-05-09 15:41:10.303284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa9831cf6c41'
down_revision = '7721230e05bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('captcha', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_captcha')
    # ### end Alembic commands ###
