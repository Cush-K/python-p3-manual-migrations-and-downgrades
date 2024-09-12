"""Changes column name from birthday to birthdate

Revision ID: b937650cb51a
Revises: 791279dd0760
Create Date: 2024-09-13 01:05:56.522364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b937650cb51a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('students', sa.Column('birthdate', sa.Date(), nullable=True))
    
    op.execute('UPDATE students SET birthdate = birthday')
    
    op.drop_column('students', 'birthday')


def downgrade() -> None:
    op.add_column('students', sa.Column('birthday', sa.Date(), nullable=True))
    
    op.execute('UPDATE students SET birthday = birthdate')
    
    op.drop_column('students', 'birthdate')
