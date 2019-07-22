from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class GroupBlogPost(Base):
    """ many 2 many relationship between groups and blog posts """
    __tablename__ = 'groups_blog_posts'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    blogPostId = Column(Integer, ForeignKey('blog_posts.id'), primary_key=True)

    group = relationship("Group", back_populates="blogPosts")
    blogPost = relationship("BlogPost", back_populates="groups")

    def __repr__(self):
        return f"<GroupBlogPost(groupId={self.groupId}, blogPostId={self.blogPostId})>"
