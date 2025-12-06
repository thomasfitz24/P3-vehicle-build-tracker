
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


## User Stories

### As a customer service advisor:

1. I want to view a list of all customer vehicles so I can quickly see which builds are currently active.
2. I want to be able to click on a vehicle to view its full build history and stages.
3. I want each vehicle to have a unique build ID so I can accurately identify it in communication with customers.
4. I want to see each vehicle’s latest status so I know whether it is in progress, waiting on parts, or completed.

### As a workshop technician:

5. I want to add new build stages to a vehicle so I can record work that needs to be completed.
6. I want to edit a build stage so I can update progress during the build.
7. I want to delete a stage if it is added by mistake or becomes irrelevant.
8. I want the stages to be displayed in a consistent order so I can read the timeline of the build clearly.

### As the site owner:

9. I want to add new vehicles to the system and link them to a customer so I can track all active builds.
10. I want to edit and delete vehicles so I can manage the database cleanly during the project lifecycle.
11. I want the system to be simple and intuitive so workshop staff can use it without training.
12. I want the data to be stored securely and reliably so progress is never lost.

### As an admin:

13. I want to manage customers, vehicles, and stages in the Django admin so I can oversee the system.
14. I want all models to be searchable and filterable so I can find records quickly.


## Data Model

The application uses a relational database structured around three core models:

### **Customer**

Represents a person who owns one or more vehicle builds.

**Fields:**

- `first_name` – Customer first name
- `last_name` – Customer last name
- `email` – Optional contact email
- `phone` – Optional contact phone number
- `created_at` – Timestamp for when the customer was added

A customer can have **multiple vehicles** associated with them (one-to-many).

---

### **Vehicle**

Represents a single vehicle being built or restored.

**Fields:**

- `customer` – ForeignKey linking to Customer
- `make` – Vehicle manufacturer
- `model` – Model name
- `year` – Optional manufacturing year
- `vin_or_id` – Unique internal build ID or VIN
- `status` – Active, Completed, or On Hold
- `created_at` – Timestamp for when the vehicle record was created

A vehicle can have **multiple build stages** (one-to-many).

---

### **BuildStage**

Represents an individual stage of the build process.

**Fields:**

- `vehicle` – ForeignKey linking to Vehicle
- `name` – Stage name

### Explanation:

- One **Customer** can own many **Vehicles**
- One **Vehicle** can contain many **BuildStages**
- BuildStages cannot exist without a Vehicle
- Vehicles cannot exist without being assigned to a Customer

This structure allows the workshop to track each step of the build from intake to completion.


## Features

### Existing Features

#### 1. Vehicle List Page

- Displays all vehicles stored in the system.
- Shows key information at a glance: make, model, internal build ID, and owner name.
- Provides a link to view full details for each vehicle.
- Includes a clear call-to-action to **add a new vehicle**.

#### 2. Vehicle Detail Page

- Shows full information for a single vehicle:
  - Owner
  - Build ID
  - Status
- Lists all associated build stages in order.
- Provides links to:
  - Add a new build stage
  - Edit the vehicle
  - Delete the vehicle
  - Return to the vehicle list

#### 3. Vehicle CRUD (Create, Read, Update, Delete)

- **Create**: Form to add a new vehicle and assign it to a customer.
- **Read**: Vehicle list and detail views.
- **Update**: Edit view using a ModelForm to update vehicle information.
- **Delete**: Confirmation page before a vehicle is permanently removed.

#### 4. Build Stage CRUD

- **Create**: Ability to add new stages for a specific vehicle (e.g. “Prep panels for paint”, “Body in paint”).
- **Read**: All stages are displayed on the vehicle detail page, in a logical order.
- **Update**: Edit view to update name, status, description, and dates of a stage.
- **Delete**: Confirmation page before removing a stage from the build.

#### 5. Django Admin Integration

- Admin interface configured for:
  - Customers
  - Vehicles
  - BuildStages
- List displays show key fields for quick overview.
- Search and filter options make it easier to find specific builds or customers.
- Useful during development to seed data and manage records.

---

### UX and Design (Current State)

- The project currently uses simple Django templates to prioritise clarity and functionality.
- Pages focus on:
  - Clear headings (Vehicle List, Vehicle Detail, Build Stages)
  - Logical navigation (list → detail → form → back again)
  - Minimal styling to keep the focus on back-end features for Milestone 3.

Further styling and layout improvements are listed in the **Future Enhancements** section.
