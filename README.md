Data Visualization Tool:-
    This project provides an interactive tool to visualize Sales, Profit, and Expenses data from a CSV file. With this tool, you can:
    •   Load a CSV file containing data on Sales, Profit, and Expenses.
    •   Visualize the data in a graphical format (Line plots).
    The tool uses a simple graphical user interface (GUI) built with tkinter, making it easy to use for anyone, even without coding experience.

Features:-
    •   Load CSV Files: Easily load a CSV file through a user-friendly file dialog.
    •   Data Visualization: Automatically generates line plots for Sales, Profit, and Expenses.
        o   Sales are plotted in blue.
        o   Profit is plotted in green.
        o   Expenses are plotted in red.

How to Use:-
    1. Run the GUI:
                    python cleab_gui.py
   

    2. Follow the steps:
        - Select a CSV file to clean.
        - Choose an option:
        - Drop rows with missing values.
        - Fill missing values with a specified value.
        - Specify a directory to save the cleaned file.

    3. View Results: The cleaned file will be saved in the selected directory.


Code Explanation:-
1. graph.py
    This file contains the core functions responsible for data loading and plotting the graphs.

    •   load(file): This function loads the data from the CSV file into a pandas DataFrame.
    •   sales(data): This function plots the Sales data from the CSV file.
    •   profit(data): This function plots the Profit data from the CSV file.
    •   expenses(data): This function plots the Expenses data from the CSV file.
    Each of these functions creates a line plot using matplotlib.

2. graph_gui.py
    This file contains the graphical user interface (GUI) built with tkinter.

    •   open_file(): Opens a file dialog that allows the user to select a CSV file. Once the file is selected, it calls the functions to plot Sales, Profit, and Expenses.
    •   main_gui(): Initializes the GUI, creates a label with instructions, and sets up a button to open the file dialog.
    
Example:-
    When you select a valid CSV file, you will see three different plots appear in the following order:

    •   Sales Plot: A line plot showing the Sales data over time (with the 'Index' column on the x-axis).
    •   Profit Plot: A line plot showing the Profit data.
    •   Expenses Plot: A line plot showing the Expenses data.
    Each plot will be displayed in a separate window.

Troubleshooting:-
    •   Error: "File not found": Make sure the CSV file exists at the specified location and is correctly formatted.
    •   Error: "Missing columns": Ensure the CSV file contains the necessary columns (Index, Sales, Profit, Expenses) to generate the plots.

This README is designed to help users easily understand how to set up and use the tool. Let me know if you'd like to make any further modifications!

This README is designed to help users easily understand how to set up and use the tool. Let me know if you'd like to make any further modifications!


Sample Images:-

![data_visualizer (1)](https://github.com/user-attachments/assets/f37e0ae0-4fce-46d2-9263-28a090dc3194)
![data_visualizer (2)](https://github.com/user-attachments/assets/d51d77d5-0f60-4d69-8a95-c981e19daf91)
![data_visualizer (3)](https://github.com/user-attachments/assets/000e64e4-f69a-4e28-bdb2-2c103c55777f)
![data_visualizer (4)](https://github.com/user-attachments/assets/6d0c4d4b-8296-4749-bdde-bcd614957bc2)




