import subprocess
import json

# Functions
def collect_data(repo_name):
    data = {}
    # Info collection
    data["repo_name"] = repo_name
    data["user_name"] = input("Username (press ENTER for 'm-GDEV' default): ")
    data["author_name"] = input("Author Name (press ENTER for 'Musa Ahmed' default)")
    data["author_email"] = input("Author Email (press ENTER for 'musaa.ahmed7@gmail.com' default)")
    data["project_name"] = input("Project Name: ")
    data["project_tagline"] = input("Project Tagline: ")
    data["project_description"] = input("Project Description (in markdown): ")
    data["logo_location"] = input("Logo path in project files: ")
    data["demo_media_location"] = input("Demo media location in project files (image or gif): ")
    data["installation_steps"] = input("Installation Steps (in markdown): ")
    data["contributing_steps"] = input("Contributing steps (leave blank to use default. in markdown): ")
    data["license_information"] = input("License Information (in markdown): ")
    data["acknowledgements"] = input("Acknowledgments (in markdown): ")

    # built with
    built_with_badges = []
    input("Please select all technologies that you've used for this project now. Press ENTER to continue.")
    while True:
        print("Please select technologies used.")
        res = subprocess.run("cat shield_names.txt | fzf", shell=True, stdout=subprocess.PIPE, text=True) 
        shield_name = res.stdout.strip()
        res2 = subprocess.run(f"cat shield_badges.txt | grep '{shield_name}' | head -n 1", shell=True, stdout=subprocess.PIPE, text=True)
        built_with_badges.append(res2.stdout.strip())
        done = input("Are you done? [y/n]: ")
        if done.lower() == 'y':
            break

    data["built_with_badges"] = built_with_badges

    return data

data = {
    "user_name": "",
    "author_name": "",
    "author_email": "",
    "repo_name": "",
    "project_name": "",
    "project_tagline": "",
    "project_description": "",
    "logo_location": "",
    "demo_media_location": "",
    "installation_steps": "",
    "contributing_steps": "",
    "license_information": "",
    "acknowledgements": "",
    "built_with_badges": []
}

### Main Program
repo_name = input("Repository Name: ")

# Check if readme information file exists
try:
    f = open (f"{repo_name}.json", "r")
    s = f.read()

    if s != "":
        print(f"{repo_name}.json already exists. If you'd like to edit values, please edit that file directly.\nIf you want to regenerate the file, please delete the existing one first.\nPress ENTER to continue.")
        input()
        data = json.loads(s)
    # no data exists for this project
    else:
        data = collect_data(repo_name)
except Exception as e:
    print(f"Could not load existing data, proceeding to collect new data | {repr(e)}")
    data = collect_data(repo_name)

# Logic
if data["user_name"] == "": 
    data["user_name"] = "m-GDEV"
if data["author_name"] == "":
    data["author_name"] = "Musa Ahmed"
if data["author_email"] == "":
    data["author_email"] = "musaa.ahmed7@gmail.com"

# Save Data 
with open(f"{repo_name}.json", "w") as write:
    json.dump(data, write, indent=4)

# README template
readme_template = f"""
<!-- https://github.com/othneildrew/Best-README-Template -->

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/{data["user_name"]}/{data["repo_name"]})
[![Contributors](https://img.shields.io/github/contributors/{data["user_name"]}/{data["repo_name"]}.svg)](https://github.com/{data["user_name"]}/{data["repo_name"]}/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/{data["user_name"]}/{data["repo_name"]}.svg?style=flat)](https://github.com/{data["user_name"]}/{data["repo_name"]}/network/members)
![GitHub Repo stars](https://img.shields.io/github/stars/{data["user_name"]}/{data["repo_name"]}?style=flat&link=https%3A%2F%2Fgithub.com%2F{data["user_name"]}%2F{data["repo_name"]}%2Fstargazers)
[![Issues](https://img.shields.io/github/issues/{data["user_name"]}/{data["repo_name"]}.svg)](https://github.com/{data["user_name"]}/{data["repo_name"]}/issues)
[![MIT License](https://img.shields.io/github/license/{data["user_name"]}/{data["repo_name"]}.svg)](https://github.com/{data["user_name"]}/{data["repo_name"]}/blob/master/LICENSE.txt)

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/{data["user_name"]}/{data["repo_name"]}">
    <img src="{data["logo_location"]}" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">{data["project_name"]}</h3>

  <p align="center">
    {data["project_tagline"]}
    <br />

</div>

<!-- TABLE OF CONTENTS -->
# Links
* [About The Project](#about-the-project)
* [Built With](#built-with)
* [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
# About The Project

{data["project_description"]}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

![Demo]({data["demo_media_location"]})

## Built With

{"".join([f'![]({badge}) ' for badge in data["built_with_badges"]])}

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
# Installation

{data["installation_steps"]}

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
# Contributing

{data["contributing_steps"] or """
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project on Github
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request on Github
 """}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Top contributors:

<a href="https://github.com/{data["user_name"]}/{data["repo_name"]}/graphs/contributors">
  <img src="https://contrib.rocks/image?repo={data["user_name"]}/{data["repo_name"]}" alt="contrib.rocks image" />
</a>


<!-- LICENSE -->
# License

{data["license_information"]}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
# Contact

{data["author_name"]} - [{data["author_email"]}](mailto:{data["author_email"]})

Project Link: [https://github.com/{data["user_name"]}/{data["repo_name"]}](https://github.com/{data["user_name"]}/{data["repo_name"]})

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
# Acknowledgments

* [Best-README-Template: for this cool template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
"""

with open(f"{repo_name}.md", "w") as f:
    f.write(readme_template)

print(f"{repo_name}.md written sucessfully!")




