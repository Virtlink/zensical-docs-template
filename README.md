# Zensical Docs Template
[![Build][github-build-badge]][github-build]
[![License][license-badge]][license]
[![Documentation][documentation-badge]][documentation]

A Zensical Docs Template repository. It enables an opinionated set of extensions and plugins by default, and contains GitHub and GitLab CI workflows to publish the documentation.

[![Documentation][documentation-button]][documentation]

- [Getting Started](https://pelsmaeker.net/zensical-docs-template/getting-started/create-the-project/)
- [Zensical documentation](https://zensical.org/)

This template is intended both for those that include the documentation in their main repository, and those that use a separate repository for the documentation, which is why all the documentation files are in the `docs/` subfolder.


## Quick Start
To use this template, install [Copier]() and invoke:

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

Navigate to [localhost:8000](http://localhost:8000/) to see the documentation.
The local documentation is automatically reloaded when changes occur.
Changes pushed to the `main` branch are automatically deployed on GitHub and GitLab.



## License
[![License: CC0-1.0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Daniel A. A. Pelsmaeker has waived all copyright and related or neighboring rights to the Zensical Docs Template repository. Feel free to use this as you see fit, no attribution required.

[github-build-badge]: https://img.shields.io/github/actions/workflow/status/Virtlink/zensical-docs-template/documentation.yaml
[github-build]: https://github.com/Virtlink/zensical-docs-template/actions
[license-badge]: https://img.shields.io/github/license/Virtlink/zensical-docs-template
[license]: https://github.com/Virtlink/zensical-docs-template/blob/master/LICENSE
[documentation-badge]: https://img.shields.io/badge/docs-latest-brightgreen
[documentation]: https://pelsmaeker.net/zensical-docs-template/
[documentation-button]: https://img.shields.io/badge/View_Documentation-blue?style=for-the-badge&logo=googledocs&logoColor=white
