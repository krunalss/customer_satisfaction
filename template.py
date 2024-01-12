import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

project_name = "customer_satisfaction"
list_of_files=[".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    # f"src/{project_name}/components/__init__.py",
    # f"src/{project_name}/utils/__init__.py",
    # f"src/{project_name}/config/__init__.py",
    # f"src/{project_name}/pipeline/__init__.py",
    # f"src/{project_name}/constants/__init__.py",
    # f"src/{project_name}/steps/__init__.py",
    "data/__init__.py",
    "pipelines/.gitkeep",
    "run_pipeline.py",
    "saved_models/.getkeep",
    "steps/__init__.py",
    "steps/ingest_data.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb",
    "test.py"    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the filename:{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} already exits")