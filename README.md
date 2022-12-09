# We sell elite wine

Website of a store selling wines and other beverages.

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson_1_We_sell_elite_wine_Layout_for_the_pitonist_Devman](https://github.com/VAChess777/Lesson_1_We_sell_elite_wine_Layout_for_the_pitonist_Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777/Lesson_1_We_sell_elite_wine_Layout_for_the_pitonist_Devman[requirements.txt](..%2FLesson_3_Hacking_the_electronic_diary_Getting_to_know_Django_ORM_Devman%2Frequirements.txt)
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

In the program `main.py ` there are environment variables.
Create a `.env` file, place it in the root directory of the program. Put the following data in the `.env` file in the `key=value` format.
                                                               
`EXCEL_FILE=` - The name of the `excel file` that contains the store's product range. By default, the project has a file `wine.xlsx `.             
`OPENING_WINERY_YEAR=` - Date of opening of the winery.              

### How to run the program:

Enter the command in console: `$ python main.py`. 


### How the program works:

The program contains scripts:

```main.py``` - the main program.  
        
The program contains a ready-made template for a website for the sale of wines:

`template.html` - Template for a website selling wines.

### Features works of the program:

The `main.py` program contains the functions:

* The `get_years` function - calculates the difference between the store opening and the present time.
Also returns the correct meaning of the word `год`, `года`, `лет`, in Russian, depending on the above difference in years.
* The `get_goods` function - retrieves all product information from the `excel file`. Brings this data to the required form for display on the site page.
* The `render_page` function - makes the necessary changes to the website template.
* The `main` function - main function.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).