from rich.console import Console
import json
import csv
import os

console = Console()


def welcome():
    console.print("Instagram Follow Back Checker", style="bold white")
    console.print("by [bold white]evenblad3\n[/]")


def ask():
    ask = input("Path of .json files: ")
    return os.path.normpath(ask)


def main(json_files_path):
    followers_file = "followers_1.json"
    following_file = "following.json"

    followers_list = []
    following_list = []

    follow_check = {}

    print("Checking...")
    if os.path.isdir(json_files_path):
        # Read Followers
        followers_file_path = os.path.join(json_files_path, followers_file)
        if os.path.isfile(followers_file_path):
            with open(followers_file_path) as f:
                info = json.load(f)
                for i in info:
                    if "string_list_data" in i:
                        followers_list.append(i["string_list_data"][0]["value"])

        # Read Following
        following_file_path = os.path.join(json_files_path, following_file)
        if os.path.isfile(following_file_path):
            with open(following_file_path) as f:
                info = json.load(f)
                for i in info["relationships_following"]:
                    if "string_list_data" in i:
                        following_list.append(i["title"])

        followers_list.sort()
        following_list.sort()

        for person in following_list:
            if person in followers_list:
                follow_check[person] = "Following Back"
            else:
                follow_check[person] = "Not Following"

        followers = len(followers_list)
        following = len(following_list)

        for person, status in follow_check.items():
            if status == "Following Back":
                console.print(f"[bold green]{person}: {status}[/]")
            else:
                console.print(f"[bold red]{person}: {status}[/]")

        print(f"\nFollowers {followers}\nFollowing {following}")


welcome()
main(ask())
