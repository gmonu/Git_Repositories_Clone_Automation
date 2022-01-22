import git
import os
import pandas as pd
import pandasql as ps

# reading csv file of Github_account_details
df = pd.read_csv('github_account_details.csv')

source_accounts = df['source_account'].unique()  # taking all distinct account names

print("**************Please select a GitHub account from which you want to clone the Repositories*************")

for names in source_accounts:
    print('-->', names)
selected_account = input()  # taking input from user for selecting the particular account

# extracting all the repositories for user's selected account
selected_repo = ps.sqldf(f"select source_repo from df where source_account = '{selected_account}'")
to_clone_repos = []

# making new list with 'source_repo' header
for i in selected_repo.index:
    to_clone_repos.append(selected_repo['source_repo'][i])

total_repos_count = len(to_clone_repos)
print(f"Total repositories in {selected_account} are: {total_repos_count}\n{to_clone_repos}")
permission_to_clone = input("Give permission to Clone Y/N")

# cloning all the repos from to_clone_repos
if permission_to_clone == 'Y' or permission_to_clone == 'Yes' or permission_to_clone == 'YES' or permission_to_clone == 'yes':
    for repos in to_clone_repos:
        if not os.path.exists(selected_account):
            os.makedirs(selected_account)
        print(f"{repos} -- Cloning in Progress")
        git.Git(f'{selected_account}/').clone(f'https://github.com/{selected_account}/{repos}.git')
        print(f"{repos} -- Cloned successfully")