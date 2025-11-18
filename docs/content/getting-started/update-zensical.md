# Update Zensical
To update the Zensical dependency, find the latest release in the [Zensical releases](https://github.com/zensical/zensical/releases) and update the Zensical version in `docs/pyproject.toml`. Then run:

```shell
cd docs/
```
```shell
uv sync --dev
```

New versions of Zensical can have breaking changes.
[Find them here](https://zensical.org/docs/upgrade/) or in the release notes.