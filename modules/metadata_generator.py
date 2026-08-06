def generate_metadata(topic):
    title = f"{topic} — What You Need To Know"
    description = (
        f"In this quick video, we explore {topic} and what it means for your future. "
        "Subscribe for fast insights into technology, business, and personal growth.\n\n"
        "Timestamps:\n"
        "0:00 Intro\n"
        "0:05 What is the trend\n"
        "0:20 Why it matters\n"
        "0:45 What you should do next\n"
    )
    tags = [
        topic.lower(),
        "ai", "future", "technology", "automation", "career advice", "business tips"
    ]
    return title, description, tags
