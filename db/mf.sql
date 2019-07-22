CREATE TABLE groups_users (
	"groupId" INTEGER NOT NULL, 
	"userId" INTEGER NOT NULL, 
	PRIMARY KEY ("groupId", "userId"), 
	FOREIGN KEY("groupId") REFERENCES groups (id), 
	FOREIGN KEY("userId") REFERENCES users (id)
)

CREATE TABLE groups_problemsets (
	"groupId" INTEGER NOT NULL, 
	"problemSetId" INTEGER NOT NULL, 
	PRIMARY KEY ("groupId", "problemSetId"), 
	FOREIGN KEY("groupId") REFERENCES groups (id), 
	FOREIGN KEY("problemSetId") REFERENCES problemsets (id)
)

CREATE TABLE groups_blog_posts (
	"groupId" INTEGER NOT NULL, 
	"blogPostId" INTEGER NOT NULL, 
	PRIMARY KEY ("groupId", "blogPostId"), 
	FOREIGN KEY("groupId") REFERENCES groups (id), 
	FOREIGN KEY("blogPostId") REFERENCES blog_posts (id)
)

CREATE TABLE submissions (
	id INTEGER NOT NULL, 
	"submittedBy" INTEGER, 
	"problemId" INTEGER, 
	grade INTEGER, 
	"gradedBy" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("submittedBy") REFERENCES users (id), 
	FOREIGN KEY("problemId") REFERENCES problems (id), 
	FOREIGN KEY("gradedBy") REFERENCES users (id)
)

CREATE TABLE problems_tags (
	"problemId" INTEGER NOT NULL, 
	"tagId" INTEGER NOT NULL, 
	PRIMARY KEY ("problemId", "tagId"), 
	FOREIGN KEY("problemId") REFERENCES problems (id), 
	FOREIGN KEY("tagId") REFERENCES tags (id)
)

CREATE TABLE problemsets_problems (
	"problemSetId" INTEGER NOT NULL, 
	"problemId" INTEGER NOT NULL, 
	PRIMARY KEY ("problemSetId", "problemId"), 
	FOREIGN KEY("problemSetId") REFERENCES problemsets (id), 
	FOREIGN KEY("problemId") REFERENCES problems (id)
)

CREATE TABLE groups (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	"createdOn" DATETIME, 
	"createdBy" INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY("createdBy") REFERENCES users (id)
)

CREATE TABLE blog_posts (
	"authorId" INTEGER, 
	id INTEGER NOT NULL, 
	title VARCHAR(255), 
	"publishedOn" DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY("authorId") REFERENCES users (id)
)

CREATE TABLE users (
	"userType" INTEGER NOT NULL, 
	handle VARCHAR(255) NOT NULL, 
	password VARCHAR(255) NOT NULL, 
	email VARCHAR(255) NOT NULL, 
	country VARCHAR(255), 
	"registredOn" DATETIME, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (handle), 
	UNIQUE (email)
)

CREATE TABLE tags (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

CREATE TABLE problemsets (
	"problemSetType" INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	grade INTEGER, 
	"startTime" DATETIME NOT NULL, 
	"endTime" DATETIME NOT NULL, 
	PRIMARY KEY ("problemSetType", id)
)

CREATE TABLE problems (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	difficulty INTEGER, 
	PRIMARY KEY (id)
)