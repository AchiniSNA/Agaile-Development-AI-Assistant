import streamlit as st
import google.generativeai as genai
import requests

# Define the Google Custom Search API method to search online for relevant results
def search_online(query):
    api_key = 'AIzaSyC2_tqhkuW6vN-cXkN5L9-USLzS4Jcunwo'  # Replace with your Google API key
    cse_id = 'e6b0abebf92054298'  # Replace with your Custom Search Engine ID
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"

    response = requests.get(url)

    # Check for request errors
    if response.status_code != 200:
        st.error(f"Error: Unable to fetch search results. Status code {response.status_code}")
        return []

    search_results = response.json()

    # Extract titles and snippets of relevant search results
    online_references = []
    if 'items' in search_results:
        for result in search_results['items']:
            title = result.get('title')
            snippet = result.get('snippet')
            link = result.get('link')
            online_references.append(f"**Title**: {title}\n**Snippet**: {snippet}\n[Read more]({link})")
    else:
        st.warning("No relevant online references found.")

    return online_references

# Function to generate prompt with online references
def make_rag_prompt(query):
    online_references = search_online(query)
    online_references_str = "\n".join(online_references) if online_references else "No online references found."

    prompt = (
        f"You are an intelligent assistant that answers questions using only online references. "
        f"Please answer the question by using information from online resources. "
        f"Make sure your answer is accurate, well-rounded, and integrates the information effectively.\n\n"
        f"**QUESTION:** '{query}'\n"
        f"**ONLINE REFERENCES:**\n{online_references_str}\n\n"
        f"**ANSWER:**"
    )
    return prompt, online_references

# Function to generate response from AI model
def generate_response(user_prompt):
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(user_prompt)
    return answer.text

# Function to create answer from prompt
def generate_answer(query):
    prompt, online_references = make_rag_prompt(query)
    answer = generate_response(prompt)
    return answer, online_references

# Streamlit App
st.set_page_config(page_title="Agile Development AI Assistant", page_icon="💁", layout="centered")

# Header Section with Description
st.title("Agile Development AI Assistant 💁")
st.markdown(
    """
    ### Get quick, reliable insights into Agile development practices!
    This AI assistant can answer your questions by referencing reliable, up-to-date online resources. 
    Simply enter your query below and let the assistant help guide you.
    """
)
st.write("---")

# Input Section with Sidebar Explanation
st.sidebar.header("About This Assistant")
st.sidebar.write(
    """
    This assistant uses Google Custom Search and a generative AI model to provide answers to Agile development questions.
    - **How it works**: The assistant finds relevant online resources for your query, then uses them to craft an informed answer.
    """
)

# Query Input Box
st.subheader("Ask an Agile Development Question")
query = st.text_input("💬 Enter your query:")

# Button to submit query and load answer
if query:
    # Create a placeholder for the loading message
    loading_placeholder = st.empty()
    loading_placeholder.write("🔍 Searching for relevant information...")
    
    # Generate answer with spinner
    with st.spinner("Generating response..."):
        answer, online_references = generate_answer(query)
    
    # Remove the loading message after generating the answer
    loading_placeholder.empty()
    
    # Displaying answer in a formatted container
    st.success("Here’s the answer to your question:")
    st.subheader("Answer:")
    st.write(answer)
    
    # Display 2-3 references after the answer
    st.write("---")
    st.subheader("References:")
    for reference in online_references[:3]:  # Show only the first 2-3 references
        st.write(reference)

else:
    st.info("Type a question in the box above to get started.")

# Footer
st.write("---")
st.markdown("Powered by Google Gemini AI and Streamlit")
