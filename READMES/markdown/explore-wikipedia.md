
<!-- https://github.com/othneildrew/Best-README-Template -->

<a id="readme-top"></a>

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/m-GDEV/explore-wikipedia)
[![Contributors](https://img.shields.io/github/contributors/m-GDEV/explore-wikipedia.svg)](https://github.com/m-GDEV/explore-wikipedia/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/m-GDEV/explore-wikipedia.svg?style=flat)](https://github.com/m-GDEV/explore-wikipedia/network/members)
![GitHub Repo stars](https://img.shields.io/github/stars/m-GDEV/explore-wikipedia?style=flat&link=https%3A%2F%2Fgithub.com%2Fm-GDEV%2Fexplore-wikipedia%2Fstargazers)
[![Issues](https://img.shields.io/github/issues/m-GDEV/explore-wikipedia.svg)](https://github.com/m-GDEV/explore-wikipedia/issues)
[![MIT License](https://img.shields.io/github/license/m-GDEV/explore-wikipedia.svg)](https://github.com/m-GDEV/explore-wikipedia/blob/master/LICENSE.txt)

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/m-GDEV/explore-wikipedia">
    <img src="./docs/logo.jpg" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Explore Wikipedia</h3>

  <p align="center">
    Ever wanted to explore the links between wikipedia pages and maybe even find paths between pages?
    <br />

</div>

<!-- TABLE OF CONTENTS -->
#### Table of Contents
* [About The Project](#about-the-project)
    * [Why I Created This Project](#why-i-created-this-project)
    * [Features](#features)
    * [Technologies Used](#technologies-used)
* [Development]
    * [Installation](#installation)
    * [Folder Structure](#folder-structure)
    * [Contributing](#contributing)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [License](#license)

<!-- ABOUT THE PROJECT -->
## About The Project

Explore Wikipedia allows you to simply explore the links between pages on wikipedia and visualize the paths between them.


<div align="center">
    <img alt="Demo Video" src="./docs/explore-wikipedia.gif" />
</div>

### Why I Created This Project
I created this proejct shortly after learning  taking a data structures course. We learned about graphs, trees, traversal, and DFS and BFS algorithms. After learning about this I immediately connected it to [The Wiki Game](https://www.thewikigame.com/): a game that places you at a certain page and asks you to find your way to the given target page. I created this project so that I could do just that and visualize the results as well. The python script `build_graph.py` can actually 'play' this game perfectly. Given a starting page and a target page, it will use a DFS to explore all wikipedia pages until it eventually finds the target page. It actually works pretty well for pages that are highly related but as soon as you put in pdifferent pages, it will get completely 'lost' and take forever to find the target (mostly because wikipedia has so many pages lol). The frontend simply looks at pre-generated data and allows you to visualize how individual pages connect to each other. This is one of my favourite projects because it is genuinely so cool to see the links between pages and the weird and unexpected links you can find between something like the page "B Programming Language" and "Gary Kasparov" (former world chess champion).

### Features
* Solve any problem from [The Wiki Game](https://www.thewikigame.com/)
* Find a path between any two pages on Wikipedia
* Beautifully visualize the path between two pages


### Technologies Used 
<img src="https://img.shields.io/badge/-Cytoscape.js-F7DF1E?style=flat&logo=cytoscapedotjs&logoColor=white"/> <img src="https://img.shields.io/badge/-Nx-143055?style=flat&logo=nx&logoColor=white"/> <img src="https://img.shields.io/badge/-MicroPython-2B2728?style=flat&logo=micropython&logoColor=white"/> <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=white"/> <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white"/> <img src="https://img.shields.io/badge/-.ENV-ECD53F?style=flat&logo=dotenv&logoColor=white"/> 


## Development

### Installation
* Create a python virtual environment with `python3 -m venv ./env`
* Activate the environment: `source ./env/bin/activate`
* Run `src/build_graph.py` and input the names of the source and target wikipedia pages
* You can now look at the generated graph here: `build/converted.js`. This file has the graph converted from `nx` format (what python ses) to `cytoscape` which is what the frontend JavaScript uses.
* Run `npm install` to install all frontend packages
* Run `npm run dev` to run the frontend
* Go to `http://localhost:5173` and view the cool visualization :)


### Folder Structure


### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project on Github
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request on Github
 

### Top contributors:

<a href="https://github.com/m-GDEV/explore-wikipedia/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=m-GDEV/explore-wikipedia" alt="contrib.rocks image" />
</a>

<!-- CONTACT -->
## Contact
Musa Ahmed - [musaa.ahmed7@gmail.com](mailto:musaa.ahmed7@gmail.com)

Project Link: [https://github.com/m-GDEV/explore-wikipedia](https://github.com/m-GDEV/explore-wikipedia)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template: for this cool template](https://github.com/othneildrew/Best-README-Template)
* [The Wiki Game was a major inspiration for this project](https://www.thewikigame.com/)


<!-- LICENSE -->
## License

Distributed under the GPL 3.0 License. See LICENSE for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<sup>README version 1.0</sup>
