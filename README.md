# Data Engineering Website for the Michihgan Daily Web Team
Final Project for SI 364

This is a public facing website for the Michigan Daily Data Engineering team. This web application displays all the work done by the team throughout the year. As well, it serves a functional purpose by allowing the organization to run more efficiently. Team members will be able to see what projects need to be worked on. As well, different departments can view the projects that data engineering is working on, projects that have been published in the paper, and it shows indiviudals who are working on the different projects displayed on the site.  Departments will be able to reach out to the team if they want to collaborate on a project being worked on. 

The website will allow logged-in end users to input different projects they are working on, enter in start dates and end dates when different steps of a project get completed, and information about themselves (i.e, email and phone number). This project is similar to Salesforce. Salesforce is a platform that companies use for case management and task management.  At the company I worked for last summer we used Salesforce to keep track of all different cases we were working on, and a platform like this will be very useful for the Data Engineering team. 

The data that will be featured on the website is information about the people working on the team, data about projects and their progress, and if a project has been published in the Newspaper.


Table Descriptions: 

I will have six tables in total: people, projects, published, sections, study, and progress. The people table shows information about individuals' who work on the team. The attributes of this table include, PersonId, FirstName, LastName, StartMonth (date they started working on the Data Engineering team), EndMonth (date they stopped working on the Data Engineering -- if they are currently working then NULL), MajorId, MinorId, Email, UmichId, PhoneNumber, Year, Role. This table has a relationship to the tables projects, study , progress, and published. 

The study table contains information about majors and minors. It has the attributes MajorId, MajorName, MinorId, and MinorName. This is where the people table gets the MinorId and MajorId data from. This table has a relationship with the people table. 

The projects table has information about past projects and projects we are currently working on. The attributes of this table is ProjectId, PersonId, Description, StartDate (date project was started- null if has not been started), EndDate (date project ended- null if has not ended), Published (no if it has not been published and yes if has been published). The projects table gets the PersonId from the people table. The PersonId refers to the person who is working on this project. The project table has relationships to the people and published tables. 

The Published table has data containing if a project has been published or not. It contains the attributes ProjectId, Published (no if has not been published and yes if has been published), PersonId, SectionId, SectionName. The ProjectId refers to the project table, the PersonId refers to the person, and the SectionId refers to the section table. This table has a relationship with the projects, people, and sections. 

The Sections table has information containing all the different sections in the Michigan Daily Newspaper. The attributes of this table are SectionId and Name. This table has a relationship with the published table. 

Finally, there is a progress table that has information about all the different projects being worked on. There are three steps to a data process: data gathering, analysis, and visualization. These steps are reflected in this table. This table has attributes: ProjectId, PersonIdDataGathering,DataGatheringStartDate, DataGatheringEndDate,  AnalysisStartDate, PersonIdAnalysis,AnalysisEndDate, VisualizationStartDate, PersonIdVisualization, VisualizationEndDate. A different person can work on different aspects of a project; therefore multiple people can work on one project. The ProjectId refers to the ProjectId table, and the PersonIdDataGathering,PersonIdAnalysis, and PersonIdVisualization refers to the people table. This table has a relationship with the projects and people table. 


The person table has a many to one relationship with the published table, many to many relationship with the progress table, many to many relationship with the projects table, and one to many relationship with the study table. The projects table has a many to one relationship with the published table, and a one to one relationship with the progress table. The sections table has a one to one relationship with the published table. 



