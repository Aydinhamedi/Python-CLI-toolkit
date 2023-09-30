from PrintColor.Print_color import print_Color
#CI_help
def CI_help(cmd_descriptions, cmd_descriptions_other, SSUH: bool = True, show_lines: bool = True): #change show_lines and SSUH to change the style
    #main
    if SSUH:
        print_Color(f'{("┌─ " if show_lines else "")}~*Main (you can run them in order for simple usage):', ['cyan'], advanced_mode=True)
        for i, (cmd, desc) in enumerate(cmd_descriptions.items(), start=1):
            if i == len(cmd_descriptions):
                print_Color(f'{("│  └─ " if show_lines else "")}~*{i}. {cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("│  ├─ " if show_lines else "")}~*{i}. {cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
        #other
        print_Color(f'{("└─ " if show_lines else "")}~*Other:', ['cyan'], advanced_mode=True)
        for i, (cmd_other, desc_other) in enumerate(cmd_descriptions_other.items(), start=1):
            if i == len(cmd_descriptions_other):
                print_Color(f'{("   └─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("   ├─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
    else:
        print_Color(f'~*commands:', ['cyan'], advanced_mode=True)
        #main
        for i, (cmd, desc) in enumerate(cmd_descriptions.items(), start=1):
            if i == len(cmd_descriptions):
                print_Color(f'{("└─ " if show_lines else "")}~*{cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("├─ " if show_lines else "")}~*{cmd}: ~*{desc}', ['yellow', 'normal'], advanced_mode=True)
        #others
        for i, (cmd_other, desc_other) in enumerate(cmd_descriptions_other.items(), start=1):
            if i == len(cmd_descriptions_other):
                print_Color(f'{("└─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)
            else:
                print_Color(f'{("├─ " if show_lines else "")}~*{cmd_other}: ~*{desc_other}', ['yellow', 'normal'], advanced_mode=True)