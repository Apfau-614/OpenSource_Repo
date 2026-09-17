# Pytest Lab

In this lab you will walk through the basic procedure for creating and contributing to an open source project.

<img src=img/meme.jpg width=300px />

## Instructions

You will need a partner to complete this lab.
Try to work with someone you don't already know.

In part 0 below you will prepare a new repo on your own account.
In part 1, your partner will contribute to your repo (and you to theirs).

### Part 0: Creating your repo

1. Create a new repository by clicking the "+" sign in the top right corner of the github webpage.

   It doesn't matter what you name your repo, except that it must be different than what your partner names their repo.

   Ensure the repository is public and that you are not creating any default files in the repo (like a README or LICENSE file).

1. On the lambda server, create an empty git repo by running the commands:

    ```
    $ mkdir pytest-example
    $ cd pytest-example
    $ git init
    ```

    Next you will connect your repo on the lambda server to my repo on github with the commands:
    ```
    $ git remote add upstream https://github.com/mikeizbicki/pytest-example
    $ git pull upstream master
    ```
    Verify that the commands worked correctly by running `ls` and observing that the contents of the folder in the lambda server match github.

    The `git pull` command is what actually downloads the contents from the lambda server and places them into your current folder.
    It takes two parameters:
    1. The "remote", which is an alias for a url.
        In the first command above we added `https://github.com/mikeizbicki/pytest-example` as the remote called `upstream`.
        This is the traditional name for a repo located on a foreign server (like github.com) that you do not own.
    2. The branch that we want to download.
        In this case we are downloading the branch `master`.
        Depending on your configurations, you might currently be in the `master` branch, `main` branch, or something else on your local repo.
        The local repo branch, however, doesn't actually matter.

    Finally we will connect your local repo on the lambda server to your newly created repo on github.
    ```
    $ git remote add origin $YOUR_REPO_URL
    $ git push origin master
    ```
    (You should substitute your repo url for the variable `$YOUR_REPO_URL` above.)

    If everything worked correctly, then you should have a copy of my repo in your repo on github.

1. Modify the README file to include a test cases badge and push it to github.

    > **HINT:**
    > I'm not going to directly tell you how to do this.
    > Instead, you should look at a repo that already has a test cases badge and copy the format of that code.
    > In general, this type of copying from other people's projects to include features they have and you want is highly encouraged.

   Once you've completed this step, you should now have a RED badge because the test cases are failing.

1. At this point, you are not allowed to directly modify your repository at all.
    Instead, your partner will follow the steps in Part 2 below to fix your repo.
    (And you will follow the steps to fix theirs.)

### Part 1: Contributing to your partner's repo

1. Fork your partner's repo.

1. On the lambda server, clone and enter your forked repo.

1. Run the following command:
    ```
    $ python3 -m pytest
    ```

1. Modify the `Fixme.py` file so that all of the tests pass.

1. Submit a pull request with changes that you've made.

    > **NOTE:**
    > You should not be submitting a pull request to my repo,
    > but to your partner's repo.

1. When you receive your partner's pull request, you should see an option to run the github actions before accepting the merge.
    You should do this and check that the change fixes the test cases before accepting the pull request.

    Test cases allow us to collaborate effectively with each other and ensure that our code is always *provably* correct.
    Maintainers of open source projects won't accept contributions that break test cases.

## Submission

Paste the URL to both your repo and your partner's repo into canvas.
