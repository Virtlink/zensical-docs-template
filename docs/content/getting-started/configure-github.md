# Configure GitHub
This documentation includes a workflow for automatically updating dependencies. To make it work, you need to allow the automated creation and approval of pull requests in GitHub, and might want to configure auto-merge and setup automated checks.


## Allow automated PRs
In your GitHub repository:

1.  Go to _Settings_, _Actions_, _General_. Scroll to the bottom.
2.  Set:

    - Allow GitHub Actions to create and approve pull requests: :white_check_mark: yes

3.  Click _Save_.


## Require status checks
This requires status checks to succeed, before (automated or manual) PRs are auto-merged. In your GitHub repository:

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

