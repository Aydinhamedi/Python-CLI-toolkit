# Documentation for Python CLI Toolkit

>  **Warning**\
>  Please note that this code uses my print_color\
>  for more info go to https://github.com/Aydinhamedi/Python-color-print.

This Python CLI Toolkit is a powerful tool for creating command-line interfaces (CLI) with Python. It provides a framework for defining commands, handling user input, and managing modules. 

## Getting Started

To start using the toolkit, you need to modify the following sections of the code:\
(`Data/CLI_main.py`)

```python
#CONST SYS
CLI_NAME = '`CHANGE THE NAME`' # your CLI name
CLI_Ver = '0.00' # your CLI ver
directory = 'Data\modules'
#other global
imported_modules = {} #DO NOT CHANGE
command_mappings = {} #DO NOT CHANGE
CMLI_args = [] #DO NOT CHANGE
#Commands>>>
command_tuple = (
    'help', # help
    'exit', # Quit the CLI
    'clear' # Clear the CLI
)
cmd_descriptions = {
    'help': 'Show the help menu with the list of all available commands'
}
cmd_descriptions_other = {
    'exit': 'Quit the CLI',
    'clear': 'Clear the CLI'
}
```

- `CLI_NAME`: Replace '`CHANGE THE NAME`' with the name of your CLI.
- `CLI_Ver`: Replace '0.00' with the version of your CLI.
- `directory`: This is the directory where your modules will be stored. It is set to 'Data\modules' by default.
- `command_tuple`: This is a tuple containing the names of all available commands. Add your commands here.
- `cmd_descriptions` and `cmd_descriptions_other`: These are dictionaries that map command names to their descriptions. Add your command descriptions here.

## CLI.cmd

The toolkit includes a `CLI.cmd` file for managing and checking required packages and Python version. 

### Configuring `CLI.cmd`

Start by setting up the configuration to suit your needs. You can do this by modifying the following lines:

```bat
REM CONF
set CLI_NAME="CHANGE THE NAME" 
set python_min_VER=9
```

For example, if you want the minimum Python version to be 3.6.x and the CLI name to be "Test", you would change the lines to:

```bat
REM CONF
set CLI_NAME=Test
set python_min_VER=6 
```

### Setting up the Requirements File

Next, specify the Python packages your project requires in `Data\requirements.txt`. For example:

```requirements
numpy
keras
Pillow
```

## Adding Commands

To add a command, you need to create a Python file in the `Data\modules` directory and specify it in the `Data\modules\modules.txt` file.

### Creating a Python File

Create a Python file in the `Data\modules` directory. This file should contain a function that implements your command. For example, if you want to add a command that adds two numbers, you might create a file named `math_module.py` with the following content:

```python
def add(arg):
    result = int(arg[0]) + int(arg[1])
    print(f"The sum of {arg[0]} and {arg[1]} is {result}.")
```

In this function, `arg` is a list that contains the arguments passed to the command. The arguments are strings, so you need to convert them to integers before performing the addition.

### Specifying the Command in modules.txt

After creating the Python file, you need to specify it in the `Data\modules\modules.txt` file. The format for specifying a command is as follows:

```
THEFILENAME : THEFUNCNAME : the command to run it ~ arg
```

- `THEFILENAME`: This is the name of the Python file you created (without the .py extension).
- `THEFUNCNAME`: This is the name of the function in the Python file.
- `the command to run it`: This is the command that users will enter in the CLI to run the function.
- `arg`: This is the argument that the function takes. It should be a list containing the arguments passed to the command.\
    here is a list of global variables that you can use when adding your own modules to the Python CLI Toolkit:

    - `CLI_NAME`: This is the name of your CLI. You can change it to whatever you want.

    - `CLI_Ver`: This is the version of your CLI. You can change it to whatever you want.

    - `directory`: This is the directory where your modules will be stored. It is set to 'Data\modules' by default.

    - `imported_modules`: This is a dictionary that stores the imported modules. The keys are the module names and the values are the module objects.

    - `command_mappings`: This is a dictionary that maps command names to their corresponding functions. The keys are the command names and the values are tuples containing the filename, function name, and argument names.

    - `CMLI_args`: This is a list that contains the arguments passed to the command. The arguments are strings.

    - `command_tuple`: This is a tuple containing the names of all available commands. You can add your commands here.

    - `cmd_descriptions` and `cmd_descriptions_other`: These are dictionaries that map command names to their descriptions. You can add your command descriptions here.

    - `Debug`: This is a function that prints debug information. It is turned off by default, but you can turn it on by entering the `debug` command in the CLI.

    These global variables are used throughout the code to manage the CLI. You can use them in your modules to interact with the CLI. For example, you can use `CMLI_args` to access the arguments passed to your command, or `Debug` to print debug information.

For example, to specify the `add` command from the `math_module.py` file, you would add the following line to `modules.txt`:

```
math_module : add : add ~ CMLI_args
```

This means that users can run the `add` command by entering `add 20 10` in the CLI. The `CMLI_args` is a list that contains the arguments passed to the command. In this case, it would be `['20', '10']`.

Note: The `~` symbol is used to specify that a command takes arguments. If a command does not take any arguments, you can omit the `~` symbol.

## Help Function

A help function is already included in the toolkit. It is specified in `modules.txt` as follows:

```
CF_help : CI_help : help ~ cmd_descriptions , cmd_descriptions_other
```

This means that users can run the `help` command by entering `help` in the CLI. The `cmd_descriptions` and `cmd_descriptions_other` are dictionaries that contain the descriptions of all available commands.

## Running the CLI

After setting up your commands, you can run the CLI by executing the main Python file or CLI.cmd file (recommended). The CLI will start in an infinite loop, waiting for user input. Users can enter commands as specified in `modules.txt`. The CLI will execute the corresponding functions and display the results. Users can exit the CLI by entering the `exit` command.
