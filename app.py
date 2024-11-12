import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re
import urllib.parse

def extract_video_id(url):
    """Extract YouTube video ID from URL"""
    # Handle different URL formats
    query = urllib.parse.urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return urllib.parse.parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None

def get_transcript(video_id):
    """Get transcript of YouTube video"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        return transcript
    except Exception as e:
        return f"Error getting transcript: {str(e)}"

def summarize_text(text, max_length=150, min_length=50):
    """Summarize text using transformers"""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Split text into chunks if it's too long
    max_chunk_size = 1024
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    
    return ' '.join(summaries)

def extract_key_points(summary):
    """Extract key points from summary"""
    # Split into sentences and filter out short ones
    sentences = re.split(r'[.!?]+', summary)
    key_points = [s.strip() for s in sentences if len(s.strip()) > 20]
    return key_points

# Streamlit UI
st.title("YouTube Video Summarizer")
st.write("Enter a YouTube video URL to get a summary and key points!")

# Input for YouTube URL
url = st.text_input("YouTube Video URL")

if url:
    if st.button("Summarize"):
        try:
            with st.spinner("Processing video..."):
                # Extract video ID
                video_id = extract_video_id(url)
                if not video_id:
                    st.error("Invalid YouTube URL")
                else:
                    # Get transcript
                    transcript = get_transcript(video_id)
                    if transcript.startswith("Error"):
                        st.error(transcript)
                    else:
                        # Generate summary
                        st.subheader("Summary")
                        summary = summarize_text(transcript)
                        st.write(summary)
                        
                        # Extract and display key points
                        st.subheader("Key Points")
                        key_points = extract_key_points(summary)
                        for i, point in enumerate(key_points, 1):
                            st.write(f"{i}. {point}")
                        
                        # Display video preview
                        st.subheader("Video Preview")
                        st.video(url)
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Add some usage instructions
with st.expander("How to use"):
    st.write("""
    1. Paste a YouTube video URL in the input field above
    2. Click the 'Summarize' button
    3. Wait for the AI to process the video
    4. View the summary and key points
    
    Note: The video must have closed captions/subtitles available.
    """)