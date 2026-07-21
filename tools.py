import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def search_jobs(query: str, results: int = 5) -> str:
    print(f"Searching jobs for: {query}")

    url = (
        "https://api.adzuna.com/v1/api/jobs/in/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page={results}"
        f"&what={query}"
        "&content-type=application/json"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return f"Error fetching jobs: {response.status_code}"

    data = response.json()

    if not data.get("results"):
        return "No jobs found."

    formatted_jobs = []

    for job in data["results"]:
        title = job.get("title", "Unknown Title")
        company = job.get("company", {}).get("display_name", "Unknown Company")
        location = job.get("location", {}).get("display_name", "Unknown Location")
        description = job.get("description", "")

        formatted_jobs.append(
            f"""
Job Title: {title}
Company: {company}
Location: {location}

Description:
{description[:700]}
"""
        )

    return "\n\n" + "=" * 60 + "\n\n".join(formatted_jobs)