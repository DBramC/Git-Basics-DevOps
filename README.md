# Git Basics Exercise -- DevOps

Welcome to the **Git Basics Exercise**. Follow the steps below to practice version control, branching, and history management using a Python web application. 

**Please do not copy paste code, write it so you will learn it**

## Prerequisites & Setup

1. **Configure Git:** Set your global Git username and email.

2. **Install Dependencies:** Install [Python 3.13 or higher](https://www.python.org/) and `uvicorn`.
   * Run the development server using the following command:
     ```bash
     py -3.13 -m uvicorn main:app --reload
     ```

3. **IDE:** Use the terminal of VSCode or configure git config to use the text editor of your choice 
---

## Exercises

### Staging & Ignoring Files

1. **First Commit:** Create a new endpoint in `main.py` then stage and commit **only** `main.py`.
   
2. **Ignore Files:** Run the server if it is not already running. **Notice** that `__pycache__` is generated. We do *not* want cache files in our Git history—configure Git to ignore it.

### Branching & Merging

3. **Create a Branch:** Create and switch to a new branch named `feat1`.

4. **Diff & Merge:** 
   * Create a new endpoint.
   * Use `git diff` to inspect your changes.
   * Commit the changes and merge `feat1` back into `main`.

5. **Merge Conflicts:** 
   * Switch to `main`, change the `/hello` endpoint to `/hi` (along with its contents), and commit.
   * Switch to `feat1`, change the `/hello` endpoint to `/goodbye`, and commit.
   * Merge `feat1` into `main` and **resolve the merge conflict**.

### Stashing & History Manipulation

6. **Reseting:** Reset the `main` branch history to the previous commit and delete the `feat1` branch.

7. **Stashing:**
   * Create and switch to a new branch named `feat2`.
   * Create another endpoint and **stash** your uncommitted changes.
   * Switch to `main`, delete the endpoint created in **Exercise 6**, and commit.
   * Switch back to `feat2`, **unstash** (pop) your changes, and commit them.
   * Merge `feat2` into `main` and delete the `feat2` branch.

8. **Revert:** On `main`, create and commit a new endpoint. Immediately **revert** this exact commit.

9. **Full Reset:** Reset the repository history back to the commit of **Exercise 2** (.gitignore).

10. **Recover:** Undo the full reset done in **Exercise 9** ( Hint it has something to do with `reflog`).

11. **Amend:** Make a new commit but make a typo in the commit message. After that create a new commit with correct spelling and amend it to the previous one.

12. **Partial Staging :** Make a change to an endpoint and create a new HELLO.txt file. Commit these two changes with two different commits using `git add -p`. 

13. **Partial Staging 2.0:** Do two changes to whatever endpoint you like. Make sure its *two different* endpoints. Using the `git add -p` with the correct **option**, commit the changes that are in the same file, with different commits. **One** for each change.

