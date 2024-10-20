import base64
import boto3
import json
import os
import streamlit as st

# AWS credentials (replace with your actual credentials)
aws_access_key_id = "your-access-key-id"
aws_secret_access_key = "your-secret-access-key"
region_name = "us-east-1"

# Create a Bedrock Runtime client with explicit credentials
client = boto3.client(
    "bedrock-runtime",
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Function to generate image from AWS Bedrock
def generate_image(prompt, steps=50):
    model_id = "stability.stable-diffusion-xl-v1"

    # Format the request payload using the model's native structure
    native_request = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 10,
        "steps": steps,
        "seed": 0,
        "width": 1024,
        "height": 1024,
        "samples": 1
    }

    # Convert the native request to JSON
    request = json.dumps(native_request)

    # Invoke the model with the request
    response = client.invoke_model(modelId=model_id, body=request)

    # Decode the response body
    model_response = json.loads(response["body"].read())

    # Extract the image data
    base64_image_data = model_response["artifacts"][0]["base64"]

    # Decode and return image data
    return base64.b64decode(base64_image_data)

# Streamlit app UI
st.title("AWS Bedrock Image Generator with Stable Diffusion")

# Input for the image prompt
prompt = st.text_input("Enter image prompt", value="Sri lanka tea plantation")

# Button to trigger image generation
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            # Call the image generation function
            image_data = generate_image(prompt)

            # Save and display the image
            image_path = "generated_image.png"
            with open(image_path, "wb") as file:
                file.write(image_data)

            # Display image in Streamlit
            st.image(image_path)
            st.success("Image generated successfully!")

        except Exception as e:
            st.error(f"Error generating image: {str(e)}")

