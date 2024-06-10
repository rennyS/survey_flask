# Priority matrix

# Project Overview
- **Project Name**: Questionnaire Assessment Web App
- **Description**: A web application that allows users to create questionnaires, assign scores to responses, and perform assessments to determine priority levels based on the total score.
# Introduction
- **Purpose**: To provide a platform for creating and assessing questionnaires with a scoring system.
- **Scope**: Development of a web app using Flask and Python, with SQL database, user authentication, and client-side validation.
# System Architecture
- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS/JavaScript
- **Database**: SQL (e.g., SQLite, PostgreSQL)
- **Deployment**: On-premises server
# Component Design
- **User Authentication**: 
    - Registration
    - Login
    - Logout
- **Questionnaire Management**:
    - Create Questionnaire
    - Edit Questionnaire
    - Delete Questionnaire
- **Assessment Module**:
    - Start Assessment
    - Answer Questions
    - Calculate Score
    - Determine Priority (Low, Medium, High)
# Data Design
- **User Table**: Stores user credentials and profile information.
- **Questionnaire Table**: Stores questionnaire metadata.
- **Question Table**: Stores individual questions and associated scores.
- **Assessment Table**: Stores assessment results and scores.
# Security Considerations
- **Authentication**: Secure user login and session management.
- **Authorization**: Role-based access control for different functionalities.
- **Data Protection**: Secure storage and transmission of sensitive data.
# Performance Metrics
- **Response Time**: Ensure quick load times for questionnaire creation and assessment.
- **Scalability**: Ability to handle multiple users and assessments concurrently.
# User Interface Design
- **Questionnaire Creation Form**: Interface for creating and editing questionnaires.
- **Assessment Form**: Interface for answering questions and viewing results.
# API Documentation
- **Endpoints**:
    - `/register` : User registration
    - `/login` : User login
    - `/logout` : User logout
    - `/create-questionnaire` : Create a new questionnaire
    - `/start-assessment` : Start a new assessment
# Error Handling and Logging
- **Error Handling**: Graceful handling of user input errors and system failures.
- **Logging**: Maintain logs for user activities and system errors.
# Testing Strategy
- **Unit Testing**: Test individual components and functionalities.
- **Integration Testing**: Test interactions between different components.
# Deployment Plan
- **Server Setup**: Configure on-premises server for deployment.
- **Deployment Steps**: Steps to deploy the web app on the server.
# Maintenance and Support
- **Maintenance Plan**: Regular updates and bug fixes.
- **Support Resources**: Documentation and support contact information.


