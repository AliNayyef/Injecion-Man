from injection_man import sql_injection, xss

import time
import sys


def main():
    print('''
     ██╗███╗   ██╗     ██╗███████╗ ██████╗██╗ ██████╗ ███╗   ██╗      ███╗   ███╗ █████╗ ███╗   ██╗
     ██║████╗  ██║     ██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║      ████╗ ████║██╔══██╗████╗  ██║
     ██║██╔██╗ ██║     ██║█████╗  ██║     ██║██║   ██║██╔██╗ ██║█████╗██╔████╔██║███████║██╔██╗ ██║
     ██║██║╚██╗██║██   ██║██╔══╝  ██║     ██║██║   ██║██║╚██╗██║╚════╝██║╚██╔╝██║██╔══██║██║╚██╗██║
     ██║██║ ╚████║╚█████╔╝███████╗╚██████╗██║╚██████╔╝██║ ╚████║      ██║ ╚═╝ ██║██║  ██║██║ ╚████║
     ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                             
    ''')
    spinner = ["|", "/", "-", "\\"]
    progress_bar = "[                    ]"  # 20 spaces for 20 steps
    total_steps = 20

    def update_progress_bar(progress):
        filled_length = int(progress / total_steps * len(progress_bar.strip("[]")))
        return f"[{'=' * filled_length}{' ' * (len(progress_bar.strip('[]')) - filled_length)}]"

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write("Loading... Please wait:\n")

    for i in range(total_steps + 1):
        spinner_frame = spinner[i % len(spinner)]
        progress_bar = update_progress_bar(i)
        sys.stdout.write(f"\r{spinner_frame} {progress_bar} {int((i / total_steps) * 100)}%")
        sys.stdout.flush()
        time.sleep(0.2)

    print("\nTool for web-injection...")

    choose = int(input("1.XSS \n2.SQLI\nSelect Number: "))
    if choose == 1:
        target_url = input("Enter Targer URL : ")
        input_id = input("Enter Input Id : ")
        button_id = input("Enter Button Value : ")
        xss.xss(target_url, input_id, button_id)

    elif choose == 2:
        target_url = input("Enter Targer URL : ")
        sql_injection.sql_i(target_url)

    else:
        print("Wrong Selection")

if __name__ == "__main__":
    main()
