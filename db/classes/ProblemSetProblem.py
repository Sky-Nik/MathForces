from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class ProblemSetProblem(Base):
    """ many 2 many relationship between problemSets and problems """
    __tablename__ = "problemsets_problems"

    problemSetId = Column(Integer, ForeignKey('problemsets.id'), primary_key=True)
    problemId = Column(Integer, ForeignKey('problems.id'), primary_key=True)

    problemSet = relationship("ProblemSet", back_populates="problems")
    problem = relationship("Problem", back_populates="problemSets")

    def __repr__(self):
        return f"<ProblemSetProblem(problemSetId={self.problemSetId}, problemId={self.problemId})>"
