---
title: "Home"
---
# Zensical Docs Template
This is a Zensical Docs Template repository. It includes GitHub and GitLab CI workflows to easily publish pages.

[Zensical Documentation](https://zensical.org/){ .md-button }

## Quick Start
To use this template, install [Copier](https://copier.readthedocs.io/en/stable/) and invoke:

```shell
copier copy gh:virtlink/zensical-docs-template my-docs-repo
```

where `my-docs-repo` is the name of the directory where you want to create the new documentation repository. From within the documentation repository, to build the pages and see edits live using [UV](https://docs.astral.sh/uv/):

```shell
cd docs/
```
```shell
uv run zensical serve
```

Navigate to [localhost:8000](http://localhost:8000/) to see the documentation. The local documentation is automatically reloaded when changes occur. Changes pushed to the `main` branch are automatically deployed on GitHub and GitLab.


## Getting Started
Here is more documentation on how to use this template:

[Get Started](./getting-started/index.md){ .md-button .md-button--primary }



