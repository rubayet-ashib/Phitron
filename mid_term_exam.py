# creating a class named "Star_Cinema"
class Star_Cinema:
    __hall_list = []

    def entry_hall(self, obj):
        self.__hall_list.append(obj)

# creating a class named "Hall" inherited from Star_Cinema
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        item = (id, movie_name, time)
        self.__show_list.append(item)

        # initializing all seats
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, id, lst):
        # Check if the show exists in seats
        if id not in self.__seats:
            print(f"Show ID : {id} does not exist.")
            return
        
        # booking seats
        for tup in lst:
            r, c = tup
            # handling invalid seats
            if(r > self.__rows) or (r < 1) or (c > self.__cols) or (c < 1):
                print("Invalid seat. Try again!")
                return
            # handling already booked seats
            if (self.__seats[id][r-1][c-1] == 1):
                print(f"The seat is already booked. Try again!")
                return
            
            self.__seats[id][r-1][c-1] = 1

    def view_show_list(self):
        for i in range(len(self.__show_list)):
            print(f"{i+1}. {self.__show_list[i][1]}, {self.__show_list[i][2]}")
    
    def view_available_seats(self, id):
        # check if the show exists in seats
        if id not in self.__seats:
            print(f"Show ID : {id} does not exist.")
            return
        
        for item in self.__seats[id]:
                print(item)


# Creating a class named "Counter", that will be initialized with a object of the class "Hall"
class Counter:
    def __init__(self, hall):
        self.hall = hall

    def view_show_list(self):
        self.hall.view_show_list()
    
    def view_available_seats(self, id):
        self.hall.view_available_seats(id)
    
    def book_seats(self, id, lst):
        self.hall.book_seats(id, lst)

# entry 2 movies for use
hall1 = Hall(5,5,"H1")
hall1.entry_show(111,"Avengers: Secret Wars (ID : 111)", "6:00 pm")
hall1.entry_show(222,"Mega Minions (ID : 222)", "9:00 pm")

# user interface
def show_menu():
    print("\nOptions : \n1. VIEW ALL SHOW TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET \n4. Exit\n")

    print("----------------")
    op = int(input("Enter option : "))
    print("----------------\n")

    if op == 1:
        hall1.view_show_list()
        show_menu()
    elif op == 2:
        id = int(input("Enter movie ID : "))
        hall1.view_available_seats(id)
        show_menu()
    elif op == 3:
        id = int(input("Enter movie ID : "))
        row = int(input("Enter row no. : "))
        col = int(input("Enter column no. : "))
        hall1.book_seats(id, [(row, col)])
        show_menu()
    elif op == 4:
        print("Exiting...")
    else:
        print("Invalid input. Try again!")
        show_menu()

# calling show_menu()
show_menu()