# cp2k-syntax
Comprehensive syntax highlighting for [CP2K](https://www.cp2k.org/ "CP2K Project") input files in Sublime Text 3. CP2K is a freely available program package to perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.

## Features
* Syntax highlighting based on the `.sublime-syntax` format requiring a recent version of Sublime Text 3 (minimum build number 3084)
* Standalone python linter which parses the input file and compares it to the [XML input description](https://www.cp2k.org/howto:generate_manual?s[]=xml "Instructions for generating the XML input description") of CP2K
	* a sample XML file `sample-xml/cp2k_input.xml` is provided for CP2K version `x.x`
* Snippets for commonly used control sequences

## Installation

This

### Package Control
1. If not already installed, install [Package Control](https://packagecontrol.io/installation "Package Control installation instructions") for Sublime Text 3.
2. Install [SublimeLinter](http://www.sublimelinter.com/en/latest/installation.html "SublimeLinter installation instructions").
3. Install this package via Package Control
	1. Open the Command Palette (`ctrl+shift+p` on Linux)
	2. Type `install` and select `Package Control: Install Package`
	3. Type `cp2k` and select `cp2k-syntax`


## Usage and configuration

## Contributing

Pull requests are welcomed. Check the issue tracker for known issues and nice-to-have unimplented features.