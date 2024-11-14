# Agile Development AI Assistant

This project is an AI-powered assistant designed to provide insights and guidance on Agile development practices, specifically for Scrum-based projects. The assistant leverages Google Custom Search to find relevant online resources and a generative AI model to answer questions based on Scrum process activities.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)

## Project Overview

This project acts as a software process assistant focused on the Scrum methodology. It allows users to enter Scrum-related questions, which the assistant answers by searching the web for relevant resources and generating a response based on these findings. Key Scrum activities such as Sprint Planning, Daily Standup, and Sprint Retrospective are supported.

## Features

- **Question Input Box**: Users can input questions related to Scrum and Agile practices.
- **Online Search Integration**: Retrieves relevant online resources to inform responses.
- **Generative AI Responses**: Provides well-rounded answers based on web search results.
- **Sidebar Information**: Shows chat history and tips on using the assistant effectively.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **Google Custom Search API**: To retrieve relevant search results.
- **Generative AI Model**: Used to generate responses based on online references.

## Live Demo

Check out the deployed app here: [Agile Development AI Assistant on Streamlit]([(https://share.streamlit.io/achinisna/scrum-mentor1/main/app.py)])
## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/agile-development-ai-assistant.git
   cd agile-development-ai-assistant

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Set up your Google Custom Search API by obtaining an API key and a Custom Search Engine (CSE) ID. See Google's documentation for guidance.

4. Create a .env file in the project root and add your API credentials as shown in the Environment Variables section below.

## Environment Variables
Create a .env file with the following environment variables:
```bash
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
```
Replace your_google_api_key and your_custom_search_engine_id with the actual values from your Google Custom Search setup.

## Usage
Run the application:

```bash
streamlit run app.py
```
Open the link provided in your terminal to view the app in your browser.

Enter questions related to Scrum practices in the input box, and the assistant will generate answers based on relevant online resources.


