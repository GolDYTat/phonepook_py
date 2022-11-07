import view, model, os

def start():
    while True:
        print('')
        command = view.show_menu()
        match command:
            case '1': 
                os.system('CLS') 
                view.show_contacts(model.get_contacts())
            case '2':
                os.system('CLS') 
                model.read_file()
            case '0':
                os.system('CLS') 
                break
            case '3':
                os.system('CLS') 
                model.save_file()
            case '4': 
                os.system('CLS') 
                model.add_contact()
            case '5':
                os.system('CLS') 
                model.change_contact()
            case '6':
                os.system('CLS') 
                model.delete_contact()
            case '7': 
                # os.system('CLS') 
                model.search_contact()  