import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    userType = Column(Integer)  # admin = 0, teacher = 1, student = 2
    handle = Column(String(255), unique=True)
    password = Column(String(255))
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f'<User(handle="{self.handle}", type={self.userType}, id={self.id})>'


class BlogPost(Base):
    __tablename__ = 'blog_posts'

    authorId = Column(Integer, ForeignKey('users.id'))
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    publishedOn = Column(DateTime, default=datetime.datetime.utcnow)

    author = relationship("User", back_populates="blogPosts")

    def __repr__(self):
        return f'<BlogPost(id={self.id}, authorId={self.authorId}, ' \
               f'title="{self.title}", publishedOn={self.publishedOn})>'


User.blogPosts = relationship("BlogPost", order_by=BlogPost.id, back_populates="author")


class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    # source_type = Column(Integer)  # contest = 0, gym = 1
    # source_id = Column(Integer)
    difficulty = Column(Integer, default=1500)

    def __repr__(self):
        return f'<Problem(id={self.id}, name="{self.name}", difficulty={self.difficulty})>'


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __repr__(self):
        return f'<Tag(id={self.id}, name="{self.name}")>'


class ProblemTag(Base):
    """ many 2 many relationship between problems and tags """
    __tablename__ = 'problems_tags'

    problemId = Column(Integer, ForeignKey('problems.id'), primary_key=True)
    tagId = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    problem = relationship("Problem", back_populates="tags")
    tag = relationship("Tag", back_populates="problems")

    def __repr__(self):
        return f"<ProblemTag(problemId={self.problemId}, tagId={self.tagId})>"


Problem.tags = relationship("ProblemTag", order_by=ProblemTag.tagId, back_populates="problem")
Tag.problems = relationship("ProblemTag", order_by=ProblemTag.problemId, back_populates="tag")


class ProblemSet(Base):
    __tablename__ = "problemsets"

    problemSetType = Column(Integer, primary_key=True)  # contest = 0, gym = 1
    id = Column(Integer, primary_key=True)  # , autoincrement=False
    # source = Column(String(255))
    # name = Column(String(255))
    grade = Column(Integer)
    startTime = Column(DateTime)
    endTime = Column(DateTime)

    def __repr__(self):
        return f"<ProblemSet(problemSetType={self.problemSetType}, grade={self.grade}, " \
               f"startTime={self.startTime}, endTime={self.endTime}>"


class ProblemSetProblem(Base):
    """ many 2 many relationship between problemSets and problems """
    __tablename__ = "problemsets_problems"

    problemSetId = Column(Integer, ForeignKey('problemsets.id'), primary_key=True)
    problemId = Column(Integer, ForeignKey('problems.id'), primary_key=True)

    problemSet = relationship("ProblemSet", back_populates="problems")
    problem = relationship("Problem", back_populates="problemSets")

    def __repr__(self):
        return f"<ProblemSetProblem(problemSetId={self.problemSetId}, problemId={self.problemId})>"


ProblemSet.problems = relationship("ProblemSetProblem", order_by=ProblemSetProblem.problemId,
                                   back_populates="problemset")
Problem.problemSets = relationship("ProblemSetProblem", order_by=ProblemSetProblem.problemSetId,
                                   back_populates="problem")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    submittedBy = Column(Integer, ForeignKey('users.id'))
    problemId = Column(Integer, ForeignKey('problems.id'))
    # A whole number in [0..7] or in {0, 1},
    # depending on contest's grading policy.
    # -1 if submission is not yer graded.
    grade = Column(Integer)
    gradedBy = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Submission(submittedBy={self.submittedBy}, problemId={self.problemId}, grade={self.grade}" \
               f"{('gradedBy=' + str(self.gradedBy)) if self.grade != -1 else ''})>"


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    createdOn = Column(DateTime, default=datetime.datetime.utcnow)
    createdBy = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Group(name={self.name}, createdOn={self.createdOn}, createdBy={self.createdBy})>"


class GroupUser(Base):
    """ many 2 many relationship between groups and users """
    __tablename__ = 'groups_users'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'), primary_key=True)

    group = relationship("Group", back_populates="users")
    user = relationship("User", back_populates="groups")

    def __repr__(self):
        return f"<GroupUser(groupId={self.groupId}, userId={self.userId})>"


Group.users = relationship("GroupUser", order_by=GroupUser.userId, back_populates="group")
User.groups = relationship("GroupUser", order_by=GroupUser.groupId, back_populates="user")


class GroupBlogPost(Base):
    """ many 2 many relationship between groups and blog posts """
    __tablename__ = 'groups_blog_posts'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    blogPostId = Column(Integer, ForeignKey('blog_posts.id'), primary_key=True)

    group = relationship("Group", back_populates="blogPosts")
    blogPost = relationship("BlogPost", back_populates="groups")

    def __repr__(self):
        return f"<GroupBlogPost(groupId={self.groupId}, blogPostId={self.blogPostId})>"


Group.blogPosts = relationship("GroupBlogPost", order_by=GroupBlogPost.blogPostId, back_populates="group")
BlogPost.groups = relationship("GroupBlogPost", order_by=GroupBlogPost.groupId, back_populates="blogPost")


class GroupProblemSet(Base):
    """ many 2 many relationship between groups and problemSets """
    __tablename__ = 'groups_problemsets'

    groupId = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    problemSetId = Column(Integer, ForeignKey('problemsets.id'), primary_key=True)

    group = relationship("Group", back_populates="problemSets")
    problemSet = relationship("ProblemSet", back_populates="groups")

    def __repr__(self):
        return f"<GroupProblemSet(groupId={self.groupId}, problemSetId={self.problemSetId})>"


Group.problemSets = relationship("GroupProblemSet", order_by=GroupProblemSet.problemSetId, back_populates="group")
ProblemSet.groups = relationship("GroupProblemSet", order_by=GroupProblemSet.groupId, back_populates="problemSet")
