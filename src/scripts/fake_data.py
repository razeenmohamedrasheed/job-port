from faker import Faker
from dotenv import load_dotenv
import psycopg2
import random
import os

# Load environment variables
load_dotenv()

fake = Faker()

# Custom job titles
job_titles = [
    "Software Engineer", "Full Stack Developer", "Backend Engineer",
    "Frontend Engineer", "Data Scientist", "AI Engineer",
    "Machine Learning Engineer", "DevOps Engineer", "Cloud Architect",
    "Consultant", "Solutions Architect", "Site Reliability Engineer",
    "Database Administrator", "Mobile App Developer",
    "Generative AI Engineer", "Prompt Engineer", "RAG Pipeline Engineer",
    "LLM Engineer", "Product Engineer", "System Analyst"
]

# Skills pool
skill_pool = [
    "Python", "FastAPI", "Django", "Flask", "Node.js", "Express", "Java", "Spring Boot",
    "C#", ".NET", "Go", "Rust", "Ruby on Rails",
    "React", "Next.js", "Angular", "Vue.js", "HTML", "CSS", "JavaScript", "TypeScript",
    "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Cassandra", "Elasticsearch",
    "AWS", "GCP", "Azure", "Docker", "Kubernetes", "Terraform", "CI/CD", "Linux",
    "NumPy", "Pandas", "Scikit-learn", "TensorFlow", "PyTorch", "OpenCV",
    "LangChain", "LlamaIndex", "Transformers", "RAG", "Vector Databases",
    "Pinecone", "Weaviate", "Milvus", "FAISS", "Hugging Face",
    "Large Language Models", "LLM Fine-tuning", "Prompt Engineering", "RAG Pipelines",
    "OpenAI API", "Anthropic Claude", "Mistral AI", "LLaMA", "Gemini",
    "Agentic AI", "LangGraph", "Multi-Agent Systems", "Generative AI",
    "AI Orchestration", "MCP (Model Context Protocol)"
]

# Connect to DB
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME"),
)
cur = conn.cursor()

# Insert jobs
for _ in range(1000):
    job_name = random.choice(job_titles)
    experience_required = random.randint(1, 10)
    skills = random.sample(skill_pool, random.randint(3, 7))
    created_by = random.randint(5, 7)  # candidate_id in your users table

    # Create description dynamically
    skills_text = ", ".join(skills)
    description = (
        f"We are looking for a {job_name} in our firm "
        f"with {experience_required} years of experience in these skills: {skills_text}."
    )

    cur.execute(
        """
        INSERT INTO jobs (job_name, description, experience_required, skills, created_by)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (job_name, description, experience_required, skills, created_by)
    )

conn.commit()
cur.close()
conn.close()

print("Inserted 1000 structured tech jobs successfully!")
