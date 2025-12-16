import subprocess
import json

# Data types
class ReadmeData:
    def __init__(self):
        self.user_name: str = ""
        self.author_name: str = ""
        self.author_email: str = ""
        self.repo_name: str = ""
        self.project_name: str = ""
        self.project_tagline: str = ""
        self.project_description: str = ""
        self.why_i_created_this_project: str = ""
        self.features: list[str] = []
        self.logo_location: str = ""
        self.demo_media_location: str = ""
        self.installation_steps: list[str] = []
        self.contributing_steps: list[str] = []
        self.license_information: str = ""
        self.acknowledgements: list[str] = []
        self.built_with_badges: list[str] = []

    def init_with_dict(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            indent=4)

# Functions
def collect_list_data(prompt):
    print(f"Collecting List Data for {prompt}. Press enter on blank input to stop.")
    count = 0
    list_data = []
    while True:
       el = input(f"Element {count}: ")
       if el == "" or el.lower() == "done":
          break 
       list_data.append(el)
       count += 1

    return list_data

def collect_list_with_links_data(prompt):
    print(f"Collecting List With Links Data for {prompt}. Press enter on blank input to stop.")
    count = 0
    list_data: list[(str, str)] = []
    while True:
       el = input(f"Element Text {count}: ")
       link = input(f"Element Link {count}: ")
       if el == "" or el.lower() == "done":
          break 
       list_data.append((el, link))
       count += 1
    
    return list_data

def collect_data(repo_name):
    data = ReadmeData()
    # Info collection
    data.repo_name = repo_name
    data.user_name = input("Username (press ENTER for 'm-GDEV' default): ")
    data.author_name = input("Author Name (press ENTER for 'Musa Ahmed' default)")
    data.author_email = input("Author Email (press ENTER for 'musaa.ahmed7@gmail.com' default)")
    data.project_name = input("Project Name: ")
    data.project_tagline = input("Project Tagline: ")
    data.project_description = input("Project Description (in markdown): ")
    data.why_i_created_this_project = input("Why I created this project (in markdown): ")
    data.features = collect_list_data("Project Features (in markdown): ")
    data.logo_location = input("Logo path in project files: ")
    data.demo_media_location = input("Demo media location in project files (image or gif): ")
    data.installation_steps = collect_list_data("Installation Steps (in markdown): ")
    data.contributing_steps = collect_list_data("Contributing steps (leave blank to use default. in markdown): ")
    data.license_information = input("License Information (in markdown): ")
    data.acknowledgements = collect_list_with_links_data("Acknowledgments (in markdown): ")

    # built with
    built_with_badges = []
    input("Please select all technologies that you've used for this project now. Press ENTER to continue.")
    while True:
        print("Please select technologies used.")
        res = subprocess.run(f"cat {BASE_FOLDER}/shield_names.txt | fzf", shell=True, stdout=subprocess.PIPE, text=True) 
        shield_name = res.stdout.strip()
        res2 = subprocess.run(f"cat {BASE_FOLDER}/shield_badges.txt | grep '{shield_name}' | head -n 1", shell=True, stdout=subprocess.PIPE, text=True)
        built_with_badges.append(res2.stdout.strip())
        done = input(f"Last used: {res.stdout.strip()} | Are you done? [y/n]: ")
        if done.lower() == 'y':
            break

    data.built_with_badges = built_with_badges

    return data

# CONSTANTS
BASE_FOLDER = "./READMES"
MARKDOWN_FOLDER = BASE_FOLDER + "/markdown"
JSON_FOLDER = BASE_FOLDER + "/json"

### Main Program
data = ReadmeData()
repo_name = input("Repository Name: ")

# Check if readme information file exists
try:
    f = open (f"{JSON_FOLDER}/{repo_name}.json", "r")
    s = f.read()

    if s != "":
        print(f"\n!!! {repo_name}.json already exists. If you'd like to edit values, please edit that file directly.\nIf you want to regenerate the file, please delete the existing one first.\nPress ENTER to continue. !!!\n")
        input()
        res = json.loads(s)
        # object written as dict in JSON, re-convert to object
        data = ReadmeData()
        data.init_with_dict(res)
        
    # no data exists for this project
    else:
        # Save the JSON file so the user can easily edit if the script crashes
        with open(f"{JSON_FOLDER}/{repo_name}.json", "w") as f:
            f.write(data.toJSON())

        data = collect_data(repo_name)
except Exception as e:
    print(f"Could not load existing data, proceeding to collect new data | {repr(e)}")
    data = collect_data(repo_name)

# Logic
if data.user_name == "": 
    data.user_name = "m-GDEV"
if data.author_name == "":
    data.author_name = "Musa Ahmed"
if data.author_email == "":
    data.author_email = "musaa.ahmed7@gmail.com"

# Save Data 
with open(f"{JSON_FOLDER}/{repo_name}.json", "w") as f:
    f.write(data.toJSON())

# README template
readme_template = f"""
<!-- https://github.com/othneildrew/Best-README-Template -->

<a id="readme-top"></a>

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/{data.user_name}/{data.repo_name})
[![Contributors](https://img.shields.io/github/contributors/{data.user_name}/{data.repo_name}.svg)](https://github.com/{data.user_name}/{data.repo_name}/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/{data.user_name}/{data.repo_name}.svg?style=flat)](https://github.com/{data.user_name}/{data.repo_name}/network/members)
![GitHub Repo stars](https://img.shields.io/github/stars/{data.user_name}/{data.repo_name}?style=flat&link=https%3A%2F%2Fgithub.com%2F{data.user_name}%2F{data.repo_name}%2Fstargazers)
[![Issues](https://img.shields.io/github/issues/{data.user_name}/{data.repo_name}.svg)](https://github.com/{data.user_name}/{data.repo_name}/issues)
[![MIT License](https://img.shields.io/github/license/{data.user_name}/{data.repo_name}.svg)](https://github.com/{data.user_name}/{data.repo_name}/blob/master/LICENSE.txt)

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/{data.user_name}/{data.repo_name}">
    <img src="{data.logo_location}" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">{data.project_name}</h3>

  <p align="center">
    {data.project_tagline}
    <br />

</div>

<!-- TABLE OF CONTENTS -->
#### Table of Contents
* [About The Project](#about-the-project)
    * [Why I Created This Project](#why-i-created-this-project)
    * [Features](#features)
    * [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Contributing](#contributing)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [License](#license)

<!-- ABOUT THE PROJECT -->
## About The Project

{data.project_description}


<div align="center">
    <img alt="Demo Video" src="{data.demo_media_location}" />
</div>

### Why I Created This Project
{data.why_i_created_this_project}

### Features
{"".join([f'* {el}\n' for el in data.features])}

### Technologies Used 
{"".join([f'{badge} ' for badge in data.built_with_badges])}



<!-- GETTING STARTED -->
## Installation
{"".join([f'* {el}\n' for el in data.installation_steps])}

<!-- CONTRIBUTING -->
## Contributing
{"".join([f'* {el}\n' for el in data.contributing_steps]) or """
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project on Github
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request on Github
 """}

### Top contributors:

<a href="https://github.com/{data.user_name}/{data.repo_name}/graphs/contributors">
  <img src="https://contrib.rocks/image?repo={data.user_name}/{data.repo_name}" alt="contrib.rocks image" />
</a>

<!-- CONTACT -->
## Contact
{data.author_name} - [{data.author_email}](mailto:{data.author_email})

Project Link: [https://github.com/{data.user_name}/{data.repo_name}](https://github.com/{data.user_name}/{data.repo_name})

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template: for this cool template](https://github.com/othneildrew/Best-README-Template)
{"".join([f'* [{el[0]}]({el[1]})\n' for el in data.acknowledgements])}

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

{data.license_information}
"""

with open(f"{MARKDOWN_FOLDER}/{repo_name}.md", "w") as f:
    f.write(readme_template)

print(f"{repo_name}.md written sucessfully!")




