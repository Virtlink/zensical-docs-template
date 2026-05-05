# Configure GitHub
This documentation includes a workflow for automatically updating dependencies. To make it work, you need to allow the automated creation and approval of pull requests in GitHub, and might want to configure auto-merge and setup automated checks.


## Allow automated PRs
In your GitHub repository:

1.  Go to _Settings_, _Actions_, _General_. Scroll to the bottom.
2.  Set:

    - Allow GitHub Actions to create and approve pull requests: :white_check_mark: yes

3.  Click _Save_.


## Require status checks
This requires status checks to succeed, before (automated or manual) PRs are auto-merged.

!!! note "This setting is recommended but not required"
    If the following is not configured, PRs created by the GitHub workflow are automatically merged without verifying that they build correctly.

In your GitHub repository:

1.  Go to _Settings_, _Branches_.
2.  Click _Add classic branch protection rule_ to create a new branch protection rule.
3.  Set:

    - Branch name pattern: `main`
    - **Protect matching branches**
        - Require status checks to pass before merging: :white_check_mark: yes
            - Require branches to be up to date before merging: :white_check_mark: yes
            - Status checks that are required: `Build`

4.  Click _Save changes_.


## Enable auto-merge
In your GitHub repository:

1.  Go to _Settings_, _General_. Scroll down to the _Pull Requests_ section.
2.  Set:

    - Allow auto-merge: :white_check_mark: yes


## Create a custom personal access token
By design, workflows that use the `GITHUB_TOKEN` [will not trigger new workflow runs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow), to avoid recursive workflow runs. This means that the status checks will not automatically run for the PRs created by the workflow. To fix this, we follow the GitHub recommended approach [outlined here](https://github.com/peter-evans/create-pull-request/blob/main/docs/concepts-guidelines.md#triggering-further-workflow-runs) and create a personal access token (PAT) with the `repo` scope.

1.  In your GitHub profile, go to _Settings_, _Developer settings_, _Personal access tokens_, _Tokens (classic)_ (or [click here](https://github.com/settings/tokens)).
2.  Click the _Generate new token_ button and select _Generate new token_.
3.  Set:

    - Token name: `Automated PR creation`
    - Description: `Access token used to create PRs in CI workflows. This allows the PR to trigger other workflows.`
    - Resource owner: (you)
    - Expiration: (a year from now)
    - Repository access:
        - All repositories
    - Permissions:
        - Contents: Read and write
        - Metadata: Read-only
        - Pull requests: Read and write

    !!! note ""
        Feel free to restrict the repositories for which this token works.

4.  Click _Generate token_.

!!! note "Machine account"
    Ideally you'd create this PAT on a [machine account](https://docs.github.com/en/github/site-policy/github-terms-of-service#3-account-requirements) with collaborator access to the repository.


## Configure the repository to use the personal access token
In your GitHub repository:

1.  Go to _Settings_, _Secrets and variables_, _Actions_.
2.  On the _Secrets_ tab, under _Repository secrets_, click _New repository secret_.
3.  Set:

    - Name: `PAT_CREATE_PR`
    - Secret: (the generated PAT, starts with `github_pat_`)

4.  Click _Add secret_.


## Update the workflow to use the personal access token
In the `update-python-dependencies.yaml` workflow:

1.  Replace all instances of `secrets.GITHUB_TOKEN` by `secrets.PAT_CREATE_PR`.
2.  Save and commit and push.

