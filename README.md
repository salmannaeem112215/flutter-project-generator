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
