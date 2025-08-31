import os
from dotenv import load_dotenv

load_dotenv(".gitignore.env") # load all the variables from the env file

from notion_client import AsyncClient

#creates asyncio environment for asynchronous client
notion = AsyncClient(auth=os.getenv("NOTION_API"))

async def add_entry_to_person_property(
    database_id: str,
    person_name: str,
    property_name: str,
    property_value: int
):
    """
    Finds a page in the given Notion database by the person's name
    and updates the given property with the integer value.
    """
    results = await notion.databases.query(
        database_id=database_id,
        filter={
            "property": "FirstName",  # adjust to your actual property name
            "title": {"equals": person_name}
        }
    )
    if not results.get("results"):
        return None

    page_id = results["results"][0]["id"]

    return await notion.pages.update(
        page_id=page_id,
        properties={
            property_name: {"number": int(property_value)}
        }
    )