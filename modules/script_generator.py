import random

def generate_script(topic):
    hooks = [
        f"What if {topic} changes your life forever?",
        f"In the next 10 years, {topic} will shock the world.",
        f"You won’t believe what’s happening with {topic}.",
        f"This is the truth about {topic} no one talks about."
    ]

    intros = [
        f"{topic} is growing faster than ever before.",
        f"The world is shifting because of {topic}.",
        f"Experts believe {topic} will dominate the future.",
        f"Technology around {topic} is evolving rapidly."
    ]

    body_points = [
        f"First, {topic} is transforming industries worldwide.",
        f"Second, it is replacing traditional systems.",
        f"Third, it creates new opportunities while removing old ones.",
        f"It also increases efficiency and reduces human effort."
    ]

    ending = [
        f"So the big question is — are you ready for {topic}?",
        f"The future belongs to those who understand {topic}.",
        f"{topic} is not coming… it’s already here.",
        f"Prepare yourself before it's too late."
    ]

    script = f"""
{random.choice(hooks)}

{random.choice(intros)}

{random.choice(body_points)}
{random.choice(body_points)}

{random.choice(ending)}

Follow for more future insights.
"""

    return script.strip()