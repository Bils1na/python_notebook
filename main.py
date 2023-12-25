from functionallity import Functionallity as func


if __name__ == '__main__':

    is_active = True
    controller = func()
    controller.ui.mainloop()

    while is_active:
        print("""If you want to make a new note, you shall enter - '1'
For printing all notes enter - '2'
If you want to exit then enter - '0'\n""")
        command = input("Choose command >> ")
        if command == "1":
            note_text = input("Enter your new note >> ")
            controller.notebook.add(note_text)
        if command == "2":
            for val in controller.notebook.notebook:
                print(val.get_text())
        if command == "0":
            is_active = False
