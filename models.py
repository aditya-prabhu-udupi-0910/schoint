import sqlite3

# Optional: sample scholarships for initial population
sample_scholarships = [
    (
        "Tech Scholars Grant",
        "Scholarship for students interested in AI and Robotics.",
        "Open to all B.Tech students in AI/Robotics",
        "₹40,000",
        "2025-08-31",
        "Technology",
        "https://example.com/tech-grant",
        "Example Org"
    ),
    (
        "STEM Future Fund",
        "Financial aid for underprivileged STEM students.",
        "STEM UG students with 75%+ score",
        "₹60,000",
        "2025-09-15",
        "STEM",
        "https://example.com/stem-future",
        "Govt of India"
    )
]

# Optional: sample internships
sample_internships = [
    (
        "AI Research Intern",
        "OpenAI",
        "Work on cutting-edge AI research projects.",
        "Final-year UG/PG students in AI/ML",
        "Remote",
        "₹20,000/month",
        "3 months",
        "2025-08-20",
        "https://openai.com/careers/ai-research-intern",
        "OpenAI"
    ),
    (
        "Web Development Intern",
        "TechSpark Solutions",
        "Develop and maintain front-end websites.",
        "UG students with HTML/CSS/JS knowledge",
        "Bengaluru",
        "₹10,000/month",
        "2 months",
        "2025-09-01",
        "https://techspark.internships.com/web-dev",
        "TechSpark"
    )
]

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Scholarships table
    c.execute('''
        CREATE TABLE IF NOT EXISTS scholarships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            eligibility TEXT,
            amount TEXT,
            deadline TEXT,
            category TEXT,
            link TEXT,
            source TEXT,
            approved INTEGER DEFAULT 1
        )
    ''')

    # Internships table (updated with all 10 fields)
    c.execute('''
        CREATE TABLE IF NOT EXISTS internships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT,
            description TEXT,
            eligibility TEXT,
            location TEXT,
            stipend TEXT,
            duration TEXT,
            deadline TEXT,
            link TEXT,
            source TEXT,
            approved INTEGER DEFAULT 1
        )
    ''')

    # Subscribers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()


def insert_sample_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Scholarships
    c.execute("SELECT COUNT(*) FROM scholarships")
    if c.fetchone()[0] == 0:
        for s in sample_scholarships:
            c.execute('''
                INSERT INTO scholarships (
                    title, description, eligibility, amount, deadline, category, link, source
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', s)

    # Internships
    c.execute("SELECT COUNT(*) FROM internships")
    if c.fetchone()[0] == 0:
        for i in sample_internships:
            c.execute('''
                INSERT INTO internships (
                    title, company, description, eligibility, location, stipend, duration, deadline, link, source
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', i)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    insert_sample_data()
    print("✅ Database initialized with scholarships, internships, and subscribers.")
