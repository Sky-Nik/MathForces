#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from classes import *
import os


os.remove('mf.db')
engine = create_engine('sqlite:///mf.db')  #, echo=True)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# region users and blogs
me = User(userType=0, handle="Nikita.Skybytskyi", password="EnY$&l^T")
session.add(me)

kate = User(userType=0, handle="Pateryna", password="aS@e%f35")
session.add(kate)

session.commit()

myFirstPost = BlogPost(authorId=me.id, title="some title")
session.add(myFirstPost)
session.commit()

me.writeBlogPost(userSession=session, blogPostTitle="some other title")

for user in session.query(User).all():
  print(user)
  for blogPost in user.blogposts:
    print(f'\t{blogPost}')
  print()
# endregion

# region problems and tags
session.add(Problem(name="Game with divisors", difficulty=1000))
session.commit()

session.add_all([
  Tag(name="number theory"),
  Tag(name="combinatorics"),
  Tag(name="games"),
  Tag(name="questions")
])
session.commit()

session.add_all([
  ProblemTag(problemId=1, tagId=1),
  ProblemTag(problemId=1, tagId=2),
  ProblemTag(problemId=1, tagId=3),
])
session.commit()

me.createProblem(userSession=session, problemName="Sphinx and three numbers", problemDifficulty=1200)
me.addProblemTags(userSession=session, problemId=2, tagIds=[2, 3, 4])

student = User(userType=2, handle="sample", password="12345678")
session.add(student)
try:
  # should fail as student does not have enoght rights to create new problems
  student.createProblem(userSession=session, problemName="Interesting fractions")
except Exception as e:
  print(e)
try:
  # nor they have rights to  add tags to existing problems
  student.addProblemTag(userSession=session, problemId=1, tagId=4)
except Exception as e:
  print(e)

for problem in session.query(Problem).all():
  print(problem)
  for ProblemTag in problem.tags:
    print(f'\t{ProblemTag}')
  print()
# endregion
