import streamlit as st
import google.generativeai as genai

# Configure the Generative AI API key
genai.configure(api_key="AIzaSyBEblD4B-gLYkR3fSK6i2AFefT_WMo5JsQ")

# Set page config for better appearance
st.set_page_config(page_title="Image Caption Generator", layout="wide")

# Apply custom CSS for sleek, modern styling with a black background
st.markdown(
    """
    <style>
    /* General background styling */
    body {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
    }
    /* Title and header styling */
    .title {
        text-align: center;
        color: #FFD700;
        font-size: 50px;
        font-weight: 800;
        margin-top: 50px;
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
    }
    .subheader {
        text-align: center;
        color: #FFFFFF;
        font-size: 22px;
        margin-top: 10px;
        margin-bottom: 40px;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #000000;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.2);
    }
    /* File uploader styling */
    div[data-testid="stFileUploader"] {
        background-color: rgba(255, 255, 255, 0.1);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 25px;
        width: 100%;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
        transition: 0.3s ease;
    }
    div[data-testid="stFileUploader"]:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.3);
    }
    /* Spinner styling */
    .spinner {
        color: #FFD700 !important;
    }
    /* Button styling */
    button {
        background-color: #FFD700 !important;
        color: #000000 !important;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        padding: 12px 30px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
    }
    button:hover {
        background-color: #FFC300;
        transform: translateY(-2px);
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.4);
    }
    /* Image preview styling */
    img {
        border: 5px solid #FFD700;
        border-radius: 20px;
        margin-top: 20px;
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.05);
    }
    /* Caption text styling */
    .caption {
        text-align: center;
        font-size: 26px;
        margin-top: 20px;
        color: #000000;  /* Changed to white for better visibility */
        font-weight: bold;
        font-style: italic;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);  /* Added shadow for better contrast */
    }
    /* Warning message styling */
    .warning {
        text-align: center;
        font-size: 18px;
        margin-top: 20px;
        color: #FF6347;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown('<div class="title">CaptiGen: Innovative AI for Dynamic Caption</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheader">Upload an image and let AI generate a creative caption for you!</div>',
    unsafe_allow_html=True,
)

# Create a sidebar for the file uploader and customization options
with st.sidebar:
    st.markdown('<h3 style="color: #FFD700;">Upload an Image</h3>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # Add customization options for tone and caption length
    tone = st.selectbox("Select Tone", ["Casual", "Formal", "Funny", "Inspirational"])
    caption_length = st.selectbox("Select Caption Length", ["Short", "Medium", "Long"])

# If the user uploads an image
if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image in the main area
    st.image("temp_image.jpg", caption="Uploaded Image", use_container_width=True)

    # Upload the image to Google Generative AI
    sample_file = genai.upload_file(path="temp_image.jpg", display_name="Uploaded Image")

    # Load the model
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

    # Generate the caption based on selected tone and length
    with st.spinner("Generating caption..."):
        response = model.generate_content(
            [sample_file, f"Generate one {tone} caption with a {caption_length} length."]
        )
    
    # Display the generated caption with styling
    st.markdown('<div class="caption">Caption Generated!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="caption">"{response.text}"</div>', unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="warning">Please upload an image to get started.</div>',
        unsafe_allow_html=True,
    )
