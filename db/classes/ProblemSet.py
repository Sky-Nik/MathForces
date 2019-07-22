from sqlalchemy import Column, Integer, DateTime

from db.classes.Base import Base


class ProblemSet(Base):
    __tablename__ = "problemsets"

    problemSetType = Column(Integer, primary_key=True)  # contest = 0, gym = 1
    id = Column(Integer, primary_key=True)  # , autoincrement=False
    # source = Column(String(255))
    # name = Column(String(255))
    grade = Column(Integer)  # nullable=True
    startTime = Column(DateTime, nullable=False)
    endTime = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<ProblemSet(problemSetType={self.problemSetType}, grade={self.grade}, " \
               f"startTime={self.startTime}, endTime={self.endTime}>"
