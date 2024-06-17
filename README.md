# Ninmu-api
The backend REST API for Ninmu, serves the web and mobile clients


# Infrastructure:
### Describe your process for branching and merging in your team’s repository (e.g. GitHub flow, Picking the right branch-merge strategy):

## Branching:
### Main Branch: The main branch always contains production-ready code.
### Feature Branches: Create separate branches for each new feature or bug fix. Name branches descriptively, e.g., feature/user-auth or bugfix/login-issue.
### Process:
Create a Branch: When starting a new task, create a new branch from main.
```
git checkout -b feature/your-feature-name
```
### Develop and Commit: Make changes and commit them frequently with clear messages.
```
git commit -m "Add user authentication"
```
### Push to Remote: Push the feature branch to the remote repository.
```
git push origin feature/your-feature-name
```
## Merging:
### Pull Request (PR): Open a PR against the main branch when the feature is complete. Include a description of changes and any relevant issue numbers.
### Code Review: Team members review the PR, suggest changes, and approve it.
### Merge: Once approved and tests pass, merge the PR into main.
```
git checkout main
git pull origin main
git merge feature/your-feature-name
 ```
### Delete Branch: After merging, delete the feature branch from the remote repository.
```
git push origin --delete feature/your-feature-name
```
## Additional Strategies:
### Rebasing: Use rebasing for cleaner commit history before merging.
```
git rebase main
```
### Squash and Merge: Squash commits into a single commit for a cleaner history.
