import os
import json
import subprocess
import concurrent.futures
import time

# Function to run flutter create command for a specific project
def run_flutter_create(category_name, path):
    project_name = path["project-name"]
    description = path["description"]

    # Get the current working directory
    current_dir = os.getcwd()

    # Create the 'projects' folder if it doesn't exist
    projects_folder = os.path.join(current_dir, "projects")
    os.makedirs(projects_folder, exist_ok=True)

    # Create the project folder inside the 'projects' folder
    project_folder = os.path.join(projects_folder, category_name, project_name)
    os.makedirs(project_folder, exist_ok=True)
    
    # Change to the project folder
    os.chdir(project_folder)

    # Run the flutter create command in the current directory
    command = f'flutter create . --org=com.menuspk --project-name={project_name} --platforms=android --description="{description}"'
    subprocess.run(command, shell=True, check=True)

    # Print a success message
    print(f"Created project '{project_name}' in folder 'projects/{category_name}'")

# Open the data file
with open("data.json", "r") as f:
    data = json.load(f)

# Create a list to store the futures
futures = []

# Iterate through each category in the data
with concurrent.futures.ThreadPoolExecutor() as category_executor:
    for category in data:
        category_name = category["category"]

        # Submit each category as a separate thread
        category_futures = [category_executor.submit(run_flutter_create, category_name, path) for path in category["paths"]]
        futures.extend(category_futures)
        # Sleep for 100 milliseconds before starting the next category
        time.sleep(0.1)

# Wait for all futures to complete
concurrent.futures.wait(futures)

print("Done!")
