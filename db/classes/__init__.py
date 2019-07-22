from sqlalchemy.orm import relationship

from db.classes.Base import Base
from db.classes.BlogPost import BlogPost
from db.classes.Group import Group
from db.classes.GroupBlogPost import GroupBlogPost
from db.classes.GroupProblemSet import GroupProblemSet
from db.classes.GroupUser import GroupUser
from db.classes.Problem import Problem
from db.classes.ProblemSet import ProblemSet
from db.classes.ProblemSetProblem import ProblemSetProblem
from db.classes.ProblemTag import ProblemTag
from db.classes.Tag import Tag
from db.classes.User import User
from db.classes.Submission import Submission

User.blogPosts = relationship("BlogPost", order_by=BlogPost.id, back_populates="author")

Problem.tags = relationship("ProblemTag", order_by=ProblemTag.tagId, back_populates="problem")
Tag.problems = relationship("ProblemTag", order_by=ProblemTag.problemId, back_populates="tag")

ProblemSet.problems = relationship("ProblemSetProblem", order_by=ProblemSetProblem.problemId,
                                   back_populates="problemSet")
Problem.problemSets = relationship("ProblemSetProblem", order_by=ProblemSetProblem.problemSetId,
                                   back_populates="problem")

Group.users = relationship("GroupUser", order_by=GroupUser.userId, back_populates="group")
User.groups = relationship("GroupUser", order_by=GroupUser.groupId, back_populates="user")

Group.blogPosts = relationship("GroupBlogPost", order_by=GroupBlogPost.blogPostId, back_populates="group")
BlogPost.groups = relationship("GroupBlogPost", order_by=GroupBlogPost.groupId, back_populates="blogPost")

Group.problemSets = relationship("GroupProblemSet", order_by=GroupProblemSet.problemSetId, back_populates="group")
ProblemSet.groups = relationship("GroupProblemSet", order_by=GroupProblemSet.groupId, back_populates="problemSet")

__all__ = ["Base", "User", "BlogPost", "Problem", "ProblemTag", "ProblemSet", "ProblemSetProblem", "Group", "GroupUser",
           "GroupBlogPost", "GroupProblemSet", "Submission"]
