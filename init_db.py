import sqlite3

conn = sqlite3.connect('scholarships.db')
c = conn.cursor()

# =====================
# Create main tables
# =====================
c.execute('''
    CREATE TABLE IF NOT EXISTS scholarships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        provider TEXT,
        eligibility TEXT,
        amount TEXT,
        deadline TEXT,
        link TEXT,
        approved INTEGER DEFAULT 0
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS internships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        provider TEXT,
        eligibility TEXT,
        amount TEXT,
        deadline TEXT,
        link TEXT,
        approved INTEGER DEFAULT 0
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL
    )
''')

# =====================
# Create archive tables
# =====================
c.execute('''
    CREATE TABLE IF NOT EXISTS scholarships_archive (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        provider TEXT,
        eligibility TEXT,
        amount TEXT,
        deadline TEXT,
        link TEXT,
        approved INTEGER DEFAULT 0
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS internships_archive (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        provider TEXT,
        eligibility TEXT,
        amount TEXT,
        deadline TEXT,
        link TEXT,
        approved INTEGER DEFAULT 0
    )
''')

# =====================
# Insert sample data (only if empty)
# =====================
sample_scholarships = [
    ("AI Talent Scholarship", "OpenAI", "Students pursuing AI degrees", "$2000", "2025-08-31", "https://openscholarship.ai", 1),
    ("Women in Tech", "Google", "Female STEM undergrads", "$3000", "2025-09-15", "https://google.com/scholarships", 1),
]

sample_internships = [
    ("AI Research Intern", "Microsoft", "CS/AI students", "₹25,000/month", "2025-08-20", "https://careers.microsoft.com/intern", 1),
    ("ML Intern", "Amazon", "B.Tech students with ML knowledge", "₹30,000/month", "2025-08-28", "https://amazon.jobs/intern", 1),
]

# Insert scholarships
c.execute("SELECT COUNT(*) FROM scholarships")
if c.fetchone()[0] == 0:
    c.executemany('''
        INSERT INTO scholarships (name, provider, eligibility, amount, deadline, link, approved)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_scholarships)

# Insert internships
c.execute("SELECT COUNT(*) FROM internships")
if c.fetchone()[0] == 0:
    c.executemany('''
        INSERT INTO internships (name, provider, eligibility, amount, deadline, link, approved)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_internships)

conn.commit()
conn.close()

print("✅ Database initialized and tables created.")
