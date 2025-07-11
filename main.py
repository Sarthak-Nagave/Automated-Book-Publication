import os
from dotenv import load_dotenv
from scraping.scraper import scrape_and_capture
from ai_writer.writer_agent import WriterAgent
from ai_writer.reviewer_agent import ReviewerAgent
from human_in_loop.feedback_interface import human_feedback_loop
from rl_module.reward_system import calculate_rl_reward
from chroma_db.version_store import save_version
from rl_module.rl_search import rl_based_search
import pyttsx3

# Insert your OpenAI API key
load_dotenv()  # Load the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

    # Step 1: Scrape
    print("Scraping content from:", url)
    chapter_content = scrape_and_capture(url)
    save_version("original", chapter_content)

    # Step 2: AI Writer
    writer = WriterAgent(OPENAI_API_KEY)
    spun_content = writer.spin_chapter(chapter_content)
    save_version("spun", spun_content)

    # Step 3: AI Reviewer
    reviewer = ReviewerAgent(OPENAI_API_KEY)
    reviewed_content = reviewer.review_chapter(spun_content)
    save_version("reviewed", reviewed_content)

    # Example search query
    search_query = "Dick canoe lagoon"
    all_versions = []
    for version in ["original", "spun", "reviewed", "final"]:
        try:
            with open(f"versions/{version}.txt", "r", encoding="utf-8") as f:
                all_versions.append(f.read())
        except FileNotFoundError:
            continue

    best_match = rl_based_search(all_versions, search_query)
    print("\n🔍 RL Search Best Match:\n")
    print(best_match[:300])

    # Step 4: Human Feedback
    final_content = human_feedback_loop(reviewed_content)
    save_version("final", final_content)

    # Step 5: RL Reward System
    reward = calculate_rl_reward(final_content)
    print(f"\n⭐ RL Reward Score: {reward}")

    # Step 6: Voice Playback
    print("\n🔊 Speaking Final Chapter...")
    speak_text(final_content[:500])

    # Final Output
    print("\n✅ Final Chapter Output:\n")
    print(final_content[:1500])

if __name__ == "__main__":
    main()
