import requests
from kwslogger import Logger

class GithbuRepoGetter:
    def __init__(self, username: str):
        self.logger = Logger()
        self.logger.clear()
        self.logger.create_logo("Repo Getter")
        self.username = username

    def get_json(self):
        self.logger.info("Requesting JSON")
        url = f"https://api.github.com/users/{self.username}/repos"
        self.logger.info(f"Requesting {url}")
        response = requests.get(url)
        return response.json()
    
    def get_repos(self):
        self.logger.info("Getting repos")
        json = self.get_json()
        repos = []
        for repo in json:
            repos.append(f"{repo['name']} -> {repo['description']}")
        return repos
    
    def download_repos_info(self):
        self.delete_old_repos()
        self.logger.info("Writing repos to repos.txt")
        repos = self.get_repos()
        with open(f"repos-{self.username}.txt", "w") as f:
            for repo in repos:
                f.write(repo + "\n")

    def delete_old_repos(self):
        self.logger.info("Deleting old repos")
        with open(f"repos-{self.username}.txt", "w") as f:
            f.write("")

if __name__ == "__main__":
    getter = GithbuRepoGetter("kWAYTV")
    getter.download_repos_info()