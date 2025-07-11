# 🚀 Automated Book Publication Workflow

A complete AI-powered pipeline to automate book chapter scraping, AI-driven rewriting, human-in-the-loop editing, and version management, with Reinforcement Learning (RL)-based optimization and voice playback support.

---

## 🔑 Key Features

| Capability                        | Status | Tools Used                             |
|------------------------------------|--------|----------------------------------------|
| Scraping & Screenshots            | ✅ Done | Playwright, BeautifulSoup              |
| AI Writing & Review               | ✅ Done | OpenAI GPT-4o API                      |
| Human-in-the-Loop Editing         | ✅ Done | Terminal-based feedback loop           |
| RL Reward System                  | ✅ Done | Custom scoring based on feedback       |
| Voice Playback                    | ✅ Done | pyttsx3 (Text-to-Speech)               |
| Agentic API                       | ✅ Done | FastAPI (for microservices)            |
| Version Control & Semantic Search | ✅ Done | ChromaDB-style local versioning        |
| RL-Based Search Algorithm         | ✅ Done | Custom RL reward-based search          |

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **Playwright** – Web scraping and screenshots
- **OpenAI GPT-4o API** – AI writer & reviewer
- **ChromaDB (Local file-based)** – Content versioning and search
- **Reinforcement Learning Concepts** – Scoring and search
- **pyttsx3** – Voice output for chapter narration
- **FastAPI** – Extendable agent-to-agent API

---

## 📂 Folder Structure

     book_publication_pipeline/
        ├── main.py # Main pipeline runner
        ├── scraping/
        │ └── scraper.py # Web scraping logic
        ├── ai_writer/
        │ ├── writer_agent.py # AI writer agent
        │ └── reviewer_agent.py # AI reviewer agent
        ├── human_in_loop/
        │ └── feedback_interface.py # Human feedback module
        ├── rl_module/
        │ ├── reward_system.py # RL reward scoring
        │ └── rl_search.py # RL-based search
        ├── chroma_db/
        │ └── version_store.py # Version saving & search
        ├── agentic_api/
        │ └── api_server.py # FastAPI microservice API
        └── versions/ # Stores all chapter versions

## ▶️ How to Run

### 1. Clone the repository
        -bash
         git clone https://github.com/Sarthak-Nagave/Automated-Book-Publication.git
         cd Automated-Book-Publication

### 2. Install dependencies
        -bash
         pip install -r requirements.txt

### 3. Add your OpenAI API key
        Edit main.py and insert your API key in the OPENAI_API_KEY variable.

### 4. Run the pipeline
        -bash
         python main.py

# EXAMPLE OUTPUT:
 
            Scraping content from: https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1

            🔍 RL Search Best Match:
            [Chapter snippet]

            ----- HUMAN FEEDBACK REQUIRED -----
            AI Drafted Chapter:
            [AI-generated draft]

            Enter your revised text (or press Enter to keep as is):
            [User input]

            ⭐ RL Reward Score: 1.0
            🔊 Speaking Final Chapter...

            ✅ Final Chapter Output:
            [Final chapter text]

### 🌟 Future Improvements
    -Advanced RL search algorithms
    -Deploy FastAPI as a microservice (e.g., Render, AWS)
    -Database-backed ChromaDB (PostgreSQL/MongoDB)
    -Continuous model improvement from user feedback

### 📜 License
    -This is an evaluation project only.
    -The developer retains full rights to the source code.
    -No commercial use by Soft-Nerve or other parties.





