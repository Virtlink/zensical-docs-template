---
title: "Configure GitHub"
---
# Configure GitHub
This documentation includes workflows for automatically updating dependencies. To make them work, you need to allow the automated creation and approval of pull requests in GitHub, configure auto-merge, and set up automated checks. The workflows authenticate as a [GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps), so that the created pull requests trigger subsequent workflows (which the default `GITHUB_TOKEN` cannot do) and commits are authored by the bot account.


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
            - Status checks that are required: `Build Documentation`

4.  Click _Save changes_.


## Enable auto-merge
In your GitHub repository:

1.  Go to _Settings_, _General_. Scroll down to the _Pull Requests_ section.
2.  Set:

    - Allow auto-merge: :white_check_mark: yes


## Create a GitHub App
By design, workflows that use the `GITHUB_TOKEN` [will not trigger new workflow runs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflow-runs/trigger-a-workflow#triggering-a-workflow-from-a-workflow), to avoid recursive workflow runs. This means that the status checks will not automatically run for the PRs created by the workflow. To fix this, the workflows authenticate as a [GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) instead of using the `GITHUB_TOKEN`. Commits and PRs created by the App show up as authored by the bot account, and the App's commits are signed by GitHub and show as :white_check_mark: _Verified_.

1.  In your GitHub profile, go to _Settings_, _Developer settings_, _GitHub Apps_ (or [click here](https://github.com/settings/apps)).
2.  Click _New GitHub App_. Give the following values:

    - GitHub App name: `Virtlink Bot`
    - Homepage URL: `https://pelsmaeker.net/`
    - **Webhook**
        - Active: :x: disabled
    - **Repository permissions**
        - Contents: Read and write
        - Pull requests: Read and write
        - Issues: Read and write
        - Metadata: Read-only (required)
        - Workflows: Read and write
    - Where can this GitHub App be installed? Only on this account

    !!! note "Workflow permission"
        The _Workflows_ permission is required because the _Update GitHub Actions_ workflow uses [Renovate](https://docs.renovatebot.com/) to update the versions of the GitHub Actions referenced in the workflow files themselves. Without this permission, GitHub rejects any push that modifies files under `.github/workflows/`.

3.  Click _Create GitHub App_.
4.  Under _Private keys_, click _Generate a private key_ and download the `.pem` file.
    Keep it safe, as you will not be able to download it again.
5.  Determine the _App ID_ (found at the top under _About_).


## Install the GitHub App
In the GitHub App settings, click _Install App_ and click the _Install_ button next to the account to install the bot to. You can restrict the App to specific repositories.


## Configure the repository to use the GitHub App
In the GitHub repository:

1.  Go to _Settings_, _Secrets and variables_, _Actions_.
2.  On the _Secrets_ tab, under _Repository secrets_, click _New repository secret_.
3.  Add the following secret:

    - Name: `APP_ID`
    - Secret: the _App ID_ of the GitHub App

4.  Click _Add secret_.
5.  Click _New repository secret_ again, and add:

    - Name: `APP_PRIVATE_KEY`
    - Secret: the entire contents of the `.pem` file (the App's private key)

    !!! note ""
        The private key is a multi-line string. Make sure to copy the entire contents of the `.pem` file. For example:

        ```
        -----BEGIN RSA PRIVATE KEY-----
        MIIEpgIBAAKCAQEAm9KB2dFRW9iRaRpdaUCWwPxRzlI3hmZxGWX60ump49NuJ4XM
        ...
        RR5z3JpJfVU4pfu8rOeEURBgLuUM4JMho2qU769I8VVlDTjRpRaaITp1
        -----END RSA PRIVATE KEY-----
        ```

6.  Click _Add secret_.

The workflows already use the `APP_ID` and `APP_PRIVATE_KEY` secrets to generate an App token, so no further changes to the workflows are needed.
