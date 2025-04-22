import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="ReverseAI - Decode LinkedIn's Wildest Posts",
    page_icon="🔄",
    layout="wide"
)


api_key = os.getenv("GEMINI_API") 

# Initialize Gemini with predefined API key
@st.cache_resource
def init_gemini():
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def generate_prompt(text, content_type="LinkedIn Post"):
    try:
        model = init_gemini()
        genai.configure(api_key=api_key)
        # Updated prompt for unhinged LinkedIn posts analysis
        prompt = f"""
        You are ReverseAI, an AI system specialized in decoding unhinged and over-the-top LinkedIn posts.
        
        Analysis Task:
        - Content Type: {content_type}
        - Unhinged LinkedIn Post to Analyze:
        ---
        {text}
        ---
        
        Instructions:
        1. Analyze the writing style, dramatic tone, and excessive elements
        2. Identify patterns typical of viral or attention-seeking LinkedIn content
        3. Reconstruct the likely prompt that would generate this type of content
        4. Add humor to your analysis when appropriate
        5. Make response short other than the prompt
        
        Format your response as:
        📝 PROMPT:
        [Write the vague prompt that would generate this type of unhinged LinkedIn post]
        
        💡 UNHINGED SCORE: [includes only numbers 1-10, where 1 is lowest and 10 is maximum LinkedIn cringe]
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app
def main():
    # Custom CSS for ReverseAI branding
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
        }
        .main-header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #4158D0, #C850C0);
            color: white;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .info-card {
            background: linear-gradient(135deg, #4158D0, #C850C0);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .stats-card {
            background: #f1f3f5;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            margin: 10px 0;
        }
        .result-box {
            background: linear-gradient(135deg, #4158D0, #C850C0);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
            border-left: 5px solid #4158D0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        .cta-button {
            background: #4158D0;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            margin: 10px 0;
        }
        .footer {
            text-align: center;
            color: #666;
            padding: 20px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header with updated tagline
    st.markdown("<div class='main-header'><h1>🔄 ReverseAI</h1><p>Decode Those Unhinged LinkedIn Posts</p></div>", unsafe_allow_html=True)
    
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Content type selection - focusing on LinkedIn posts
        content_type = st.selectbox(
            "LinkedIn Post Category",
            options=["Humble Brag", "Career Advice", "Hustle Culture", "Corporate Inspiration", "Failure-to-Success Story", "Generic LinkedIn Post"],
            help="Select the type of LinkedIn content you're analyzing"
        )
        
        # Text input area with updated placeholder
        text_input = st.text_area(
            "Paste the unhinged LinkedIn post",
            height=200,
            placeholder="Paste that wild LinkedIn post here..."
        )
    
    with col2:
        st.markdown("""
        <div class='info-card'>
        <h3>About</h3>
        <p>Ever scrolled LinkedIn and wondered "who writes this stuff?" </p>
        <p>Now you can find out exactly what prompt would create those
        unhinged LinkedIn posts flooding your feed.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Analyze button with updated text
    if st.button("🔄 Decode", type="primary"):
        if text_input:
            with st.spinner('Analyzing unhinged energy...'):
                result = generate_prompt(text_input, content_type)
            
            st.markdown("---")
            st.subheader("Prompt Behind the Post")
            st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
            
            # Share on social button
            col1, col2 = st.columns(2)
            with col1:
                st.button("Clear Result", key="copy_result")
        else:
            st.error("Please paste a LinkedIn post to analyze its unhinged energy!")

    st.markdown(
    f'<p style="color: gray; font-size: 0.8em;"> Made with ❤️ by <a href="https://github.com/Shaheer04" target="_blank">Shaheer Jamal</a></p>',
    unsafe_allow_html=True,
    )
    # Footer with updated text
    st.markdown("<div class='footer'>ReverseAI | Decoding LinkedIn's Most Unhinged Content Since ChatGPT </div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()