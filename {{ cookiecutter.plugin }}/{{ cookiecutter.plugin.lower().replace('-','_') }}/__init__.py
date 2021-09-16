from rsserpent.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="{{ cookiecutter.plugin }}",
    author=Persona(
        name="{{ cookiecutter.username }}",
        link="{{ cookiecutter.link }}",
        email="{{ cookiecutter.email }}"
    ),
    prefix="/{{ cookiecutter.plugin.removeprefix('rsserpent-plugin-') }}",
    repository="https://github.com/{{ cookiecutter.username}}/{{ cookiecutter.plugin }}",
    routers={route.path: route.provider},
)