import os

def process_documents(pdf_paths, persona, job):
    extracted_sections = []
    subsection_analysis = []

    for path in pdf_paths:
        document = os.path.basename(path)

        
        extracted_sections.append({
            "document": document,
            "section_title": "Introduction",
            "importance_rank": 1,
            "page_number": 1
        })

        subsection_analysis.append({
            "document": document,
            "refined_text": "This section discusses ...",
            "page_number": 1
        })

    return extracted_sections, subsection_analysis
