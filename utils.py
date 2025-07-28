def process_documents(filenames, persona, job):
    # Fake output for demo — replace with real analysis logic
    return {
        "extracted_sections": [
            {
                "document": filenames[0],
                "section_title": "Executive Summary",
                "importance_rank": 1,
                "page_number": 1
            },
            {
                "document": filenames[1] if len(filenames) > 1 else filenames[0],
                "section_title": "Financial Highlights",
                "importance_rank": 2,
                "page_number": 3
            }
        ],
        "subsection_analysis": [
            {
                "document": filenames[0],
                "refined_text": "The company reported strong revenue growth and increased R&D spending.",
                "page_number": 1
            },
            {
                "document": filenames[1] if len(filenames) > 1 else filenames[0],
                "refined_text": "Significant investment was made in AI-driven product lines.",
                "page_number": 3
            }
        ]
    }
