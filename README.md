# Pyschool

This project is my notes from learning Python and Git.  
My intent is to use it as a reference when working on other Python projects.

This project will use Python specific syntax and PEP8 style guide.  
It will also have some reminders of good coding/version control practices.

I'll add notes here as I feel is needed.

### Git Commands Index
 - `git fetch origin` Retrieve changes from remote repository without merging to local.
 - `git pull origin main` Merges remote `main` branch with your current branch.
 - `git status` See Git info such as your current branch, and files that have been changed/need commits.
 - `git checkout <branch-name>` Change your current branch.
 - `git add <file_name>` Stage file for commit. 
 - `git commit -m "concise message"` Commit project changes that will be pushed.
 - `git push <branch-name>` Push changes from current branch to `<branch-name>`.
 - `git checkout -b <branch-name>` Create new local branch.
 - `git branch -d <branch-name>` Delete local branch.
 - `git push -u origin <branch-name>` Push local branch to remote repository. ("Creates" remote branch.)
 - `git push origin --delete <branch-name>` Delete remote branch.
 - 

## Starting the day through Git:

1. **Fetch Updates:**
    - Begin by fetching any changes that might have occurred in the remote repository since your last session:
        - `git fetch origin`
        - This retrieves any new commits or branches without merging them into your local branches,
          allowing you to review them first.

2. **Review Updates (if applicable):**
    - If working in a collaborative environment, check for new commits or branches using:
        - `git branch -a` to see all local and remote branches.
        - `git log main..origin/main` to view commits on `origin/main` that aren't in your local `main` branch.
    - Assess whether you need to merge or rebase to incorporate these changes into your local work.

3. **Checkout Appropriate Branch:**
    - Ensure you're working on the correct branch:
        - `git checkout main` to switch to the `main` branch.
    - Create a new branch for new features or bug fixes to isolate your work:
        - `git checkout -b <branch-name>`
            - Use prefixes to categorize branches and instantly understand their purpose.
                - e.g., `feature/` `bugfix/` `hotfix/` `release/` `docs/` `test/`
            - After the prefix, add a descriptive suffix that clarifies the specific change or feature.
                - e.g., `feature/add-login-system` `bugfix/crash-on-startup` `release/v1.2.0`

4. **Pull Changes (if necessary):**
    - If you need to incorporate remote changes into your local branch, use:
        - `git pull origin main` to fetch and merge changes from the remote `main` branch into your local `main` branch.

5. **Review Status:**
    - Use `git status` to check the status of your working directory, including untracked files, modified files,
      and file stages. This helps you understand what changes you've made and what needs to be committed.

## Ending the day through Git:

1. **Committing Changes:**
    - Stage relevant changes: Ensure you've staged all the changes you want to track before committing.
      Use `git add <file_name>` to stage specific files or `git add .` to stage everything.
    - Write informative commit messages: Summarize the changes you made in a clear and concise message. Mention the
      issue fixed, feature added, or task completed. A good message helps understand the code's evolution later.
    - Create multiple commits for significant work: If you worked on various things throughout the day, consider
      splitting them into separate commits with focused messages. This allows for finer-grained rollback if needed.

2.**Organizing Branches**
   - Push your work to remote: After committing, push your local changes to the remote repository 
     (e.g., GitHub) using `git push <branch-name>`. This ensures your work is backed up and accessible to others.
   - Switch to `main` branch: If you were working on a feature branch, switch back to the main branch using 
     `git checkout main`. This ensures you're working on the current codebase when starting your next session.
   - Clean up local branches (optional): If you have completed feature branches and pushed them to remote, consider 
     deleting them locally using `git branch -d <branch-name>`. This keeps your local environment tidy.

## Key Points:
- Review your changes: Before committing, take a moment to review your code and messages to ensure everything is 
  correct and well-documented.
- Commit Frequently: Make small, focused commits with clear messages to track progress and facilitate collaboration.
- Pull Often: Pull changes from the remote repository regularly to stay up-to-date and avoid merge conflicts.
- Utilize Branching: Use branches for features, bug fixes, and experiments to isolate changes and maintain a clean  
  `main` branch.
- Address Conflicts Proactively: Resolve merge conflicts as soon as they arise to prevent accumulation and
  more complex issues.
- Communicate with Collaborators: Discuss changes and branching strategies with teammates to ensure a smooth
  workflow and avoid misunderstandings.
