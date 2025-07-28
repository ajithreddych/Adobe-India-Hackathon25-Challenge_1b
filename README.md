# 🧠 Persona-Driven Document Intelligence

## 🔍 Overview

This project is built for **Round 1B of the Adobe India Hackathon 2025** under the theme:  
**“Connect What Matters — For the User Who Matters”**

The goal is to build a system that acts as an **intelligent document analyst**, capable of:
- Understanding a given **persona** and their **job-to-be-done**
- Extracting the most relevant content from a set of related **PDF documents**
- Producing a structured JSON output that highlights the important sections and insights

---

## 📘 Problem Statement

You are required to:
- Analyze **3–10 PDF documents**
- Understand a **persona** (e.g., researcher, student, analyst)
- Understand the **task/job** that the persona needs to perform
- Extract and rank document sections that are relevant to the task
- Provide a refined text analysis per section

---

## 🧾 Input Specification

1. **PDF Collection**: 3–10 documents (textbooks, research papers, reports, etc.)
2. **Persona Definition**: A role with expertise and specific focus areas
3. **Job-to-Be-Done**: A concrete task the persona wants to accomplish

---

## 📤 Output Specification

The system outputs a JSON in the following format:

### 1. Metadata
- `documents`: List of PDF file names
- `persona`: Persona description
- `job`: Job to be done
- `processed_at`: Timestamp of execution

### 2. Extracted Sections
- `document`: File name
- `page_number`: Page where the section is found
- `section_title`: Heading/Title of the section
- `importance_rank`: Relevance score based on persona-task alignment

### 3. Subsection Analysis
- `document`: File name
- `page_number`: Page where the subsection appears
- `refined_text`: Extracted or summarized content

---

## 🧪 Sample Use Cases

### 📚 Academic Research  
- **Persona**: PhD in Computational Biology  
- **Job**: Write literature review on GNNs for Drug Discovery  
- **Docs**: Research papers  

### 📊 Business Analysis  
- **Persona**: Investment Analyst  
- **Job**: Compare R&D and revenue across tech companies  
- **Docs**: Annual reports  

### 🎓 Educational Prep  
- **Persona**: Undergraduate Chemistry Student  
- **Job**: Prepare for exam on reaction kinetics  
- **Docs**: Textbook chapters  

---

## 🧰 Project Structure

