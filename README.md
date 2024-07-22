# Chatbot

This project implements a chatbot for a wine-selling business using Flask. The chatbot answers questions based on a pre-defined corpus of question-answer pairs stored in a JSON file. If the user asks something outside the scope of the corpus, the chatbot directs them to contact the business directly.

## Features

- Minimalistic and interactive UI.
- Answers questions based on a given corpus.
- Directs users to contact the business for out-of-corpus questions.
- Maintains conversation context.

## Technologies Used

- Flask (Python web framework)
- HTML, CSS, JavaScript (Frontend)
- OpenAI API (For handling responses, if needed)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/wine-chatbot.git
    cd chatbot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your-openai-api-key
    ```

5. Run the application:
    ```bash
    python app.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000/` to access the chatbot.

## File Structure
chatbot/
├── app.py
├── sample_question_answers.json
├── templates/
│ └── index.html
├── static/
│ └── styles.css
├── .env
├── requirements.txt
└── README.md

# Output
1. Correct input -
   ![image](https://github.com/user-attachments/assets/a0e05d44-a2ce-414f-b49e-ab06a6b82771)
2. Incorrect input -
   ![image](https://github.com/user-attachments/assets/cb0edef0-636c-418f-a0c8-72da1f2656d6)


