#!/usr/bin/env python3
import os

def load_organized_questions(filepath):
    # Dictionary format: { "Section Name": ["Question 1", "Question 2"] }
    study_data = {}
    current_section = "General"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Identify a Section (e.g., # Remote Workflow & Communication)
            if line.startswith('#'):
                current_section = line.replace('#', '').strip()
            # Identify a question (lines starting with - or numbers)
                if current_section not in study_data:
                    study_data[current_section] = []
            # Identify Question (e.g., - How do you ensure seamless communication with the in-office clinical team while working remotely?)    
            elif line.startswith(('-', '*')):
                question_text = line.lstrip('-* ').strip()
                study_data[current_section].append(question_text)
                
    return study_data

def run_exam(study_data):
    for section, questions in study_data.items():
        total_in_sec = len(questions)
    
    for index, q_text in enumerate(questions):
            # Visual feedback
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- STUDY MODE: VIRAL PRODUCTS ---")
            print(f"CURRENT SECTION: {section.upper()}")
            print(f"Progress: Question {index + 1} of {total_in_sec}")
            print("-" * 30)
            
            print(f"\nPROMPT: {q_text}")
            
            input("\n[Press Enter for next question]")

    print("\nGreat job! You've finished all sections.")

if __name__ == "__main__":
    # This finds the directory where your script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # This joins that directory with your filename
    file_path = os.path.join(script_dir, 'study_material.md')
    
    data = load_organized_questions(file_path)
    run_exam(data)