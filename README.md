# Mapa Senderista Local (0.1)

This projects aims to be a repository that you can store locally that can help you visualize your hiking projects or the routes that you want to check out.

## Description

The most interesting thing about this project is that it lets you visualize all your routes (both the ones that you have done already and the one that you aim to do someday) in a single map. You can also edit them, turn the routes into different colours depending on whether you have already donde them, already planned when to do them or if you have already done them.

## Getting Started

### Dependencies

* `folium==0.14.0`
* `gpxpy==1.5.0`
* Ubuntu (may or may not work in other operating systems, I haven't tested it) 

### Installing

* `git clone https://github.com/marc-marcos/mapa-senderista-local` 
* Execute installing script: `./install.sh`
* `python3 createDatabase.py`

### Executing program

* To start the gui: `python3 index.py` 

## Help

Most problems I've countered have come from not having ran `regenerateRoutes.py` when modifying the folder structure.

## Authors

Contributors names and contact info

ex. [@marc-marcos](https://github.com/marc-marcos)

## Version History

Still no initial release.

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Roadmap

- 0.1 Version (next release)
    - [X] GUI to avoid having to deal with terminal usage.
    - [X] Installation via script.
- Future versions
    - [ ] More options to modify the database. 
    - [ ] Being able to add points arbitrarily besides adding gpx routes.
    - [ ] Link of the route in the popup.

## Acknowledgments


Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)