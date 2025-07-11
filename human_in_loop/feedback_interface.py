def human_feedback_loop(content):
    print("----- HUMAN FEEDBACK REQUIRED -----")
    print("AI Drafted Chapter:\n", content[:500], "...\n")
    revised = input("Enter your revised text (or press Enter to keep as is):\n")
    return revised if revised.strip() else content