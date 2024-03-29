import os
import json
import subprocess
import concurrent.futures
import time

# Function to run flutter create command for a specific project
def run_flutter_create(category_name, path):
    project_name = path["project-name"]
    description = path["description"]

    # Run the flutter create command in the current directory
    command = f'flutter create {project_name} --org=com.menuspk --project-name={project_name} --platforms=android --description="{description}"'
    subprocess.run(command, shell=True, check=True)

    # Print a success message
    print(f"Created project '{project_name}' in folder 'projects/{category_name}'")
# Open the data file
with open("data.json", "r") as f:
    data = json.load(f)

# Create a list to store the futures
futures = []
current_dir = os.getcwd()
# Iterate through each category in the data
with concurrent.futures.ThreadPoolExecutor() as category_executor:
    for category in data:
        category_name = category["category"]

        # Create a folder for the category
        category_folder = os.path.join(os.getcwd(), "projects", category_name)
        os.makedirs(category_folder, exist_ok=True)
        
        # Change to the category folder
        os.chdir(category_folder)

        # Submit each path within the category as a separate thread
        category_futures = [
            category_executor.submit(run_flutter_create, category_name, path) for path in category["paths"]
        ]
        
        # Wait for all subthreads within the category to complete
        concurrent.futures.wait(category_futures)

        # Move back to the original working directory
        os.chdir(current_dir)

        # Sleep for 100 milliseconds before starting the next category
        time.sleep(0.1)

print("Done!")
