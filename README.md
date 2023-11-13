# 🌟 GitHub Repo Getter 🌟

## 📖 Introduction
This Python script, **GitHub Repo Getter**, is designed to fetch and list all repositories for a specified GitHub user. It utilizes the GitHub API to retrieve repository names and descriptions, offering a simple and efficient way to access repository information.

## 🚀 Features
- Fetches all repositories of a specified GitHub user.
- Retrieves names and descriptions of repositories.
- Logs all actions for easy debugging and monitoring.
- Writes repository information to a text file.

## ⚙️ Installation
To use GitHub Repo Getter, you'll need Python installed on your system.

1. Clone the repository:
```bash
git clone https://github.com/kWAYTV/github-repo-getter.git
```
2. Navigate to the project directory:
```bash
cd github-repo-getter
```

## 📋 Usage
Ensure you have `requests` and `kwslogger` libraries installed. You can install them using pip:
```bash
pip install requests kwslogger
```

To run the script, simply execute:
```python
python3 github_repo_getter.py
```


## 📝 How It Works
- Specify the GitHub username.
- The script fetches the repositories and their descriptions using GitHub's API.
- Information is logged for transparency.
- Repository data is saved in a text file.

## 🤝 Contributing
Feel free to fork the project, make changes, and submit pull requests!

## ⚠️ License
Distributed under the MIT License. See `LICENSE` for more information.