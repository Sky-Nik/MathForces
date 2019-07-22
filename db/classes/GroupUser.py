from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class GroupUser(Base):
    """ many 2 many relationship between groups and users """
    __tablename__ = 'groups_users'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'), primary_key=True)

    group = relationship("Group", back_populates="users")
    user = relationship("User", back_populates="groups")

    def __repr__(self):
        return f"<GroupUser(groupId={self.groupId}, userId={self.userId})>"
