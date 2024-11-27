    Data Visualization Tool:-
       This project allows users to visualize data from a CSV file by selecting columns for the x-axis and multiple columns for the y-axis. The program plots line graphs based on the selected data columns using          Matplotlib and Tkinter for the GUI.
    
    Features:-
        •    Load CSV: Open any CSV file and load its data.
        •    Select Columns: Choose the columns to plot against each other (e.g., Date vs Sales, Profit vs Expenses).
        •    Plot Graphs: Generate line graphs for selected columns.
        •    Interactive GUI: Easy-to-use graphical interface to select data and plot graphs.
    
    
    How to Use:-
        1.Run the Program
            •   Execute the main Python script graph_gui.py to start the application. The GUI will open.
    
        2. Open CSV File
            •   Click Open CSV to open a file dialog and select the CSV file you want to visualize.
        3. Select Columns
            •   A new window will open where you can:
                o   Select the X-axis column from the dropdown menu.
                o   Select one or more Y-axis columns using checkboxes.
        4. Plot Graph
            •   After selecting the columns, click the Plot Graph button to generate the graph
    
    The application will automatically generate for features that you select.
    
    Code Explanation:-
        1.  graph.py: Contains the core logic for loading CSV files and plotting data.
            •   ld(f): Loads the CSV file.
            •   plt_d(d, x, y): Plots selected columns as graphs.
        2.  graph_gui.py: Implements the graphical user interface for selecting files and columns.
            •   op_f(): Opens the file dialog to load a CSV file.
            •   sel_col(d): Displays a column selection window for the user.
            •   gui(): Sets up the main window for the application.
        
    
    
    Troubleshooting:-
        •   Missing Dependencies: If you encounter errors related to missing modules (pandas, matplotlib, tkinter), ensure all required libraries are installed. Run pip install pandas matplotlib to install the necessary dependencies.

    •   File Not Found: If the program doesn't load your CSV file, ensure the file path is correct and that the file is accessible. Verify the file is in CSV format and contains the expected columns.

This README is designed to help users easily understand how to set up and use the tool. 

    Sample Images-

![visualize (1)](https://github.com/user-attachments/assets/a62a960e-246e-425a-a308-e1c2022f427e)

![visualize (2)](https://github.com/user-attachments/assets/63da4360-c9ae-4aec-9b2b-8b51e6cba1eb)

![visualize (3)](https://github.com/user-attachments/assets/52e72e58-a2b9-42dd-ae0c-146dc530da51)

![visualize (4)](https://github.com/user-attachments/assets/304d5161-3e66-4df2-9b8a-0e909bf9dd0f)





