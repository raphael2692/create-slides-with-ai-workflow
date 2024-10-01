import streamlit as st
import subprocess
import time
from pathlib import Path
import os

from utils import generate_marp_deck

# Function to create markdown from topic description and generate PDF using marp-cli
def generate_pdf_from_marp(topic_description:st, additional_guidelines:str):
    # Define a secure path for the markdown and output files in the current working directory
    current_dir = Path(os.getcwd())
    markdown_file = current_dir / "slide-deck.md"
    output_file = current_dir / "output.pdf"
    
    my_bar = st.progress(10, text="Generating deck...")
    content = generate_marp_deck(topic_description, additional_guidelines)

    # Write the topic description into the Markdown file
    my_bar.progress(40, "Saving Deck...")
    with open(markdown_file, encoding="utf-8", mode="w") as f:
        f.write(content)
    
    # Command to invoke marp-cli using npx to generate PDF from the markdown file
    my_bar.progress(50, "Converting Deck...")
    command = f'npx @marp-team/marp-cli@latest "{markdown_file}" -o "{output_file}"'

    # Run the command using shell=True to ensure Windows executes it correctly
    process = subprocess.run(command, capture_output=True, text=True, shell=True, env=os.environ)
    
    if process.returncode != 0:
        # If there was an error in generating the PDF file, return an error message
        st.error(f"Error generating PDF: {process.stderr}")
        return None

    my_bar.empty()
    return output_file



# Streamlit app
st.title("Slide Deck Generator")

# Text input for topic description
topic_description = st.text_area("Enter the topic description:", height=200)

# Text input for additional guidelines
additional_guidelines = st.text_area("Enter additional guidelines (e.g. tone, max number of slides, etc. ):", height=100)


# Generate button
if st.button("Generate Slide Deck"):
    # Ensure a topic description is provided
    if topic_description:
        # Generate the PDF using Marp CLI
        file_path = generate_pdf_from_marp(topic_description, additional_guidelines)
        
        if file_path and Path(file_path).is_file():
            # Provide a download button for the generated PDF file
            with open(file_path, "rb") as f:
                st.download_button(
                    label="Download Generated Slide Deck",
                    data=f,
                    file_name="output.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("Failed to generate the slide deck.")
    else:
        st.warning("Please provide a topic description.")
