"""
Configuration module for Project Metabolism
Ensures all required directories exist before execution
"""
import os
from pathlib import Path

# Create required directories
REQUIRED_DIRS = [
    'config',
    'data',
    'logs',
    'strategies',
    'executions',
    'backup'
]

def initialize_project_structure():
    """Create all required directories and verify write permissions"""
    for dir_name in REQUIRED_DIRS:
        Path(dir_name).mkdir(exist_ok=True)
        
    # Verify critical files exist
    required_files = [
        'config/firebase_credentials.json',
        '.env'
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Critical file missing: {file_path}")
    
    print("✓ Project structure initialized successfully")