def create_record(name, telefon, address, ):
    """Создает рекорд"""
    record = {
        'name': name,
        'phone': telefon,
        'address': address
    }
    return record


user1 = create_record("Vasya", "899999999", "Tunis")
user2 = create_record("Misha", "999999", "Moscow")

print(user1)
print(user2)


def give_award(medal, *persons):  # Ставим *  если хотим несколько значений и он должен БЫТЬ В КОНЦЕ
    """Награждения медалями"""
    for person in persons:
        print("Награждается " + person.title() + " медалью " + medal)


give_award("За берлин", "Вася", "Петя")
