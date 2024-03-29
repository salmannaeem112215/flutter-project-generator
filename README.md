# Flutter Project Generator

## Introduction

The Flutter Project Generator is a tool that simplifies the creation of Flutter projects in different categories. It leverages concurrent threads for faster project creation and includes a batch file for easy execution. Projects are configured in a data-driven manner using the `data.json` file.

## Demo

[Watch the demo video](./demo/demo.webm)

(Click the link to watch the demo)

## Prerequisites

Before running the script, ensure the following:

1. You have Flutter installed on your system.
2. You are in the root directory of the project.
3. Open the `data.json` file to customize project categories and details.

## Usage

1. Double-click on the `run_project_generator.bat` file to run the project generator.
2. Wait for the script to execute.

The projects will be created inside the `projects` folder, organized by categories specified in the `data.json` file.

## Configuration

1. Open the `data.json` file to customize project categories and details.
2. Each category should have a name and a list of projects with their respective names and descriptions.

```json
[
  {
    "category": "mobile",
    "paths": [
      { "project-name": "app1", "description": "Mobile App 1" },
      { "project-name": "app2", "description": "Mobile App 2" }
    ]
  },
  {
    "category": "web",
    "paths": [
      { "project-name": "web1", "description": "Web App 1" },
      { "project-name": "web2", "description": "Web App 2" }
    ]
  }
]
```

# Automating the Deployment of 40 Mobile Apps with Flutter

## Video Series Overview

In this video series, we demonstrate how to automate the deployment of 40 mobile apps on the Play Store using Flutter. This automation process significantly reduces the time and effort required to publish each application individually.

## Step 1: Creating 40 Flutter Projects

The first step is to create 40 Flutter projects using a custom script. The Flutter Project Generator tool, showcased in the demo, leverages concurrent threads for faster project creation. This video demonstrates the project creation process, highlighting how the tool utilizes data-driven configuration from the `data.json` file.

_Note: The goal is to create a mobile app for each template from menuspk.com and publish it on the Play Store._

## Next Steps

### STEP 1: Creating 40 GitHub Repositories (Completed)

The GitHub repositories have been created for each Flutter project. This step ensures that each project has a dedicated repository for version control and collaboration.

### STEP 2: Automating Code Editing for All Repositories

The second step involves automating code editing tasks across all GitHub repositories. This automation enhances the consistency and efficiency of the codebase.

### STEP 3: Batch Commit for All Repositories

Batch commit functionality is applied to all repositories, streamlining the version control process. This ensures that changes are tracked and managed efficiently.

### STEP 4: Generating Executables for All Applications

The final step focuses on generating executables for all 40 mobile applications. This prepares the apps for deployment on the Play Store.

By the end of this series, you'll witness the deployment of 40 mobile apps on the Play Store in a fraction of the time it would take manually. Stay tuned for upcoming videos where we dive into each step of the automation process.
