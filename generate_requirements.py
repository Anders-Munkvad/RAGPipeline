import os
import glob
import tempfile
import subprocess
import shutil

def generate_requirements(notebook_dir, output_requirements="requirements.txt"):
    # Create a temporary directory to store converted Python files
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Temporary directory created at {temp_dir}")
        
        # Find all .ipynb files in the provided notebook directory
        notebook_paths = glob.glob(os.path.join(notebook_dir, "*.ipynb"))
        if not notebook_paths:
            print("No notebook files found in the directory.")
            return
        
        # Convert each notebook to a Python script using nbconvert
        for nb in notebook_paths:
            print(f"Converting {nb} to Python script...")
            cmd = [
                "jupyter", "nbconvert", 
                "--to", "python", 
                nb, 
                "--output-dir", temp_dir
            ]
            subprocess.run(cmd, check=True)
        
        # Run pipreqs on the temporary directory to generate requirements.txt
        print("Running pipreqs to generate requirements.txt...")
        cmd_req = ["pipreqs", temp_dir, "--force"]
        subprocess.run(cmd_req, check=True)
        
        # The generated file should be in the temp_dir
        generated_req = os.path.join(temp_dir, "requirements.txt")
        if os.path.exists(generated_req):
            # Copy the generated requirements.txt to the desired output location
            shutil.copy(generated_req, output_requirements)
            print(f"Requirements file successfully generated at: {output_requirements}")
        else:
            print("Failed to generate requirements.txt.")

if __name__ == "__main__":
    # Change 'Code' to the directory where your notebooks reside
    notebook_directory = "Code"
    generate_requirements(notebook_directory)
