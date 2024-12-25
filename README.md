# Personal Chatbot with Multi-Session Management

This project implements a chatbot interface that supports multi-session chat management using the LangChain framework and the Groq model. The system allows users to create, switch between, and manage multiple chat sessions seamlessly.

---

## Features

1. **Multi-Session Management**

   - Create new chat sessions dynamically.
   - Switch between existing chat sessions.
   - Retrieve and display chat histories for individual sessions.

2. **Model Integration**

   - Powered by the Groq `llama3-70b-8192` model.
   - Provides natural and context-aware conversational responses.

3. **Customizable Chat Histories**

   - Stores chat histories for each session using LangChain's `ChatMessageHistory`.
   - Maintains message types for both human and AI messages.

4. **Streamlit Frontend**

   - User-friendly interface built using Streamlit.
   - Displays chat messages dynamically with styled message containers.

---

## Requirements

### Python Libraries

- `streamlit`
- `langchain_core`
- `langchain_community`
- `langchain_groq`

### API Key

You need a valid Groq API key to use the `ChatGroq` model. Replace the placeholder API key in the code with your actual API key.

---

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your Groq API key to the `groq_api_key` variable in the code.

---

## Usage

1. Run the application:

   ```bash
   streamlit run chatbot_interface.py
   ```

2. Use the sidebar to:

   - Create new chat sessions.
   - Switch between existing chat sessions.

3. Interact with the chatbot in the main interface.

---

## Project Structure

- **`chatbot_interface.py`**: The main file containing the Streamlit frontend.
- **`chatbot_core.py`**: Contains core functionalities for session management and chat history.

---

## Code Overview

### Key Functions

1. **`create_new_session`**

   - Creates a new session with a unique session ID.

2. **`get_session_name`**

   - Retrieves the name of a session based on its first message.

3. **`generate_response`**

   - Generates AI responses using the Groq model and updates the chat history.

4. **`get_chat_history`**

   - Fetches the chat history for a specific session.

### Technologies Used

- **LangChain Framework**: For managing message histories and enabling model integration.
- **Groq Model**: For conversational AI capabilities.
- **Streamlit**: For creating an interactive and user-friendly frontend.

---

## Future Enhancements and Contribution

- Add session renaming capabilities for better session management.
- Support exporting and importing chat histories.
- Enable additional model configurations to enhance response accuracy.

- Welcome!!

---

## License

This project is unlicensed.

---



