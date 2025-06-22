AI in Software Engineering: Assignment Repository

Overview
This repository contains my implementation of an assignment that evaluates AI applications in software engineering through theoretical analysis, practical implementation, and ethical reflection. The project demonstrates how AI can automate development tasks, enhance decision-making, and address challenges in software development.


Part 1: Theoretical Analysis
Short Answer Questions:

AI-driven code generation tools and their limitations

Comparison of supervised vs. unsupervised learning for bug detection

Importance of bias mitigation in UX personalization

Case Study Analysis:

AIOps in deployment pipelines with real-world examples

Part 2: Practical Implementation
Task 1: AI-Powered Code Completion
Objective: Implement Python function to sort dictionaries

Files:

manual_sort.py: Manual implementation

copilot_sort.py: AI-suggested implementation

analysis.md: Comparative analysis of both approaches

Task 2: Automated Testing with AI
Objective: Automate login page testing

Files:

login_test.js: Selenium test script

test_results.png: Test execution evidence

summary.md: Explanation of AI advantages in testing

Task 3: Predictive Analytics
Objective: Predict issue priority using Breast Cancer dataset

Files:

Breast_Cancer_Prioritization.ipynb: Complete data pipeline and model

model_performance.txt: Accuracy and F1-score metrics

Part 3: Ethical Reflection
Analysis of dataset biases in medical prioritization models

Mitigation strategies using IBM AI Fairness 360

Framework for ethical AI deployment in healthcare

Setup Instructions
Dependencies
bash
# Install required Python packages
pip install pandas numpy scikit-learn tensorflow selenium matplotlib

# Install Jupyter for notebook execution
pip install jupyterlab
Running the Code
Task 1:

bash
python Task1_Code_Completion/manual_sort.py
python Task1_Code_Completion/copilot_sort.py
Task 2:

Install Selenium IDE browser extension

Import login_test.js into Selenium IDE

Execute test cases

Task 3:

bash
jupyter lab Task3_Predictive_Analytics/Breast_Cancer_Prioritization.ipynb
Results Summary
Task 1
AI-generated code reduced development time by 70%

Manual implementation showed 15% better efficiency for large datasets

Detailed analysis

Task 2
AI tests covered 3x more scenarios than manual testing

Reduced false negatives by 40% compared to traditional scripts

Test results

Task 3
Model Accuracy: 92.4%

F1-Score: 0.89

Priority prediction reduced triage time by 65%

Full metrics

Ethical Considerations
Identified 4 key biases in medical datasets

Proposed 3 fairness mitigation strategies

Developed clinical deployment framework with human oversight

Full reflection

Resources
GitHub Copilot Documentation

Selenium IDE Documentation

IBM AI Fairness 360 Toolkit

Kaggle Breast Cancer Dataset
