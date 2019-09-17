# **qmap**
CS 355 Term Project

# **CunyMap**(tentative title)
## **Project Members :**
Ahmad Fawad
Arthur Heesun
Ehsan Yasin A
Graber Shlomo
Htet Joseph Kaung
Lange Bryan Y
Legendre Bertin Junior
Lei Ming
Lomax Richard A
Nikitina Maria D
Ross Matthew O
Singh Harmandeep
Wang Xiaoxiao
Wu Evan

## **Project Scope :**
#### Creating a website that will allow a student to view the most successful course path to graduating quickly
- Project will be divided into groups with a heavy focus on technical direction<br>
There will be 2 teams, Frontend and Backend
    - The Frontend team will be focusing on the web stack's frontend layer
        - They will be responsible for establishing the entire UX and UI experience of the website, with a strong focus on efficient deliverability and a quality experience
        - This will include managing a unified project management system, separate from the Backend teams' but related to the main project's goals as dictated by leads and director
    - The Backend team will be focusing on the entire backend stack of the application
        - They will be responsible for implementing the programmatic backbone of the application, with a strong focus on scalability and modularity to be efficient in integrating with the other layers
        - This will include managing a separate project management system as well as implementing the entire data layer
- The infrastructure layer of the project will be a shared responsibility between teams, with teams leads negotiating closely with team director on how it should be setup most appropriately for project needs
    - Both teams will work in the same repository while isolating their code using the MVC workflow style
    - The infrastructure layer will not have a direct team allocation and thusly will not have a project management system. It will be the responsibility of each team to negotiate needs on a case by case basis with leads and the director to have the infrastructure requirements handled


## **Project Technologys:**
- Frontend
    - HTML5
    - ReactJS
    - Bootstrap
- Backend
    - Python
    - MySQL
- Infrastructure
    - Github
    - CircleCI
    - Venus

## **Project Data Need:**
All data should be in a format that can be read using MySQL
CRSE_CATALOG
CRSE_OFFER
Prerequisite structure for all offered courses, seperated by college
Major requirements for all included majors, seperated by college
Minor requirements for all included minors, seperated by college
Graduation requirements for all included colleges (including what gen eds are required, and how many credits are required)
Which semesters each course is offered
How many credits each course is worth

## **Project Milestones:**
1. **9/12** - Assignment
2. **9/17** - Allocate Teams, implement codebase in github, implement projects in github, enforce project roadmap for each team
3. **10/24** - Complete setup of codebase, using roadmap and wireframes, implement a dummy website not connected to backend that will display static data for UX, backend implement python and mysql platform and have test functions to ensure data integration is working, also setup deployment pipeline and system backend for UX testing. By this point in the project we should have our codebase defined, our roadmap of features set forth, and a website with a landing page, that will have some clickable elements that show some static, potentially irrelevant data just to show proof of concept. On the backend we should have some concept functions that can run basic queries to ensure we are able to establish platform database connectivity, as well as the feature roadmap for integrations to the backend(eg, with frontend) also as a proof of concept for how the rest of the platform development process will be going and the skeleton for the direction it will be taking
4. **11/21** - Ensure pipeline is capable of deploying autonomously, have frontend integration with backend established and begin roadmap for feature additions. By this point we should have a wireframe of the website available that has some basic navigation and can return some queued data from the backend directly via the site. This step is to show where the teams should be focusing on their integration with each other, so that can be kept in mind when working on features, that will be fleshing out the UI and more accurately controlling the platform's datasets
5. **12/12** - Ensure all new features are successful and submit working project
