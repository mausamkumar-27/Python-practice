'''player_score=100
def add_bonus():
    global player_score
    player_score +=50
    print("Score inside function after bonus:",player_score)
add_bonus()
print("Score outside function:",player_score)'''


daily_limit=10000
def check_limit():
    print("Current Limit:",daily_limit)
def update_limit(new_limit):
    global daily_limit
    daily_limit=new_limit
    print("Limit updated inside function:",new_limit)
    print(" Dekho Limit updated inside function:",daily_limit)
check_limit()
update_limit(25000)
check_limit()
print("Limit outside functions:",daily_limit)