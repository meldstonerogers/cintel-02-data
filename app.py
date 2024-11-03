import plotly.express as px
from shiny.express import input, ui
from shiny import render
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
from shinyswatch import theme

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Melissa's Penguin Practice Data", fillable=True, theme=theme.morph)

# Add a Shiny UI sidebar for user interaction
# Use a with block to add content to the sidebar
with ui.sidebar(bg="#8fb597"):  
    ui.h2("Sidebar") # Use the ui.h2() function to add a 2nd level header to the sidebar    
    ui.hr(), # Use ui.hr() to add a horizontal rule to the sidebar 
#ADD ADDITIONAL ATTRIBUTES 


    # Use ui.input_selectize() to create a dropdown input to choose a column
    ui.input_selectize(  
        "selected_attribute",  
        "Select an option below:",  
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],  
    )  

    @render.text
    def select():
        return f"{input.selectize()}"
    
    # Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "Plotly Bin Count", 1, min=1, max=50)  

    @render.text
    def numeric():
        return input.numeric()

    # Use ui.input_slider() to create a slider input for the number of Seaborn bin
    (ui.input_slider("seaborn_bin_count", "Seaborn Bin Count", 1, 50, 25),)  

    @render.text
    def slider():
        return f"{input.slider()}"

    # Use ui.input_checkbox_group() to create a checkbox group input to filter the species
    ui.input_checkbox_group(  
        "selected_species_list",  
        "Select One or More Species:",
        choices=["Adelie", "Chinstrap", "Gentoo"],
        selected=["Adelie", "Chinstrap", "Gentoo"],
        inline=False 
    )  

    @render.text
    def value():
        return ", ".join(input.checkbox_group())

    # Use ui.a() to add a hyperlink to the sidebar
    ui.a("Melissa's GitHub", href="https://github.com/meldstonerogers", target="_blank") 

#Main Content 
#Data Table, showing all data
#Data Grid, showing all data

with ui.layout_columns():
    with ui.card(full_screen=True):
            ui.card_header("Data Table")
            
            @render.data_frame  
            def penguins_table():
                return render.DataTable(
                    penguins_df, selection_mode="row", width="400px", height="250px"
            )  

    with ui.card(full_screen=True):
            ui.card_header("Data Grid")
        
            @render.data_frame  
            def penguins_grid():
                return render.DataGrid(penguins_df) 

#Plotly Histogram, showing all species 
#Seaborn Histogram, showing all species 

#Plotly Scatterplot, showing all species 
#with ui.card(full_screen=True):

   # ui.card_header("Plotly Scatterplot: Species")

   # @render_plotly
   # def plotly_scatterplot():
        # Create a Plotly scatterplot using Plotly Express
        # Call px.scatter() function
        # Pass in six arguments:
