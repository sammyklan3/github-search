import requests
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def search_github_repositories(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()['items']
        return repositories
    else:
        print(Fore.RED + "Failed to retrieve repositories.")
        return None

def display_repositories(repositories):
    if repositories:
        print(Fore.GREEN + "Search Results:")
        print("-" * 50)
        for index, repo in enumerate(repositories):
            print(f"{Fore.RED}{index + 1}. {Fore.RESET}{repo['full_name']} - {repo['description']}")
        print("-" * 50)

def display_repository_details(repository):
    print(Fore.CYAN + "Repository Details:")
    print("-" * 50)
    print(f"{Fore.MAGENTA}Repository: {Fore.RESET}{repository['full_name']}")
    print(f"{Fore.MAGENTA}Description: {Fore.RESET}{repository['description']}")
    print(f"{Fore.MAGENTA}Language: {Fore.RESET}{repository['language']}")
    print(f"{Fore.MAGENTA}URL: {Fore.RESET}{repository['html_url']}")
    print("-" * 50)

def clone_repository(repository):
    clone_url = repository['clone_url']
    os.system(f"git clone {clone_url}")

def main():
    last_repositories = []

    while True:
        print(Style.RESET_ALL)
        query = input(Fore.YELLOW + "Enter the search query (or 'exit' to quit): ")
        
        if query.lower() == 'exit':
            break
        
        repositories = search_github_repositories(query)
        
        if repositories:
            last_repositories = repositories
            display_repositories(repositories)
            
            try:
                choice = int(input(Fore.YELLOW + "Enter the index of the repository you want to view details for (or '0' to go back): "))
                
                if choice == 0:
                    continue
                
                if 1 <= choice <= len(repositories):
                    selected_repository = repositories[choice - 1]
                    display_repository_details(selected_repository)
                    
                    action = input(Fore.YELLOW + "Enter 'clone' to clone the repository or 'back' to go back to the list: ")
                    
                    if action.lower() == 'clone':
                        clone_repository(selected_repository)
                        print(Fore.GREEN + f"Successfully cloned {selected_repository['full_name']}.")
                    elif action.lower() == 'back':
                        continue
                    else:
                        print(Fore.RED + "Invalid action.")
                else:
                    print(Fore.RED + "Invalid index.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
        else:
            print(Fore.RED + "No repositories found.")

if __name__ == "__main__":
    main()
