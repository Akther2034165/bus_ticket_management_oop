#but ticket booking system

#__Admin__#
# adds a new buss
# check availabe buses
# check bus info

#__User__# 
# check availabe buses
# can check bus info
# can reserves a particular seat


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_dest,to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_dest = from_dest
        self.to = to
        self.seat = ["Empty" for i in range(20)]
    

# b = Bus(2,"Rahim","12PM","1PM","Dhaka","Ctg")
# print(vars(b))

class Phitron:
    total_bus = 5
    total_bus_list = []
    def add_bus(self):
        bus_no = int(input("ENTER BUS NO. : "))
        flag = 1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print('Bus already added!')
                flag = 0
                break
        if flag:
            bus_driver = input("ENTER BUS DRIVER NAME : ")
            bus_arrival = input("ENTER BUS ARRIVAL TIME : ")
            bus_departure = input("ENTER BUS DEPARTURE TIME : ")
            bus_from = input("ENTER BUS STARTS FROM : ")
            bus_to = input("ENTER BUS DESTITAION : ")
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\nNew Bus added successfully! ")

# company = Phitron()
# company.add_bus()


class Counter(Phitron):
    user_list = []
    def reservation(self):
        bus_no  = int(input("ENTER BUS NO : "))
        
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger = input("ENTER YOUR NAME : ")
                seat_no = int(input("ENTER SEAT NO : "))

                if seat_no > 20:
                    print("Opps! Seat not found")
                elif w['seat'][seat_no-1] != "Empty":
                    print("Seat already Booked")
                else:
                    w['seat'][seat_no-1] = passenger
            else:
                print("Opps! There is no bus availabe")
        # for bus in self.total_bus_list:
        #     print(bus['seat'])
    def show_ticket(self):
        bus_no = int(input("ENTER BUS NO. : "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print("*"*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"BUS NUMBER : {bus_no} \t\t\t DRIVER : {w['driver']}")
                print(f"ARRIVAL : {w['arrival']} \t\t\t DEPARTURE TIME : {w['departure']}\n FROM : {w['from_dest']} \t\t\t TO : {w['to']} ")

                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}",end = "\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}",end = "\t")
                        a+=1
                    print()
                print('*'*50)

    def get_user(self):
        return self.user_list

    def create_account(self):
        name = input("ENTER YOUR USERNAME : ")
        password = input("ENTER YOUR PASSWORD : ")
        self.new_user = User(name, password)
        self.user_list.append(vars(self.new_user))
    
    def availabe_buses(self):
        if len(self.total_bus_list) == 0:
            print("Opps! No Buses Availabe")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"BUS NUMBER : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"ARRIVAL : {bus['arrival']} \t DEPARTURE TIME : {bus['departure']}\n FROM : \t{bus['from_dest']} TO : \t {bus['to']}")
            print('*'*50)

# ___Global___
# Create An Account 
# Login to Your Account
# Exit 
#     __USER__
#        1.Bus info
#        2.Reservation / book ticket
#        3.Availabe Buses 
#        4.Exit

#     __ADMIN__
#        1.Add Bus
#        2.Availabe Buses
#        3.Can check bus info
#        4.Exit

while True:
    company = Phitron()
    b = Counter()
    print("1. CREATE AN ACCOUNT\n2. LOGIN TO YOU ACCOUNT\n3. EXIT")
    user_input = int(input("ENTER YOUR CHOICE : "))

    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("ENTER YOUR USERNAME : ")
        password = input("ENTER YOUR PASSWORD : ")

        flag = 0
        isAdmin = False

        if name == "Admin" and password == "123":
            isAdmin = True

        if isAdmin == False:
            for user in b.get_user():
                if user['username'] ==  name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10} WELCOME TO BUS TICKET BOOKING SYSTEM")
                    print("1. AVAILABLE BUSES\n2. SHOW BUS INFO \n3. RESERVATION\n4. EXIT")

                    a = int(input("ENTER YOUR CHOICE : "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.availabe_buses()
                    elif a == 2:
                        b.show_ticket()
                    elif a == 3:
                        b.reservation()
            else:
                print("Opps! NO USERNAME FOUND")
        else:
            while True:
                 print(f"\n{' '*10} WELCOME TO BUS TICKET BOOKING SYSTEM ADMIN PANNEL")
                 print("1. ADD BUS\n2. AVAILABLE BUSES \n3. SHOW BUS INFO\n4. EXIT")
                 a = int(input("ENTER YOUR CHOICE : "))
                 if a == 4:
                    break
                 elif a == 1:
                    b.add_bus()
                 elif a == 2:
                    b.availabe_buses()
                 elif a == 3:
                    b.show_ticket()

