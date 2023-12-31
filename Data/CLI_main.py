#pylib
import os
import sys
import glob
import trace
import difflib
import inspect
import importlib.util
import traceback
from datetime import datetime
from PrintColor.Print_color import print_Color
#global vars>>>
#CONST SYS
CLI_NAME = '`CHANGE THE NAME`' # your CLI name
CLI_Ver = '0.00' # your CLI ver
directory = 'Data\modules'
#other global
imported_modules = {} #DO NOT CHANGE
command_mappings = {} #DO NOT CHANGE
CMLI_args = []
Debug_m = False
#Commands>>>
command_tuple = (
    'help', # help
    'debug', # Debug
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
#other>>>
python_files = glob.glob(os.path.join(directory, "*.py"))
#funcs(INTERNAL)>>> (DO NOT CHANGE)
#CLI_IM
def CLI_IM(CLII: bool = True):
    if CLII: print_Color('>>> ', ['green'], print_END='')  
    U_input = input('').lower()
    try:
        str_array = U_input.split()
        if str_array[0] in command_tuple:
            return str_array
        else:
            closest_match = difflib.get_close_matches(str_array[0], command_tuple, n=1)
            if closest_match:
                print_Color(f'~*ERROR: ~*Invalid input. you can use \'~*help~*\', did you mean \'~*{closest_match[0]}~*\'.', ['red', 'yellow', 'green', 'yellow', 'green', 'yellow'], advanced_mode=True)
            else:
                print_Color(f'~*ERROR: ~*Invalid input. you can use \'~*help~*\'.', ['red', 'yellow', 'green', 'yellow'], advanced_mode=True)
            return ['IIE']
    except IndexError:
        return ['IIE']
#IEH
def IEH(id: str = 'Unknown', stop: bool = True, DEV: bool = True):
    print_Color(f'~*ERROR: ~*Internal error info/id:\n~*{id}~*.', ['red', 'yellow', 'bg_red', 'yellow'], advanced_mode=True)   
    if DEV: 
        print_Color('~*Do you want to see the detailed error message? ~*[~*Y~*/~*n~*]: ',
                    ['yellow', 'normal', 'green', 'normal', 'red', 'normal'],
                    advanced_mode = True,
                    print_END='')
        show_detailed_error = input('')
        if show_detailed_error.lower() == 'y':
            print_Color('detailed error message:', ['yellow'])
            traceback.print_exc()
    if stop: sys.exit('SYS EXIT|ERROR: Internal|by Internal Error Handler')
#Debug
def Debug(ID, DEBUG_IF, SFL: bool = True, Force: bool = False, SFCS: bool = True):
    """
    This function is used for debugging purposes. It prints out various information about the data passed to it.

    Args:
        ID (Any): The identifier for the data. This could be any type, but is typically a string.
        DEBUG_IF (Any): The data that needs to be debugged. This could be any type.
        SFL (bool, optional): A flag to determine if the stack frame location should be included in the debug information. Defaults to True.
        Force (bool, optional): A flag to force the debug information to be printed even if the global Debug_m is set to False. Defaults to False.
        SFCS (bool, optional): A flag to determine if the function call stack should be included in the debug information. Defaults to True.

    Returns:
        None
    """
    try:
        if Debug_m or Force:
            frame_info = inspect.currentframe()
            stack_trace = traceback.format_stack()
            stack_trace_formated = ''
            for line in stack_trace[:-1]:
                stack_trace_formated += '--> [!>>>' + line 
            location = f'{inspect.stack()[1].filename}:{frame_info.f_back.f_lineno}' if SFL else f'L:{frame_info.f_back.f_lineno}'
            Debug_data = \
            f'\n~*--> ~*DEBUG INFO id: ~*[{str(ID)}]~*, ' \
            f'Location: ~*[{location}]~*, ' \
            f'time: ~*[{datetime.now().strftime("%Y/%m/%d | %H:%M:%S")}]\n~*--> ~*' \
            f'Data: ~*{str(DEBUG_IF)}\n~*--> ~*' \
            f'Data Type: ~*{type(DEBUG_IF)}\n~*--> ~*' \
            f'Memory Address: ~*DEC>>>~*{id(DEBUG_IF)}~* | HEX>>>~*{hex(id(DEBUG_IF))}~* | BIN>>>~*{bin(id(DEBUG_IF))}\n' 
            if SFCS:
                Debug_data += f'~*--> ~*Function Call Stack: ~*↓\n~*{stack_trace_formated}\n'
            print_Color(Debug_data,
            ['red', 'magenta', 'green', 'magenta', 'yellow', 'magenta', 'yellow',
            'red', 'magenta', 'yellow', 'red', 'magenta', 'yellow', 'red', 'magenta',
            'cyan', 'yellow', 'cyan', 'yellow', 'cyan', 'yellow', 'red', 'magenta', 'green', 'yellow'] if SFCS else \
            ['red', 'magenta', 'green', 'magenta', 'yellow', 'magenta', 'yellow',
            'red', 'magenta', 'yellow', 'red', 'magenta', 'yellow', 'red', 'magenta',
            'cyan', 'yellow', 'cyan', 'yellow', 'cyan', 'yellow'], 
            advanced_mode=True)
    except NameError:
        print_Color('~*[`Debug` func] --> ERROR: ~*carate a global var named `Debug_m` for turning on and off the Debug func.', ['red', 'yellow'], advanced_mode=True)
#load modules
def LCM():
    #Get Import List
    with open('Data\modules\modules.txt', 'r') as f:
        for line in f:
            parts = line.strip().split('~')
            filename, funcname, command = [part.strip() for part in parts[0].split(':')]
            args = [arg.strip() for arg in parts[1].split(',')] if len(parts) > 1 else []
            command_mappings[command] = (filename, funcname, args)
    #import
    for file in python_files:
        # Get the module name (without the .py extension)
        module_name = os.path.splitext(os.path.basename(file))[0]

        # Create a module spec
        spec = importlib.util.spec_from_file_location(module_name, file)

        # Create a module from the spec and add it to sys.modules
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Store the module in the dictionary
        imported_modules[module_name] = module
#main>>>
def main():
    #CLI loop
    while True: #WT
        #input manager
        input_array = CLI_IM()
        command = input_array[0]
        global CMLI_args
        global Debug_m
        try:
            CMLI_args = input_array[1:]
        except IndexError:
            CMLI_args = []
        if command in command_mappings:
            Debug('command_IC', command)
            Debug('command_mappings', command_mappings)
            Debug('CMLI_args', CMLI_args)
            Debug('imported_modules', imported_modules)
            filename, funcname, argnames = command_mappings[command]
            module_name = os.path.splitext(filename)[0]
            args = [globals()[argname] for argname in argnames]
            getattr(imported_modules[module_name], funcname)(*args)
        else:
            match command: #MI
                case 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(CLI_Info)
                case 'exit':
                    raise KeyboardInterrupt
                case 'debug':
                    print('Debug mode is ON...')
                    Debug_m = True
                case _:
                    # IEH(id = 'F[main],L1[WT],L2[MI],Error[nothing matched]', stop = False, DEV = False)
                    pass
#start>>>
if __name__ == '__main__':
    #clear the 'start L1' prompt
    print('                  ', end='\r')
    #Start INFO
    VER = f'V{CLI_Ver}' + datetime.now().strftime(" CDT(%Y/%m/%d | %H:%M:%S)")
    #CLI_Info
    CLI_Info = f'{CLI_NAME} Ver: {VER} \nPython Ver: {sys.version} \nType \'help\' for more information.'
    print(CLI_Info)
    #start main
    try:
        try:
            LCM()
            main()
        except (EOFError, KeyboardInterrupt):
            pass
    except Exception as e:
        IEH(id=f'F[SYS],RF[main],Error[{e}]', DEV=True)
    else:
        print_Color(f'\n~*[{CLI_NAME} CLI] ~*closed.', ['yellow', 'red'], advanced_mode=True)
#end(EOF) 