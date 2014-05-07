Fatal Crashes in Australia (2009-2013): Pivot Table Builder and Data Insights
=======================
Data source: https://www.bitre.gov.au/statistics/safety/fatal_road_crash_database.aspx

Contributors: Mubashwer Salman Khurshid (601738), Philip Lizio (582835), Asir Akram Sadman (601258) [INFO2002_2014S1_WED10_2]

=======================
Project Phase 3
An interactive web application [group]

This project specification may be updated to make corrections or clarifications; we will make an announcement about significant changes. 

To be completed by small groups (three students)
Late penalty: You will lose two marks for every day (or part thereof) that your submission is late.

Overview
The purpose of the project is to give you experience creating a non-trivial web-application which combines many of the skills and technologies you have learnt during the semester. It is also an opportunity for you to gain experience working in a team on a challenging task. 

You will implement an interactive web application in Python, which will be hosted on IVLE. Developing this application will involve data gathering, data processing, data visualisation and data analysis.

What data should you use for the application?

A dataset of your choice. Your application could use data in any format (CSV, XML or JSON), the data can be hosted in IVLE or retrieved remotely from an on-demand data service. You do not have to use all the data in the file, only a sufficient number of entries to show all the required functionality of the application and an interesting insight from the data. Note that IVLE places limiting constraints on how much computation your application can perform. Large data sets may cause your application to overstep those constraints.

Part 1: A pivot table builder (15%)

You need to design an interactive pivot builder of your selected dataset. This application should allow users to select two categorical attributes of your selected dataset, an attribute for the aggregated value, and a filter by value option. The cells of the pivot table output should be coloured according to the aggregated value. The colours can be taken from monochromatic or dichromatic palette.
 
Building pivot table means your dataset needs to have two or more categorical attributes (or columns). If your dataset contains only numerical data, generate new categorical attributes by applying equal interval classification (binning) on the selected numerical attributes.

The example application is available here. Note that this example is a very rudimentary solution to part 1. Your application needs to demonstrate more finesse, graceful error handling, and sophisticated interaction (e.g. selection of formulas applied to the value attribute, or better classification method) in order to get a high marks.

Part 2: An open-ended task (10%)

The goal of the second part of phase 3 is to demonstrate your capability in taking a dataset and (i) showing an interesting insight of the data through visualisation (visual analytics) or (ii) providing user with a way to interactively inspect the data. You can view this goal as developing an application for either confirmatory or exploratory data analytics.

You can start with a simple question or hypothesis like "Melbourne has been getting warmer in the last 50 years" and use visualisation to argue for your hypothesis. Obviously, there is an expectation to provide in-depth analysis of the solution. For this example, you can not simply produce a single line chart of Melbourne's average temperature over the last 50 years, you may want to show the variance, mean maximum, or longer summer within the period. As a guidelines, you should produce 5 visualisations or insights from your data.

Reuse the dataset you work with in part 1. You may reuse some of your work in part 1, but you can also build something totally new.

Requirements

You should produce an interactive web application that has at least the following properties:

It should be implemented in Python, and must function correctly when hosted on IVLE. 
It must use CGI and forms to get input from the user.
It must use valid XHTML or HTML5 to display output to the user.
It must use CSS appropriately in providing the visual aspect of the application.
You may use JavaScript for your application, but your code will not be assessed.

Marking Guide for the application

This stage of the project is worth 30% of your total mark (25% application + 5% group presentation).

Your program will be assessed for correctness and quality. A program of high quality has the following properties:

It is well documented. 
It is well structured:
It is decomposed into sensible and logical functions.
It uses library code where appropriate.
Program statements are not too long or complex.
Variable names are well chosen and meaningful.
It avoids unnecessary repetition of code.
Program constants, such as file names and special numbers, are defined in one place so they can be modified easily.
It is reasonably robust and can deal with errors gracefully.

Groupwork Guide

To work successfully in a team, please look at the following guide. In addition, we will require you to use a group subversion repository for all your work in this project, which your tutor should have helped you set up. If you do not have a group repository, please contact one of the subject coordinators as soon as possible. The repository should contain not just the final polished version of your code: you should be checking in intermediate versions that work to some extent, but are not yet complete, for instance. You should use it as a way of sharing files, and of keeping track of who has done what. Use the commit messages in subversion to assist in identifying what exactly you have contributed to the project, as well as your own development log files.
Presentation

Overview

Each group must make a presentation in the final workshop for the semester. You will make the presentation in your normal workshop time. The presentation is worth 5% of your mark for the subject.

The presentation should take roughly 10-15 minutes. Each member of the group must speak in the presentation, therefore you must make sure that all group members attend your final workshop.

You may use slides in the presentation (but they are not required). If you choose to use slides, then you should bring them on a USB stick to the workshop. Microsoft PowerPoint and PDF formats should work on the machines in the labs, but it is your responsibility to check before your final workshop.

The presentation should address (at least) each of the following four issues:

What are the main features of your application? 
Describe the steps you have taken in developing the project: data gathering, data processing, data visualisation, and data analysis. 
How did you structure your application and solution?

You should be prepared to answer questions from your workshop demonstrator and the other students in your workshop at the end of the presentation.

Marking Guide for the presentation

You will be marked according to the following criteria:

Was the presentation clear, coherent and well structured?
Did each member of the group participate equally in the presentation?
Did the presentation address each of the four issues listed above?
How well were questions answered?
