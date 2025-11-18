# Zensical Docs Template
This is a Zensical Docs Template repository. It includes GitHub and GitLab CI workflows to easily publish pages.

To use, invoke:

```bash
uv run zensical serve
```

This will publish the documentation at [localhost:8000](http://localhost:8000/) by default, and watch for any changes to the documentation source files.

[Zensical Documentation](https://zensical.org/){ .md-button }


## Customization
Change the fields in `zensical.toml` to suit your needs. In particular, change `site_url` to the URL where the site will be hosted. Additionally, change the `site_name`, `site_description`, `site_author`, `copyright`, and the URLs for `repo_url` (where the repository button links to) and `edit_uri` (where the pages can be edited).


## Updating
To change the version of Zensical, change the version number in `pyproject.toml` and run `uv sync`.


## Different branch
The template assumes your default branch is named `main` or `master`. If it's named something else, change the `on push branches` in `.github/workflows/documentation.yaml`:

```yaml
on:
  push:
    branches:
      - my-docs-branch
```

# Deploying
This documentation can be deployed on Github (`.github/workflows/documentation.yaml`) or Gitlab (`.gitlab-ci.yml`).


# Updating to Latest Template
This page describes how to update your documentation to include the latest changes to the template repository.


## Template Remote
To update to the latest version of the template, first ensure the template repository is added as a remote for the documentation repository:

```sh
git remote -v

origin      git@github.com:MyUsername/my-docs-repo.git (fetch)
origin      git@github.com:MyUsername/my-docs-repo.git (push)
template    git@github.com:Virtlink/zensical-docs-template.git (fetch)
template    git@github.com:Virtlink/zensical-docs-template.git (push)
```

If not, add the template remote repository:

```sh
git remote add template git@github.com:Virtlink/zensical-docs-template.git
```


## Fetch Latest Changes
Fetch the changes in the template remote:

```sh
git fetch template
```


## Merge Latest Changes
Merge the latest changes from the template's `main` branch into your repository:

```sh
git merge template/main
```

??? tip "Unrelated Histories"
    If you get the error `fatal: refusing to merge unrelated histories`, then your documentation repository was never based on the template. However, you can force Git to merge the template anyway by using this command:

    ```sh
    git merge template/main --allow-unrelated-histories
    ```


## Fix Any Conflicts, and Commit
Now use the Git command line to fix any merge conflicts, and commit the result.


## Fix the Breaking Changes
New versions of Zensical can have breaking changes.
[Find them here](https://zensical.org/docs/upgrade/).