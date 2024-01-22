import os
import json
import subprocess
import concurrent.futures

# Function to run flutter create command
def run_flutter_create(category_name, path):
    project_name = path["project-name"]
    description = path["description"]

    # Create the 'projects' folder if it doesn't exist
    projects_folder = os.path.join(os.getcwd(), "projects")
    os.makedirs(projects_folder, exist_ok=True)

    # Create the project folder inside the 'projects' folder
    project_folder = os.path.join(projects_folder, category_name, project_name)
    os.makedirs(project_folder, exist_ok=True)
    os.chdir(project_folder)

    # Run the flutter create command in the current directory
    command = f'flutter create . --org=com.menuspk --project-name={project_name} --platforms=android --description="{description}"'
    subprocess.run(command, shell=True, check=True)

    # Print a success message
    print(f"Created project '{project_name}' in folder 'projects/{category_name}'")

    # Change back to the original working directory
    os.chdir(current_dir)

# Open the data file
with open("data.json", "r") as f:
    data = json.load(f)

# Get the current working directory
current_dir = os.getcwd()

# Create a list to store the futures
futures = []

# Iterate through each category in the data
with concurrent.futures.ThreadPoolExecutor() as executor:
    for category in data:
        category_name = category["category"]

        # Submit each category's projects as a separate thread
        futures.extend(executor.submit(run_flutter_create, category_name, path) for path in category["paths"])

# Wait for all threads to complete
concurrent.futures.wait(futures)

print("Done!")
