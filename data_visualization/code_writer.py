from utils import prompt_gpt, response_to_text

def import_libs() -> str:
    """
    code for importing libraries 
    """
    output = ""
    output += "import numpy as np\n"
    output += "import pandas as pd\n"
    output += "import matplotlib.pyplot as plt\n"
    return output 

def read_csv(file_path = "file.csv") -> str:
    """
    code for reading a csv file using pandas
    file_path: str, the path to the csv file
    """
    output = ""
    output += "df = pd.read_csv('file.csv')\n"
    output += "print(df.head())\n"
    return output

def plot(type, x_var, y_var, x_label = "X axis", y_label = "Y axis", title = "Scatter Plot", indent = 0, 
                 x_min = "None", x_max = "None", y_min = "None", y_max = "None", 
                 background = "white", text_color = "balck", font_size = '30', 
                 save_fig = False, save_path = "scatter_plot.png", transparent = False) -> str:
    """
    code for plotting a scatter plot using matplotlib
    type: str, the type of plot (e.g., 'scatter', 'line', 'bar')
    x_var: str, the variable for the x axis
    y_var: str, the variable for the y axis
    x_label: str, the label for the x axis
    y_label: str, the label for the y axis
    title: str, the title of the plot
    indent: int, the number of indents to add to the code
    x_min: str, the minimum value for the x axis
    x_max: str, the maximum value for the x axis
    y_min: str, the minimum value for the y axis
    y_max: str, the maximum value for the y axis
    background: str, the background color of the plot
    text_color: str, the color of the text in the plot
    font_size: str, the font size of the text in the plot
    save_fig: bool, whether to save the figure
    save_path: str, the path to save the figure
    transparent: bool, whether to save the figure with a transparent background
    """
    output = ""
    output += indent * "    " + "plt."+type+"("+x_var+", "+y_var+")\n"
    output += indent * "    " + "plt.xlabel('" + x_label + "')\n"
    output += indent * "    " + "plt.ylabel('" + y_label + "')\n"
    output += indent * "    " + "plt.title('" + title + "')\n"

    output += indent * "    " + "ax = plt.gca()\n"
    output += indent * "    " + "ax.set_xlim(["+x_min+", "+x_max+"])\n"
    output += indent * "    " + "ax.set_ylim(["+y_min+", "+y_max+"])\n"
    output += indent * "    " + "ax.set_facecolor('"+background+"')\n"
    output += indent * "    " + "ax.spines['bottom'].set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.spines['left'].set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.spines['top'].set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.spines['right'].set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.xaxis.label.set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.yaxis.label.set_color('"+text_color+"')\n"
    output += indent * "    " + "ax.title.set_color('"+text_color+"')\n"
    output += indent * "    " + "plt.xticks(color='"+text_color+"', fontsize="+font_size+")\n"
    output += indent * "    " + "plt.yticks(color='"+text_color+"', fontsize="+font_size+")\n"
    
    if save_fig:
        output += indent * "    " + "plt.savefig('"+save_path+"', transparent="+str(transparent)+")\n"
    output += indent * "    " + "plt.show()\n"
    return output

def main():
    """
    main function for the code writer
    It takes user input and generates code using the above functions
    """
    print("Welcome to the code writer! ")
    print("You can use the following commands:")
    print("import_libs()")
    print("read_csv(file_path)")
    print("plot(type, x_var, y_var, x_label, y_label, title, indent, x_min, x_max, y_min, y_max, background, text_color, font_size, save_fig, save_path, transparent)")
    code = ""
    while True:
        command = input()
        if command == "end":
            print(code)
            break
        else:
            command = response_to_text(prompt_gpt(command))
            result = eval(command)
            code += result + "\n"



if __name__ == "__main__":
    main()