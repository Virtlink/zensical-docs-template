# Create the Project

- [Generate the project using Copier](#generate-the-project-using-copier-recommended)
- [Cloning the template](#cloning-the-template)

## Generate the project using Copier (recommended)
Alternatively, you can use [Copier](https://copier.readthedocs.io/en/stable/). Follow the [Copier installation instructions](https://copier.readthedocs.io/en/stable/#installation) and then invoke:

```shell
copier copy gh:virtlink/zensical-docs-template my-docs-repo
```

where `my-docs-repo` is the name of the directory where you want to create the new documentation repository. Answer the questions and the files will be generated.


## Cloning the template
You can clone the template into a new repository on GitHub using the _Use this template_ button in the top-right and selecting _Create a new repository_.

Alternatively, you can create a new Git repository using `git init` and then follow the instructions to apply the template to an existing repository.

In any case, after cloning the repository contents, remove the following files and directories:

- `copier.yml`
- `LICENSE`
- `README.md`
- `template/`

Furthermore, change the fields in `zensical.toml` to suit your needs. In particular, change `site_url` to the URL where the site will be hosted. Additionally, change the `site_name`, `site_description`, `site_author`, and the URLs for `repo_url` (where the repository button links to) and `edit_uri` (where the pages can be edited).

