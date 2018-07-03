# Programmable-Web-Query-System
Parsed two text files api.txt and mashup.txt using python and created two json files respectively.
Created a MongoDB database to store API and MASHUP JSON data.
Developed a web based query system using Python's Flask framework and angularJS

## Prerequisites

There are not many prerequisites required to build and run this project, but you'll need the following:
* Python3
* MongoDB

## Steps to run the Project

### Clone The GitHub Repository
  ```bash
  $ git clone https://github.com/ck4957/Programmable-Web-Query-System
  ```
  Navigate into it using your Terminal (Mac & Linux) or Command Prompt (Windows)
  ```
  $ cd Programmable-Web-Query-System
  ```
  Folder Structure is as follows:
  ```
  |__
	|__static
		|__css
		|__fonts
		|__js
	|__templates
		|__index.html
	|__app.py
  ```


Install the MongoDB

Import the two JSON files 

1. **apiJson.json** - API Dataset
2. **mashupJson.json** - Mashup Dataset

using mongoimport commands

```
C:\{MongoDB Folder Path}\bin>import --db (dbname) --collection (collectionname) --file (filename with path) --jsonArray
```
Start the MongoDB server:
```
C:\{MongoDB Folder Path}\bin>mongod.exe
```
### Clone The GitHub Repository
  ```bash
  $ git clone https://github.com/ck4957/Programmable-Web-Query-System
  ```
  Navigate into it using your Terminal (Mac & Linux) or Command Prompt (Windows)
  ```
  $ cd Programmable-Web-Query-System
  ```
  Folder Structure is as follows:
  ```
  |__
	|__static
		|__css
		|__fonts
		|__js
	|__templates
		|__index.html
	|__app.py
  ```
Files: 
	Txt_to_Json.py // Program to parse the two text files and create two json file.


### Run the application using following command: 
```python
  python app.py
```
  This will the start localhost on port 5000. Go to browser and enter url: (http:\\localhost:5000)
