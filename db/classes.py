import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
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

  def writeBlogPost(self, userSession, blogPostTitle):
    userSession.add(BlogPost(authorId=self.id, title=blogPostTitle))
    userSession.commit()

  def addProblemTag(self, userSession, problemId, tagId):
    # check if user is admin or teacher
    if self.userType == 0 or self.userType == 1:
      userSession.add(ProblemTag(problemId=problemId, tagId=tagId))
      userSession.commit()
    else:
      raise PermissionError("Student cannot add tag to problem!\n")

  def addProblemTags(self, userSession, problemId, tagIds):
    # check if user is admin or teacher
    if self.userType == 0 or self.userType == 1:
      for tagId in tagIds:
        self.addProblemTag(userSession, problemId, tagId)
      userSession.commit()
    else:
      raise PermissionError("Student cannot add tags to problem!\n")

  def createProblem(self, userSession, problemName, problemDifficulty=None):
    # check if user is admin or teacher
    if self.userType == 0 or self.userType == 1:
      userSession.add(Problem(name=problemName, difficulty=problemDifficulty))
      userSession.commit()
    else:
      raise PermissionError("Student cannot create problem!\n")


class BlogPost(Base):
  __tablename__ = 'blogposts'

  authorId = Column(Integer, ForeignKey('users.id'))
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(255))
  publishedOn = Column(DateTime, default=datetime.datetime.utcnow)

  author = relationship("User", back_populates="blogposts")

  def __repr__(self):
    return f'<BlogPost(id={self.id}, authorId={self.authorId}, title="{self.title}", publishedOn={self.publishedOn})>'


User.blogposts = relationship("BlogPost", order_by=BlogPost.id, back_populates="author")


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
  """ many2many relationship between problems and tags """
  __tablename__ = 'problems_tags'

  problemId = Column(Integer, ForeignKey('problems.id'), primary_key=True)
  tagId = Column(Integer, ForeignKey('tags.id'), primary_key=True)

  problem = relationship("Problem", back_populates="tags")
  tag = relationship("Tag", back_populates="problems")

  def __repr__(self):
    return f"<ProblemTag(problemId={self.problemId}, tagId={self.tagId})>"


Problem.tags = relationship("ProblemTag", order_by=ProblemTag.tagId, back_populates="problem")
Tag.problems = relationship("ProblemTag", order_by=ProblemTag.problemId, back_populates="tag")
