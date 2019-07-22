from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class ProblemTag(Base):
    """ many 2 many relationship between problems and tags """
    __tablename__ = 'problems_tags'

    problemId = Column(Integer, ForeignKey('problems.id'), primary_key=True)
    tagId = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    problem = relationship("Problem", back_populates="tags")
    tag = relationship("Tag", back_populates="problems")

    def __repr__(self):
        return f"<ProblemTag(problemId={self.problemId}, tagId={self.tagId})>"
