# GitHub Search

This Python script allows you to search for repositories on GitHub based on a search query. You can select a repository using its index and then choose to either clone the repository or perform another search.

## NOTE
It's recommended to use virtualenv but can also work without

## Prerequisites

- Python 3.11 or higher
- Git (if you want to clone repositories)

## Installation

1. Clone this repository:

    ```shell
    git clone https://github.com/sammyklane/github-search.git
    ```

2. Change into the project directory:

    ```shell
    cd github-search
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```shell
    python main.py
    ```

2. Enter your search query when prompted.

3. Select a repository by entering its corresponding index.

4. Choose an action:
    - To clone the repository, enter `clone`.
    - To perform another search, enter your query.
    - To exit the script, enter `exit`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).