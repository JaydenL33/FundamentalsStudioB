The Development Processes
*************************

The development process group SANITISE.media agreed on the agile development methods. The agile development method allows for an iterative process where requirements and potential
solutions that evolve throughout the project, as the scope becomes more evident as the project progresses. 

To facilitate this development method, our team has used several tools collectively and individually to manage team progress effectively. The following tools include
Microsoft teams; for team communication and ideas management and generation, GitHub; for collective and active development of code and the project, and lastly lab archives
for the individual logging of activities and ideas. 

The Team Processes
==================

This section describes each team member, their experience relevant to the project, and roles within the project. The leadership arrangements are also described here in
addition to establishing meeting arrangements. 

Details of the Team
-------------------

Team members and their experience and roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Albert Ferguson

    **Experience:**
    Extensive experience in Python, data mining and analytics (Pandas, Numpy, SciPy), data scraping (Selenium), database SQL management and design, data ETL and pipelining, backend design, 
    development operations (aka DevOps), Git, Canva and functional design.

    **Roles:**
    In charge of setting up the majority of the backend design specifically with the hosting of the website, Responsible for acquiring the raw data for processing and mining
    through the pipelines designed. Setting up the SQL database to store the raw data that has been scrapped. Setting up sphinx to help automate documentation of the final report. 

2. Cohen Bosworth

    **Experience:**
    mid-level experience in data analysis, data mining, Python, basic experience with SQL, JavaScript, front end design, backend design, HTML, web hosting, Git.

    **Roles**:
    Responsible for contributing to the data mining areas, using pandas, and various Python libraries (e.g. NumPy, Matplotlib). In addition to D3.js development and integration. 

3. Jayden Lee

    **Experience:**
    Extensive experience in backend development & design, system design & architecture, API routing, Python, data analytics, data mining, JavaScript, React.JS, dev-ops, node.js, Flask,
    Git, website design.

    **Roles:**
    Primarily responsible for the front to middle-end design and the associated API routes needed to interface between the database server set up by Albert, and the front end as setting up
    by Joel and Jayden. Also responsible for most of the front end, setting up node.js and react components to help build the website and its functionality. 

4. Joel Morrison
    
    **Experience:**
    Extensive experience with JavaScript, HTML, specifically front end design. Experience in designing and implementing websites, python, data analytics, Git.

    **Roles:**
    Primarily responsible for the development of the front-end interface and the various required scrolling effects and web pages. Further, helping Jayden with react development and JavaScript
    for the website.

Leadership arrangements
-----------------------

The decision of leadership arrangements concluded that Albert and Jayden take point on the project. This agreement is due to their extensive experience both have in setting up essential parts
of the project. By putting the two most experienced data engineers as lead role; allows faster deployment and sharing of information related to the data engineering tools and techniques necessary
to complete the project within the specified time requirements. 

Meeting arrangements
--------------------

Meeting arrangements, as set out at the start of the semester, established that group SANITISE.media would meet every Monday. This meeting should endeavour to coincide approximately to the
time of the Fundamental Studio B plenary session time. We would meet appropriately between 45 minutes to two hours to discuss our progress made as well as the next steps for the week ahead.
Contingency plans if the weekly meeting is not possible with everyone had led to a general time when everyone was available to meet. As per the subject requirements, we were to meet with Don
and Robin, where we discussed our progress where we are at, in addition to ideas that we could use in the project and add to our lab archives. 

Development process
------------------------------------

1. Inital Brainstorming

   The first major milestone in the development of the project was the initial brainstorming of several ideas of which the project will not only be based on but also brainstormed how it will look
   and how it will be built. Given the recent events at the time of brainstorming it was decided that the data visualisation should be based on and around viruses, particularly the effects of
   Covid19 on the world. 


2. Research

   Before any initial designing or developing for the project was conducted each member took the time to complete research in not only the science and impact behind Covid-19 but also areas, ideas
   or skills they were interested in further developing to be able to achieve the creation of the website. 


3. Project Outline and Design

   The above mention research into similar projects, methods of website creation and the overall data that was being discovered on the Covid-19 meant that the was better prepared when it came
   to the designing and creating a concrete project outline in which would direct all development of the project. The team then discussed the exact requirements that would be for the project to
   prove a success a successful and achieve its purpose of educating a larger audience. These requirements involved the creation and development of backend and a front end for the website. The
   project outline thus began with outlining the development of the alpha stage which would involve storyboarding, creating and designing basic key elements for there to be a simple but functioning
   solution.

4. Project Allocation

   Each member in the team chosen their own area in which they wanted to develop and from there individual tasks where assigned to each member which reflected the needs of the product as outlined as well as their interest and ability for the project which they will develop for the final prototype.

5.	Project Proposal

   The next major milestone in the development process was the creation of the project proposal which is a writing document that outline the research and project development that had been undertaken as well as what was planned for the future in terms of development of the project. 


6.	Website Development

   The next stage in development was the full creation of a more completed and refined solution that incorporated both the development of the backend and the frontend. This led to an optimised build and design of the website.


Outlined is the individual process and tasks that where completed during this development stage:

7.	Backend Development

  **-Creation of a Database management system**
  
  **-Hosting of Website**
  
  **-Data Mining**
  
  **-Data retrieval and transformation**

8.	Frontend Development

 **-Story Page**
 
 **-About Us Page**
 
 **-D3.js Development:**
 
 **Creation of Data Visualisation including Graphs.**


   
   
   
   
   
 

Gantt Chart of Development Process
------------------------------------

.. _labelGanttChart:

.. figure:: images/GANTT_CHART.png
    :alt: Gantt Chart of our Project Stages
    :width: 110%

    Gantt Chart of Development Process


Reflections
===========

Effectiveness of your team processes
------------------------------------

Reflecting upon the team processes that we have used throughout the project, the team generally agrees all team processes were active throughout the development of the project inclusive of
changing requirements, documenting all essential processes needed for the project to come together, in addition to effective communication and sharing of ideas needed throughout the project. 

By establishing a well organised GitHub allowed the tracking of all work that needed to be completed and work and progress throughout the project. Multiple branches were set up for different
purposes of the project. This process allowed development completed by each team member to be merged into one. 

Due to the current circumstances of COVID-19, we were all required to work from home we, therefore, had taken full advantage of Microsoft teams to ensure robust communication with team members,
ensuring effective communication of ideas, deadlines, in addition to collating resources that could be researched further for application within the project. 

Lastly, Lab archives being individual lead to the opportunity of self-evaluation and reflection upon the processes that our team had taken, in addition to the tasks assigned to each member.
Overall the team agreed on Lab archives being an effective way of documenting precisely each team member had completed relative to the project as a whole.

As for how the requirements have been met, SANITISE has used sufficient techniques available to us from the existing API routing framework. The API routing is used to ensure multiple components
of the project come together and are useable in the final product. Three levels of API are used where APIs are used to pull data from the database to the front end via the middle-ware flask server.
A database API was used to allow adaptability of the database to our project and other projects, in addition to setting up the necessary environment to interface successfully with the application.
Lastly an API ingest is used to take the raw data and transform it to be subsequently mined and then presented visually. This was integral in creating an efficient way to utilize large amounts of
raw data. 
