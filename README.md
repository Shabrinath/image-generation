# Image Generation with AWS Bedrock

This project demonstrates how to generate images using the AWS Bedrock service with the Stability AI Stable Diffusion model. The script provides a simple interface using Streamlit for generating images based on user-provided prompts.

## Features
- Generates images based on text prompts using AWS Bedrock's Stable Diffusion model.
- User-friendly web interface built with Streamlit.

## Requirements

To run this script, you need the following:

- Python 3.7 or higher
- AWS account with Bedrock access
- An IAM user with permissions to use Bedrock services
- Necessary Python libraries

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install the required packages:
   ```
   pip install -r requirements.txt

4. Set up AWS credentials:
   ```
   aws configure
   You will be prompted to enter your AWS Access Key, Secret Key, region, and output format.

## Usage

1. Run the Streamlit application:
```
streamlit run app.py

2. Access the application by navigating to:
```
http://localhost:8501
Enter a prompt in the text input field, click "Generate Image," and the generated image will be displayed on the page.

## Example Prompts
"Sri lanka tea plantation"
"A beautiful sunset over the mountains"
"A futuristic city skyline"

## Notes
Ensure you have adequate permissions set up in your AWS account for accessing Bedrock and generating images.
This script is designed for educational purposes; consider optimizing it for production use.
