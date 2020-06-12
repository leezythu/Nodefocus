# Development Guild Book

from <b><i>Team Storms</i></b>



# 1 Introduction

### BASICS

This project was originally established for visualize professionals relation map in various degree. But now the colaboration with Aminer team has raised its bar to a higher standard. Which now our goal is to make a lightweight mobile platform for users to use our platform in a way that is similar to LinkedIn. We call our app "学脉", "The Learners".

Don's get me wrong, making a rip off version of LinkedIn is definitely not what we are looking for. What we want is a more academia-focused platform that gathers all academia related infomations and help our users to get what they want in the most intuitive and convienient way. 

### AMBITIONS

A platform that can help users to :

- Get infomation on their interested academia topics
- Establish connections with other learners
- Organize groups/events/lectures/activities among desired learners
- Setup their Academic Achievement



# 2 Product Details

##### List of Funtionalities:

- User profile and their custom data
- Feeds that is related to user's interests
- SNS functionalities
- (Optional/Later) Qualified Learner's Record/Certificates/History

(Explanations of each functionalities can be found below)

----

### User profile and their custom data

Allow users to log in and have their own custom data such as
- Interests
- Communities
- Associations
- Majors
- Labs
- etc...

### Feeds that is related to user's interests

- Feeds that is related to their interests (based on the users' personal data)
- Feeds of users/channels that a user is following
- Users are also allowed to create their own channels, post their own feeds, and so on.

### SNS functionalities

- Ability to connect with other friends/people and chat with them
- Groups in different areas (can be divided by their schools, their majors, their labs, AAAI conference etc.)
- In order to help people connect/reach out to other users, "Relation Map" is used to show one's connections in a visual way.

### (Optional/Later) Qualified Learner's Record/Certificates/History

This is something worth investigate in the future. Leaners can enter their achievements, certificates, records, and etc on the platform and use them to establish their social identity.

By having authoriezed authorities for certain kind of certificates might be more supportive to the legitimacy of one's history.

Blockchain might be a good solution for such functionality too.



# 3 Technical Solutions

##### Frontend Solutions:

- Flutter for mobile development

##### Backend Solutions:

- Currently using Flask python, but might change to Golang gin

##### Database:

- Mongodb

##### Data Fetching Cronjob:

- If webcrawler is needed, then scrapy framework will be used. 
- Other wise, any stable platform that can fetch data on time and correctly stores them to the database would be used. Nestjs is a good option.



# 4 Current Stage

So as it is still just a pre-matured idea, lots of discussions and brainstorming will be needed. 

##### Things needs to be decided:

1. Timeline / Milestones
2. Resources that are helpful to this project
3. Procedure of colaborations
4. etc......



# 5 Future Vision

The name "Learner" does not only stand for the professional researchers but also students. Therefore, would be cool if eventually we start to target schools to try our platform and let students to use it. But that's too much brainstorming for the moment. Should focus on the current matter first~!
