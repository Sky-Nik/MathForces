from sqlalchemy import Column, Integer, ForeignKey

from db.classes.Base import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    submittedBy = Column(Integer, ForeignKey('users.id'))
    problemId = Column(Integer, ForeignKey('problems.id'))
    # A whole number in [0..7] or in {0, 1},
    # depending on contest's grading policy.
    # -1 if submission is not yer graded.
    grade = Column(Integer)
    gradedBy = Column(Integer, ForeignKey('users.id'), nullable=True, default=None)

    def __repr__(self):
        return f"<Submission(submittedBy={self.submittedBy}, problemId={self.problemId}, grade={self.grade}" \
               f"{('gradedBy=' + str(self.gradedBy)) if self.grade != -1 else ''})>"
