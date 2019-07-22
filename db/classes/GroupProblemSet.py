from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class GroupProblemSet(Base):
    """ many 2 many relationship between groups and problemSets """
    __tablename__ = 'groups_problemsets'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    problemSetId = Column(Integer, ForeignKey('problemsets.id'), primary_key=True)

    group = relationship("Group", back_populates="problemSets")
    problemSet = relationship("ProblemSet", back_populates="groups")

    def __repr__(self):
        return f"<GroupProblemSet(groupId={self.groupId}, problemSetId={self.problemSetId})>"
