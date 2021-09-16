from typing import Any, Dict


path = "${{ cookiecutter.plugin.removeprefix('rsserpent-plugin-') }}"


async def provider() -> Dict[str, Any]:
    """Define a basic example data provider function."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Article", "description": "Example Content"}],
    }