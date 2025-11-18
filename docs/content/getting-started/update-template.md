---
title: "Update the template"
---
# Update the documentation template
After you've applied the template, you can update it to a new version by:

- [Update the project generated using Copier]()
- [Update the cloned template]()


## Update the project generated using Copier
When you used Copier to generate the project, you can also use Copier to update it.

```shell
copier update
```


## Update the cloned template
When you cloned the template repository, it can be updated through Git.

## Template Remote
First ensure the template repository is added as a remote for the documentation repository:

```shell
git remote -v
```
```
origin      git@github.com:MyUsername/my-docs-repo.git (fetch)
origin      git@github.com:MyUsername/my-docs-repo.git (push)
template    git@github.com:Virtlink/zensical-docs-template.git (fetch)
template    git@github.com:Virtlink/zensical-docs-template.git (push)
```

If not, add the template remote repository:

```shell
git remote add template git@github.com:Virtlink/zensical-docs-template.git
```


## Merge latest changes
Fetch the changes in the template remote:

```shell
git fetch template
```

Then merge the latest changes from the template's `main` branch into your repository:

```shell
git merge template/main
```

!!! tip "Unrelated Histories"
    If you get the error `fatal: refusing to merge unrelated histories`, then your documentation repository was never based on the template. However, you can force Git to merge the template anyway by using this command:

    ```sh
    git merge template/main --allow-unrelated-histories
    ```

Finally, use the Git command line to fix any merge conflicts, and commit the result.

