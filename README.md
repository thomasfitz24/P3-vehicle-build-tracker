# P3 – Vehicle Build Tracker

The Vehicle Build Tracker is a full-stack Django web application that allows a workshop or custom vehicle builder to track each customer build from initial intake through key stages such as prep, paint, interior, and final testing.

The project was created as part of **Milestone Project 3 – Back-End Development** for the Code Institute Level 5 Diploma in Web Application Development.

## Table of Contents

* [Project Overview](#project-overview)
* [Rationale](#rationale)
* [Screenshots](#screenshots)
* [User Goals](#user-goals)
* [Site Owner Goals](#site-owner-goals)
* [User Stories](#user-stories)
* [UX and Design](#ux-and-design)
* [Wireframes]()
* [Data Model](#data-model)
* [Data Model Diagram (ERD)]()
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Requirements](#requirements)
* [Deployment](#deployment)
* [Credits](#credits)

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

## Rationale

The primary goal of the Vehicle Build Tracker is to provide a focused, database-driven tool for managing custom vehicle builds in a workshop environment. Instead of relying on spreadsheets, emails, or handwritten notes, the project offers a structured way to record customers, vehicles, and build stages from initial intake through to completion. This aligns directly with the brief for Milestone Project 3 by demonstrating a full back-end solution with clear CRUD functionality and relational data design.

The motivation for this project comes from the reality of how many small workshops actually operate. Custom builds are often coordinated through informal systems: shared Excel files, WhatsApp chats, and ad-hoc notes on job sheets. These methods work until the number of vehicles and customers grows, at which point it becomes difficult to answer simple questions like “What stage is this vehicle at?” or “Which builds are close to completion?”. Miscommunication, duplicated information, and missed stages all become more likely when there is no single source of truth.

From a back-end development perspective, this creates a clear opportunity. A relatively small set of core entities—Customer, Vehicle, and BuildStage—captures most of the domain logic needed to track a build. By modelling these explicitly in a relational database and exposing them through a Django application, the project can give workshops a more reliable and maintainable way to manage builds while also satisfying the pedagogical goals of the course (models, views, templates, forms, and admin).

The specific problem the project addresses is the lack of a central, structured place to see the current status and history of each vehicle build. Without such a system, it is difficult for staff to know which builds are active, which stages have been completed, and what work is coming next. This problem affects customer-facing staff (who need clear updates), technicians (who need to see stage sequences), and the workshop owner (who needs an overview of all ongoing work).

The Vehicle Build Tracker proposes a simple but focused solution:

- Each **Customer** can be created once and linked to any number of **Vehicles**.
- Each **Vehicle** has a unique build ID, basic specs, and an overall status.
- Each **BuildStage** records a named step in the process, its status, order, and key dates.

Together, these features create a straightforward workflow: staff can list all vehicles, open a specific build, and then read or update the stages associated with it. The application includes full CRUD for both Vehicles and BuildStages, plus admin support for managing customers and seeding data. This keeps the scope realistic while still demonstrating the core patterns expected of a back-end project.

Compared with informal tracking methods, this approach offers several benefits. It reduces the risk of losing information because all data is stored in a single database rather than scattered across tools. It improves clarity, as each vehicle has a dedicated detail page showing its owner, build ID, status, and stages in order. It also improves consistency: stages follow the same structure for every build, making it easier to standardise workshop processes over time. From a learning perspective, it shows how a relatively small codebase can provide meaningful value by modelling the right entities and relationships.

The scope of the current project is deliberately focused on internal workshop use. The application does not yet implement user authentication, role-based permissions, a customer-facing portal, or advanced UI design. Deployment is targeted at a single environment rather than a multi-tenant or multi-workshop setup. These constraints keep the codebase manageable and ensure that the core learning outcomes (Django models, CRUD views, forms, templates, and deployment) are implemented to a good standard before additional complexity is added.

Future enhancements could extend the project in several directions. For example, adding authentication would allow different roles (admin, technician, service advisor) with different permissions. A customer portal could provide read-only access to build statuses. Search and filtering could help staff find builds by customer, build ID, or status. Finally, more advanced UI and visual progress components (timelines, progress bars, dashboards) could make the system even more usable day-to-day.

In summary, the Vehicle Build Tracker exists to solve a clear, real-world problem: the difficulty of managing custom vehicle builds with informal tools. By modelling customers, vehicles, and build stages in a relational database and exposing them through a Django application, the project delivers a practical, maintainable solution while directly meeting the learning and assessment goals of Milestone Project 3.

## Screenshots

Below are the key screenshots required for Milestone Project 3 assessment:

### Home (Vehicle List) Page

- Shows all vehicles in the system.
- Includes “Add Vehicle” button and navigation bar.

### Vehicle Detail Page

- Displays full build information for a selected vehicle.
- Shows build stages, edit/delete buttons, and stage actions.

### Add Vehicle Form

- Demonstrates form validation and correct CRUD handling.

### Edit Vehicle Form

- Shows update functionality and existing data pre-filled.

### Add Build Stage Form

- Shows ability to add new build stages linked to a vehicle.

### Edit Build Stage

- Demonstrates updating a stage with validation.

### Delete Confirmation Pages

- Vehicle delete confirmation
- Build stage delete confirmation

### Django Admin Panel

- Showing Customers, Vehicles, and Build Stages in admin.
- Includes search, filters, and model overview.

### Success Messages

- Example: “Vehicle added successfully”
- Example: “Stage deleted”
- Example: “Vehicle updated”

<img width="1442" height="489" alt="Screenshot 2025-12-06 at 20 30 19" src="https://github.com/user-attachments/assets/e19d0fac-e19d-46f6-8a1c-4b5de58b6e8a" />
<img width="1463" height="619" alt="Screenshot 2025-12-06 at 20 30 02" src="https://github.com/user-attachments/assets/915d2c43-5370-4adb-971f-d7b1b7440c75" />
<img width="1440" height="594" alt="Screenshot 2025-12-06 at 20 29 11" src="https://github.com/user-attachments/assets/53f67eb6-155e-4086-a6ee-233560eca700" />
<img width="699" height="249" alt="Screenshot 2025-12-06 at 20 28 03" src="https://github.com/user-attachments/assets/7f7186f8-f529-40f1-9253-72422fd4a55b" />
<img width="637" height="224" alt="Screenshot 2025-12-06 at 20 27 52" src="https://github.com/user-attachments/assets/94e39366-79ad-40cf-8d03-7e206f71f02c" />
<img width="613" height="488" alt="Screenshot 2025-12-06 at 20 27 09" src="https://github.com/user-attachments/assets/580acb7c-42b8-4cea-9f19-de9fb92e6cfc" />
<img width="538" height="389" alt="Screenshot 2025-12-06 at 20 25 52" src="https://github.com/user-attachments/assets/439f7c1e-aaed-4e2d-8334-0668d94d3ae0" />
<img width="782" height="394" alt="Screenshot 2025-12-06 at 20 25 31" src="https://github.com/user-attachments/assets/bb7f6fa1-4165-47e4-b4b9-f6914c60e7b4" />
<img width="533" height="448" alt="Screenshot 2025-12-06 at 20 24 48" src="https://github.com/user-attachments/assets/70ef843b-8414-49cc-9acb-673ee3af809a" />
<img width="692" height="216" alt="Screenshot 2025-12-06 at 20 24 30" src="https://github.com/user-attachments/assets/bb1dadb9-2706-4ec2-b510-87335c0e7e8d" />

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

## UX and Design

The focus of this project is on back-end functionality and data modelling, so the UX is intentionally kept simple and clear.

### Information Architecture

The core flow for a user is:

1. **Vehicle List** – entry point showing all vehicles and a link to add a new one.
2. **Vehicle Detail** – focused view of a single build, showing the owner, build ID, status, and all build stages.
3. **Stage Forms** – small, focused forms for adding or editing build stages.
4. **Navigation Links** – “Back to all vehicles” and “Back to vehicle” links keep the user in a clear loop.

### Design Choices

- Clear headings for each page (Vehicle List, Vehicle Detail, Build Stages).
- Simple, form-based interface to reduce cognitive load for workshop staff.
- Minimal styling to keep the emphasis on functionality and CRUD behaviour for Milestone 3.
- Consistent use of links and buttons for actions (Add, Edit, Delete) so the user always understands what will happen next.

Further visual styling, layout improvements, and responsive design are listed in the **Future Enhancements** section.

## Wireframes

The initial planning for the Vehicle Build Tracker included two core wireframes representing the main user interactions within the system. These wireframes helped define layout, navigation, and expected user flow before development began.

### Vehicle List Wireframe

This screen shows the main landing page of the application, listing all vehicles currently in the system along with an option to add a new vehicle.

*(Insert your Vehicle List wireframe image here)*

### Add Vehicle Wireframe

This form allows a user to add a new vehicle to the system, selecting a customer and entering the vehicle details.

*(Insert your Add Vehicle wireframe image here)*

# Data Model Diagram (ERD)

The following Entity Relationship Diagram shows the structure of the relational database used in the Vehicle Build Tracker:

### Explanation of Relationships

* **Customer → Vehicle (1-to-Many)**

  Each customer can own  **multiple vehicles** , but every vehicle belongs to **exactly one** customer.
* **Vehicle → BuildStage (1-to-Many)**

  Each vehicle contains  **multiple build stages** , but every build stage is linked to  **one specific vehicle** .

### Why this structure fits the domain

This model reflects a real workshop environment:

* A customer may have several builds over time.
* A vehicle progresses through multiple defined stages (prep, paint, interior, testing).
* Build stages cannot exist independently — they must always belong to a vehicle.

This schema fully supports CRUD operations and meets the Unit 3 requirement for a  **well-designed relational data model**

Represents a person who owns one or more vehicle builds.

**Fields:**

- `first_name` – Customer first name
- `last_name` – Customer last name
- `email` – Optional contact email
- `phone` – Optional contact phone number
- `created_at` – Timestamp for when the customer was added

A customer can have **multiple vehicles** associated with them (one-to-many).

---

### Vehicle

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

### Explanation:

### BuildStage

Represents an individual stage of the build process.

**Fields:**

- `vehicle` – ForeignKey linking the stage to a Vehicle
- `name` – Stage name (e.g., “Prep panels for paint”)
- `description` – Optional detail describing the work performed
- `status` – Not Started, In Progress, Blocked, or Complete
- `order` – Integer controlling the order stages are displayed
- `due_date` – Optional expected completion date
- `completed_date` – Optional timestamp for when the stage is finished
- `created_at` – Auto timestamp when the stage is created
- `updated_at` – Auto timestamp updated whenever the stage is changed
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

## Technologies Used

### Languages

- **Python** – Primary back-end development language.
- **HTML** – Used for Django templates.
- **CSS** – (Minimal) For basic layout and structure.

### Frameworks and Libraries

- **Django (Python Web Framework)**
  - MVC/MVT architecture
  - URL routing
  - Django ORM for database management
  - Django templates
  - Django admin for internal management

### Tools & Services

- **Git & GitHub** – Version control, commits, and project backups.
- **VS Code** – Primary development environment.
- **SQLite** – Default Django relational database for development.
- **Pip & Virtualenv** – Package and environment management.
- **Browser DevTools** – Manual testing and layout inspection.

## Testing

Testing for this project was carried out manually throughout development.
The following areas were tested:

### 1. Page Rendering

- All key pages load without errors:
  - Vehicle List
  - Vehicle Detail
  - Add Vehicle
  - Edit Vehicle
  - Delete Vehicle
  - Add Stage
  - Edit Stage
  - Delete Stage

### 2. CRUD Operations

- **Vehicles**: Create / Read / Update / Delete
- **Stages**: Create / Read / Update / Delete
- Correct redirects after form submission.
- Confirmation screens appear before destructive actions.

### 3. Form Validation

- Required fields must be completed.
- VIN/build ID must be unique (enforced in the model).
- Invalid form submissions correctly re-render with errors.

### 4. User Flow

- Navigation between list → detail → form pages is smooth.
- “Back to all vehicles“ and “Back to vehicle“ links work as expected.

### 5. Admin Testing

- Records can be created, edited, and deleted in Django Admin.
- Search and filter functionality works correctly.
- All models appear in admin.

---

### Future Enhancements

### Manual Test Cases

| Test Name                                | Input                                      | Expected Result                                      | Actual Result | Pass/Fail |
| ---------------------------------------- | ------------------------------------------ | ---------------------------------------------------- | ------------- | --------- |
| Load Vehicle List Page                   | Visit `/`                                | Page loads with heading and “Add New Vehicle” link | As expected   | Pass      |
| Create Vehicle                           | Fill form with valid data                  | Vehicle is saved and visible in list                 | As expected   | Pass      |
| Create Vehicle (Missing Required Fields) | Submit empty form                          | Form errors appear                                   | As expected   | Pass      |
| View Vehicle Detail                      | Click a vehicle in the list                | Detail page loads with all info                      | As expected   | Pass      |
| Edit Vehicle                             | Change vehicle info in form                | Updates appear on detail page                        | As expected   | Pass      |
| Delete Vehicle                           | Confirm delete                             | Vehicle removed and list updates                     | As expected   | Pass      |
| Add Build Stage                          | Fill form with valid fields                | Stage appears under vehicle                          | As expected   | Pass      |
| Edit Build Stage                         | Modify stage info                          | Updates appear under vehicle                         | As expected   | Pass      |
| Delete Build Stage                       | Confirm delete                             | Stage removed from list                              | As expected   | Pass      |
| Navigation Check                         | Use all “Back” and “Edit/Delete” links | All links route correctly                            | As expected   | Pass      |

Although the core CRUD features are complete, there are several planned improvements that would make the system more powerful and user-friendly:

### 1. Improved UI and Styling

- Use a shared base template (`base.html`)
- Add a navigation bar
- Introduce responsive design
- Apply consistent CSS styling throughout

### 2. User Authentication

- Allow staff to log in and manage builds securely
- Add permissions (e.g., only admins can delete vehicles)

### 3. Progress Tracking / Timeline View

- Visual representation of build stages (e.g., timeline / progress bar)
- Colour-coded stage statuses

### 4. File Uploads

- Allow images or documents to be attached to build stages
- Useful for workshop photos or inspection reports

### 5. Search and Filtering

- Search for vehicles by build ID, customer, or model
- Filter by status (Active / Completed / On Hold)

### 6. Customer Portal (Long-Term Goal)

- A read-only portal where customers could log in and view build progress
- Optional ability for customers to upload documents such as inspiration images
- Integration with notifications (email or SMS)

---

## Requirements

Before deployment or running locally, ensure:

- Python 3.12+
- Django installed via requirements.txt
- A virtual environment is activated
- All migrations have been applied:
  `python manage.py migrate`

---

## Deployment

The project can be deployed using either **Heroku** or **Render**.
The following steps outline deployment using **Render**, which is currently the recommended free option.

### 1. Requirements

Before deployment, ensure:

- Your `requirements.txt` file is up to date:pip freeze > requirements.txt2. Push Code to GitHub Deployment is linked to the GitHub repository used for this project.
- A `Procfile` is included with: web: gunicorn tracker.wsgi

### 2. Push Code to GitHub

Deployment is linked to the GitHub repository used for this project.

### 3. Create a Render Web Service

1. Go to https://render.com
2. Create a new **Web Service**
3. Connect your GitHub account and select this repository
4. Set:

- **Runtime:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn tracker.wsgi`
- **Environment:** `PYTHON_VERSION=3.12`

### 4. Set Django Environment Variables

Add the following environment variables in Render::

- `SECRET_KEY=<your secret key>`
- `DEBUG=False`
- `ALLOWED_HOSTS=your_render_domain`

### 5. Run Database Migrations

In the Render dashboard shell: python manage.py migrate

### 6. App Live

Once deployment completes, the live link will appear on your Render dashboard.

---

**Note:**
For the milestone submission, a working deployed version is required, along with screenshots or confirmation of deployment steps.

## Credits

- Django documentation for guidance on model design and CRUD patterns.
- Code Institute educational materials for project requirements and structure.
- Stack Overflow and Django community examples for general debugging.
- All project code, structure, and templates written by the student (Thomas Fitzgerald) for Milestone Project 3.
