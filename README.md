# cp2k-syntax
Comprehensive syntax highlighting for [CP2K](https://www.cp2k.org/ "CP2K Project") input files in Sublime Text 3. CP2K is a freely available program package to perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.

## Features
* Syntax highlighting based on the `.sublime-syntax` format requiring a recent version of Sublime Text 3 (minimum build number 3084)
* Standalone python linter which parses the input file and compares it to the [XML input description](https://www.cp2k.org/howto:generate_manual?s[]=xml "Instructions for generating the XML input description") of CP2K
	* a sample XML file `sample-xml/cp2k_input.xml` is provided for CP2K version `x.x`
* Snippets for commonly used control sequences

## Installation

The simplest way to install this package is via [Package Control](https://packagecontrol.io/ "Sublime Text Package Control"). Alternatively, you can clone this repository.

#### Installation via Package Control
1. Make sure you have a working python interpreter (supported versions `=>2.5` and `3.x`).
2. If not already installed, install [Package Control](https://packagecontrol.io/installation "Package Control installation instructions") for Sublime Text 3.
3. Install [SublimeLinter](http://www.sublimelinter.com/en/latest/installation.html "SublimeLinter installation instructions").
4. Install this package via Package Control
	1. Open the Command Palette (`ctrl+shift+p` on Linux/Windows)
	2. Type `install` and select `Package Control: Install Package`
	3. Type `cp2k` and select `cp2k-syntax`

#### Installation via Git
1. Make sure you have all the prerequisites listed above.
2. Open a terminal and create a working directory for this repository.
3. Move to the directory you created in the previous step and clone the repository `git clone https://github.com/nholmber/cp2k-syntax`
4. Create a folder for this package in your local Sublime Text [`Packages/User` directory](http://docs.sublimetext.info/en/latest/basic_concepts.html? "Instructions for finding")
5. Recursively copy (`cp -r *`) all files related to this package into the folder you created in the previous step. 

## Usage and configuration

## Contributing

Pull requests are welcomed. Check the issue tracker for known issues and nice-to-have unimplented features.