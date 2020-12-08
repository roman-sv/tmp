class EquipmentStorage:
    max_count_storage:int = 3 # максимальное количество оргтехники на складе
    equipment_list:list = []

    def storage(self, unit, for_department):
        tmp_dict = {'type': unit.eq_type, 'model': unit.model, 'price': unit.price, 'for_department': for_department}

        self.equipment_list.append(tmp_dict)

    def storage_info(self):
        print(f'Доступная техника на складе: ')
        for row in self.equipment_list:
            print(row)

    def transfer_equipment(self):
        for idx, row in enumerate(self.equipment_list):
            print(f'{row["type"]} {row["model"]} передан в/на {row["for_department"]}')

        self.equipment_list.clear()
        print(f'Количество техники на складе после передачи в подразделения: {len(self.equipment_list)}')

class Equipment:
    model: str = ''
    price: float = 0
    paper_num:int = 0 # количество бумаги


class Printer(Equipment):
    eq_type: str = 'принтер'
    cartridge_level: int = 100 # условно уровень картриджа в процентах
    text_to_print:str = ''

    def __init__(self, model:str, price:float, text_to_print:str, paper_num:int):
        self.model = model
        self.price = price
        self.text_to_print = text_to_print
        self.paper_num = paper_num

    def print(self):
        if self.cartridge_level < 3:
            print('Низкий уровень чернил')
        elif self.paper_num <= 0:
            print('Отсутствует бумага')
        else:
            print(self.text_to_print)


class Scanner(Equipment):
    eq_type: str = 'сканер'
    file_name:str = '' # имя файла
    ext_format:str = '' # расширение файла

    def __init__(self, model:str, price:float, file_name:str, ext_format:str, paper_num:int,):
        self.model = model
        self.price = price
        self.paper_num = paper_num
        self.file_name = file_name
        self.ext_format = ext_format

    def scan(self):
        if self.paper_num == 1:
            print(f'Документ сохранён в файле: {self.file_name}{self.ext_format}')
        else:
            print(f'Отсутствует документ для сканирования')


class Xerox(Equipment):
    eq_type:str = 'ксерокс'
    cartridge_level = 100 # условно уровень картриджа в процентах
    text_to_copy: str = ''

    def __init__(self, model:str, price:float, text_to_copy:str, paper_num:int):
        self.model = model
        self.price = price
        self.text_to_copy = text_to_copy
        self.paper_num = paper_num

    def print(self):
        if self.cartridge_level < 3:
            print('Низкий уровень тонера')
        elif self.paper_num <= 0:
            print('Отсутствует бумага')
        else:
            print(self.text_to_copy)

storage = EquipmentStorage()

while True:
    if len(storage.equipment_list) == storage.max_count_storage:
        print('Недостаточно места на складе!')
        break

    eq_type = input('Это принтер(printer)/сканер(scanner)/ксерокс(xerox)? ')
    model = input('Введите модель >> ')
    price = input('Введите цену >> ')

    if not price.isdigit():
        print('Цена должна содержать только цифры!')
        continue

    department = input('Для какого подразделения техника? ')
    quit = input('Продолжить ввод? y/n ')

    if eq_type == 'принтер' or eq_type =='printer':
        printer1 = Printer(model, float(price), 'Test_to_print', 1)
        storage.storage(printer1, department)
    elif eq_type == 'сканер' or eq_type =='scanner':
        scanner1 = Scanner(model, float(price), 'scan01', '.jpg', 1)
        storage.storage(scanner1, department)
    elif eq_type == 'ксерокс' or eq_type =='xerox':
        xerox1 = Xerox(model, float(price), 'test_to_copy', 5)
        storage.storage(xerox1, department)
    if quit == 'n':
        break

#printer1 = Printer('HP LaserJet Pro M15w', 9000, 'Test_to_print', 1)
#scanner1 = Scanner('HP ScanJet Pro 4500 FN', 7000, 'scan01', '.jpg', 1)
#xerox1 = Xerox('LaserJet Pro MFP M26A', 10000 ,'test_to_copy', 5)

storage.storage_info() # инфо по складу
storage.transfer_equipment() #передача техники в подразделения