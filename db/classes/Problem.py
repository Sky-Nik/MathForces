from sqlalchemy import Column, Integer, String

from db.classes.Base import Base


class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    # source_type = Column(Integer)  # contest = 0, gym = 1
    # source_id = Column(Integer)
    difficulty = Column(Integer, default=1500)

    def __repr__(self):
        return f'<Problem(id={self.id}, name="{self.name}", difficulty={self.difficulty})>'
