# cs203s2021-practical6

[![Actions Status](../../workflows/build/badge.svg)](../../actions)

## DUE: by 8:30 am on Thursday, May 6

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Learning](#learning)
- [Tasks](#tasks)
- [System Commands](#system-commands)

  - [Using Pyenv and Pipenv](#using-pyenv-and-pipenv)
  - [Using Docker](#using-docker)
  - [Using Gradle](#using-gradle)

- [Output](#output)

- [Automated Checks with GatorGrader](#automated-checks-with-gatorgrader)

- [Updates](#updates)

- [GitHub Actions](#github-actions)

- [Reporting Problems](#reporting-problems)

- [Receiving Assistance](#receiving-assistance)

- [Practical Assessment](#practical-assessment)

## Introduction

Designed for use with [GitHub Classroom](https://classroom.github.com/) and [GatorGrader](https://github.com/GatorEducator/gatorgrader/), this repository contains the starter files for a practical assignment in an software engineering course class that uses the Python programming language. The GitHub Actions CI builds for this repository will fail, as evidenced by a red ✗ appearing in the commit logs.

This assignment requires a software engineer to explore Python object oriented programming style. Then, developers are invited to refactor the program and to write more test cases to increase the coverage. Finally, they are to reflect on four different types programming styles.

When you use the `git commit` command to transfer your source code to your GitHub repository, [GitHub Actions CI](https://github.com/features/actions) will initialize a build of your assignment, checking to see if it meets all of the requirements. If both your source code and writing meet all of the established requirements, then you will see a green ✔ in the listing of commits in GitHub. If your submission does not meet the requirements, a red ✗ will appear instead.

## Objectives

To practice using GitHub to access the files for a practical assignment. Additionally, to practice using the Ubuntu operating system and software development programs such as a "terminal window" and a "testing tool". You will also continue to practice using Slack to support communication with the technical leaders and the course instructor. You will carry on with practice in implementing and running a Python program and also using Pipenv and the course's automated grading tool to assess your progress towards correctly completing the project. Along with practicing how to use Pytest plugins, you will refactor the source code of a Python program implemented in the object-oriented style and then use parameterized testing to establish a confidence in the program's correctness. You will also further practice the refactoring of a Python program that does not meet certain design and implementation standards. Finally, you will compare and contrast the four programming styles covered in this course's practicals, identifying your preferences and the trade-offs inherent in each style.

## Learning

If you have not done so already, please read all of the relevant [GitHub Guides](https://guides.github.com/) that explain how to use many of the features that GitHub provides. In particular, please make sure that you have read the following GitHub guides: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/), [Hello World](https://guides.github.com/activities/hello-world/), and [Documenting Your Projects on GitHub](https://guides.github.com/features/wikis/). Each of these guides will help you to understand how to use both [GitHub](http://github.com) and [GitHub Classroom](https://classroom.github.com/).

To do well on this assignment, you should also read Chapters 1 and 5 in "Think Python" and review a [`termfrequency` program](https://github.com/crista/exercises-in-programming-style/blob/master/11-things/tf-11.py) accompanying the "Exercises in Programming Style" book. You should also read the first four chapters in "Python Testing with Pytest", making sure that you understand parameterized testing. Please make sure that you review the relevant content in "Cooperative Software Design" and "Philosophy of Software Design". You are also expected to find and read all additional online resources that you need to complete this assignment.

## Tasks

This assignment assumes that you have correct and working Docker, Git, Pipenv, and a recent version of Python.

Study the provided source code and the technical documentation to understand the type of output that your program produces. Make sure that you notice that this source code is incorrectly formatted and written in a fashion that uses non-standard features of the Python programming language. Part of your job for this assignment is to refactor the source code so that it meets all of the well-established standards for Python programs. Make sure that you format all of the Python source code and its comments so that it adheres to all of the linting standards, only disabling certain checks when there is no other alternative. Figures 1 and 2 provide two segments of Python source code that illustrate the correct way to reformat the code, adding the "pragmas" that disable certain linting checks as needed. You also need to ensure that the function comments adhere to the standard which mandates, among other requirements, that there be no spacing in the docstrings that must end with a period. Students who have questions about how to reformat the source code should talk to a technical leader or the course instructor, highlighting the problematic linting check.

As you are improving all of the provided code, you should also run the Pytest test suite that currently contains one test. Following the strategy of this test and the documentation for the functions in the program, add all of the test cases that you would need to achieve high coverage of the program under test. You should also write parameterized Pytest test cases that exercise the functions in this object-oriented-style program with numerous inputs. To implement a parameterized test case, you must decorate a Python testing function with the `` `@pytest.mark.parametrize`` annotation. Although you are not required to write all of your tests in a parameterized fashion, at least some of the new tests that you write must adopt this approach. Whenever possible, you should also use the Hypothesis automated test data generation tool to automatically create inputs for your test cases, documenting how the tool enables to you cover the source code of the functions.

Finally, please compare and contrast the pipeline and object-oriented versions of this program to this one that is written in an object-oriented fashion. What are the similarities and differences? Which one do you prefer? Which one is easier to test?

A summary of the tasks to be completed in this practical is below.

1. Study the given program in the object oriented style, trying to understand the structure and the flow of the program. Run it and observe that correct output is produced.

2. Using the command given in the [Using Pyenv and Pipenv](#using-pyenv-and-pipenv) section below, run linting and reformatting tools. You can also run `pydocstyle` tool by itself using `pipenv run pydocstyle`. Similarly, you can run linting tools individually, for example, `pylint` as `pipenv run pylint termfrequency/compute_tf_objectoriented.py`. Fix the linting problems based on the errors produced.

3. Study the test program. Run testing and study its results. Fix any errors that occur.

4. Add more test cases to improve coverage, including at least one parameterized test.

5. Complete the `reflection.md` document.

6. Ensure that all GatorGrader checks and GitHub actions pass.

## System Commands

This project invites students to enter system commands into a terminal window. This assignment uses [Docker](https://www.docker.com) to deliver programs, such as `gradle` and the source code and packages needed to run [GatorGrader](https://github.com/GatorEducator/gatorgrader), to a students' computer, thereby eliminating the need for a programmer to install them on their development workstation. Along with using Docker for automated grading and assessment on your laptop, students are also asked to setup a full-fledged Python development environment that leverages [Pyenv](https://github.com/pyenv/pyenv) to download and manage versions of Python and [Pipenv](https://github.com/pypa/pipenv) to install and manage Python packages.

### Using Pyenv and Pipenv

Assuming that you will use [Pyenv](https://github.com/pyenv/pyenv) to download and manage your installation of Python, this practical assignment also invites you to use [Pipenv](https://github.com/pypa/pipenv) to create a virtual environment, install and manage development packages, and to run Python commands. Previously, you should have run the following command:

- Install and upgrade the `pipenv` command: `pip install pipenv --user` or `sudo -H pip install -U pipenv` (note, if you have both Python2 and Python3, you may need to use `pip3` command instead of `pip`)

Here is a sample of the Pipenv commands that you will need to run during this assignment. Please note these commands are using the scripts located in your practical directory. If you prefer to run each individual tool separately, please refer to the commands you used in the previous practical.

- Install the new development dependencies with new `pytest` plugins: `pipenv` command: `pipenv install --dev`
- Run the linters and the formatter to check the Python source code: `pipenv run lint --check`
- Run the program with `pipenv` and `python3` and a small input: `pipenv run python3 termfrequency/compute_tf_objectoriented.py inputs/input.txt`
- Run the program with `pipenv` and `python3` and a realistic input: `pipenv run python3 termfrequency/compute_tf_objectoriented.py inputs/pride-and-prejudice.txt`
- Run the test suite to check your Python source code: `pipenv run test`
- Run the test suite and calculate test suite coverage: `pipenv run cover`

To run one of these commands, you must be in the main directory for this assignment where the configuration files are located. Then, you can type these commands in the terminal and study the output.

Since the provided test suite also uses Pytest's markers, then if you want to exclude the test cases that use Hypothesis you can type:

- `pipenv run pytest -m "not hypothesisworks"`

Alternatively, if you want to include the test cases that use Hypothesis you can type:

- `pipenv run pytest -m "hypothesisworks"`

### Using Docker

Once you have installed [Docker Desktop](https://www.docker.com/products/docker-desktop), you can use the following `docker run` command to start `gradle grade` as a containerized application, using the [DockaGator](https://github.com/GatorEducator/dockagator) Docker image available on [DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

```bash
docker run --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator
```

The aforementioned command will use `"$(pwd)"` (i.e., the current directory) as the project directory and `"$HOME/.dockagator"` as the cached GatorGrader directory. Please note that both of these directories must exist, although only the project directory must contain something. Generally, the project directory should contain the source code and technical writing of this assignment, as provided to a student through GitHub. Additionally, the cache directory should not contain anything other than directories and programs created by DockaGator, thus ensuring that they are not otherwise overwritten during the completion of the assignment. To ensure that the previous command will work correctly, you should create the cache directory by running the command `mkdir $HOME/.dockagator`.

If you are running your program on a Windows Operating System, you should run the following command instead, replacing the word "user" with the username of your machine:

```bash
docker run --rm --name dockagator -v "%cd%":/project -v "C:\Users\user/.dockagator":/root/.local/share gatoreducator/dockagator
```

Here are some additional commands that you may need to run when using Docker:

- `docker info`: display information about how Docker runs on your workstation
- `docker images`: show the Docker images installed on your workstation
- `docker container list`: list the active images running on your workstation
- `docker system prune`: remove many types of "dangling" components from your workstation
- `docker image prune`: remove all "dangling" docker images from your workstation
- `docker container prune`: remove all stopped docker containers from your workstation
- `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

### Using Gradle

Since the above `docker run` command uses a Docker image that, by default, runs `gradle grade` and then exits the Docker container, you may want to instead run the following command so that you enter an "interactive terminal" that will allow you to repeatedly run commands within the Docker container.

In Linux and Mac OS:

```bash
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

In Windows OS (replace `user` with your machine's username):

```bash
docker run -it --rm --name dockagator -v "%cd%":/project -v "C:\Users\user/.dockagator":/root/.local/share gatoreducator/dockagator /bin/bash
```

Once you have typed this command, you can use the [GatorGrader tool](https://github.com/GatorEducator/gatorgrader) in the Docker container by typing the command `gradle grade` in your terminal. Running this command will produce a lot of output that you should carefully inspect. If GatorGrader's output shows that there are no mistakes in the assignment, then your source code and writing are passing all of the automated baseline checks. However, if the output indicates that there are mistakes, then you will need to understand what they are and then try to fix them.

## Output

Running the program with the small input should produce the following output:

```
live  -  2
mostly  -  2
white  -  1
tigers  -  1
india  -  1
wild  -  1
lions  -  1
africa  -  1
```

Running the program with the realistic input should produce the following output:

```
mr  -  786
elizabeth  -  635
very  -  488
darcy  -  418
such  -  395
mrs  -  343
much  -  329
more  -  327
bennet  -  323
bingley  -  306
jane  -  295
miss  -  283
one  -  275
know  -  239
before  -  229
herself  -  227
though  -  226
well  -  224
never  -  220
sister  -  218
soon  -  216
think  -  211
now  -  209
time  -  203
good  -  201
```

A partial output from running the test suite initially is below. You will add more test cases to improve coverage:

```
tests/test_compute_tf_pipeline.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓                   100% ██████████

---------- coverage: platform darwin, python 3.8.3-final-0 -----------
Name                                   Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------
termfrequency/__init__.py                  0      0      0      0   100%
termfrequency/compute_tf_pipeline.py      33     18     10      1    37%   11-13, 31-35, 40-49, 54, 59-61, 69
----------------------------------------------------------------------------------
TOTAL                                     33     18     10      1    37%
Coverage XML written to file coverage.xml


Results (1.14s):
     21 passed
```

## Automated Checks with GatorGrader

In addition to meeting all of the requirements outlined in the assignment sheet, your submission must pass the following checks that [GatorGrader](https://github.com/GatorEducator/gatorgrader) automatically assesses. If [GatorGrader's](https://github.com/GatorEducator/gatorgrader) automated checks pass correctly, the tool will produce the output similar to the one below.

```
✔  The __init__.py in tests has exactly 0 of the 'TODO' fragment
✔  The file conftest.py exists in the tests directory
✔  The reflection.md in writing has at least 400 word(s) in total
✔  The reflection.md in writing has exactly 8 of the 'heading' tag
✔  The reflection.md in writing has exactly 0 of the 'TODO' fragment
✔  The file test.sh exists in the scripts directory
✔  The file __init__.py exists in the tests directory
✔  The repository has at least 3 commit(s)
✔  The file cover.sh exists in the scripts directory
✔  The reflection.md in writing has at least 1 of the 'code_block' tag
✔  The test_compute_tf_objectoriented.py in tests has at least 0 single-line Python comment(s)
✔  The cover.sh in scripts has exactly 0 of the 'TODO' fragment
✔  The compute_tf_objectoriented.py in termfrequency has at least 7 multiple-line Python comment(s)
✔  The test_compute_tf_objectoriented.py in tests has at least 1 of the '@pytest.mark.parametrize' fragment
✔  The file test_compute_tf_objectoriented.py exists in the tests directory
✔  The compute_tf_objectoriented.py in termfrequency has exactly 0 of the 'TODO' fragment
✔  The file lint.sh exists in the scripts directory
✔  The file compute_tf_objectoriented.py exists in the termfrequency directory
✔  The test_compute_tf_objectoriented.py in tests has at least 5 multiple-line Python comment(s)
✔  The lint.sh in scripts has exactly 0 of the 'TODO' fragment
✔  The test_compute_tf_objectoriented.py in tests has exactly 0 of the 'TODO' fragment
✔  The reflection.md in writing has exactly 0 of the 'Add Your Name Here' fragment
✔  The test_compute_tf_objectoriented.py in tests has at least 5 of the 'test_' fragment
✔  The test_compute_tf_objectoriented.py in tests has at least 5 of the 'assert' fragment
✔  The conftest.py in tests has exactly 0 of the 'TODO' fragment
✔  The compute_tf_objectoriented.py in termfrequency has at least 3 single-line Python comment(s)
✔  The file reflection.md exists in the writing directory
✔  The test.sh in scripts has exactly 0 of the 'TODO' fragment


    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Passed 28/28 (100%) of checks for cmpsc-203-spring-2021-practical7! ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Updates

If the course instructor updates the provided material for this assignment and you would like to receive these updates, then you can type this command in the main directory for this assignment:

```
git remote add download git@github.com:allegheny-computer-science-203-s2021/practical07.git
```

You should only need to type this command once; typing the command additional times may yield an error message but will not negatively influence the state of your repository. Now, you are ready to download the updates provided by the course instructor by typing:

```
git pull download main
```

This second command can be run whenever the course instructor needs to provide you with new source code for this assignment. However, please note that, if you have edited the files that the course instructor updated, running the previous command may lead to Git merge conflicts. If this happens, you may need to manually resolve them with the help of the instructor or a teaching assistant.

## GitHub Actions

This assignment uses [GitHub Actions CI](https://github.com/features/actions) to automatically run the checking programs every time you commit to your GitHub repository. The checking will start as soon as you have accepted the assignment, thus creating your own private repository.

## Reporting Problems

If you have found a problem with this assignment's provided source code, then you can go to the [Computer Science 203 Practical 7 Starter](https://github.com/allegheny-computer-science-203-s2021/practical07) repository and create an issue by clicking the "Issues" tab and then clicking the green "New Issue" button. If you have found a problem with the [GatorGrader tool](https://github.com/GatorEducator/gatorgrader) and the way that it checks you assignment, then you can follow the aforementioned steps to create an issue in its repository. To ensure that your issue is properly resolved, please provide as many details as is possible about the problem that you experienced.

Students who find and use the appropriate GitHub issue tracker to correctly document a mistake in any aspect of this laboratory assignment will receive free GitHub stickers and extra credit towards their grade for it.

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a teaching assistant during the laboratory session. Alternatively, you may ask questions in the Slack workspace for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **Percentage of Correct GatorGrader Checks**: Students are encouraged to repeatedly try to improve their submission so that it passes all of GatorGrader's checks by, for instance, creating a correct number of minimum test cases. Students should also repeatedly revise their technical writing to ensure that it also passes all of GatorGrader's checks about, for instance, the length of its content and its appropriate use of Markdown.

- **GitHub Actions CI Build Status**: Since additional checks on the source code and/or technical writing may be encoded in GitHub Actions CI's actions and, moreover, all of the GatorGrader checks are also run in GitHub Actions CI, students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗. As with the previous grading component, students are encouraged to repeatedly revise their code and technical writing in an attempt to get their GitHub Actions CI build to pass.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
