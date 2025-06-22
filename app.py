
import json
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.
    Args:
        text (str): The input text to analyze.
        
    Returns:
        str: A JSON string containing polarity, subjectivity, and assesment
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2), # Polarity ranges from -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2), # Subjectivity ranges from 0 (objective) to 1 (subjective)
        "assessment": "Positive" if sentiment.polarity > 0 else "Negative" if sentiment.polarity < 0 else "Neutral"
    }

    return json.dumps(result)

# Create the Gradio interface

demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(label="Enter text for sentiment analysis", placeholder="Type here..."),
    outputs=gr.Textbox(label="Sentiment Analysis Result", placeholder="Result will be displayed here..."), # Changed from gr.JSON to gr.Textbox
    title="Sentiment Analysis App",
    description="This app analyzes the sentiment of the input text and returns the polarity, subjectivity, and assessment.",
)

# Launch the interface and MCP Server
if __name__ == "__main__":
    demo.launch(mcp_server=True, share=True)  # Set share=True to allow public access
    # Note: mcp_server=True is used to enable the MCP server for the app.
    # You can remove share=True if you want to run it locally without public access.
    # Ensure you have the necessary packages installed:
    # pip install gradio textblob
    # Also, make sure to download the necessary NLTK corpora for TextBlob:
    # python -m textblob.download_corpora
    # This will ensure that TextBlob can perform sentiment analysis correctly.          