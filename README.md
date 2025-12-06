
# P3 – Vehicle Build Tracker

The Vehicle Build Tracker is a full-stack Django web application that allows a workshop or custom vehicle builder to track each customer build from initial intake through key stages such as prep, paint, interior, and final testing.

The project was created as part of **Milestone Project 3 – Back-End Development** for the Code Institute Level 5 Diploma in Web Application Development.

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Stories](#user-stories)
- [UX and Design](#ux-and-design)
- [Data Model](#data-model)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Project Overview

Workshops that build or restore custom vehicles often manage projects using spreadsheets, email chains, or handwritten notes. This makes it difficult to see:

- Which vehicles are currently in progress
- Which customer owns each build
- Which build stage each vehicle is at
- What work has been completed and what is still outstanding

The **Vehicle Build Tracker** aims to solve this by providing a simple web interface where staff can:

- Create customers and link vehicles to them
- Record each vehicle build with a unique ID and status
- Add build stages (such as “Prep panels for paint”, “Body in paint”, “Interior trim”, “Final testing”)
- Update and delete stages as the build progresses

The focus of the project is to demonstrate:

- A relational database with linked models
- Full CRUD functionality (Create, Read, Update, Delete)
- A Django back end with templates and forms
- A clear, workshop-friendly user flow from vehicle list → detail → build stages.

---

## User Goals

- To quickly see all active vehicle builds and their current status.
- To view detailed information for a single build, including owner, build ID, and stages.
- To update progress without needing technical knowledge or access to raw databases.

---

## Site Owner Goals

- To have a central, maintainable system for tracking custom vehicle builds.
- To make it easier to give accurate progress updates to customers.
- To demonstrate full-stack back-end skills, including database design, CRUD, and deployment, for Milestone Project 3.
