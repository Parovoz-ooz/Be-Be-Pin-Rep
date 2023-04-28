#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;


struct Contact {
    string name;
    string phone;
};


vector<Contact> contacts;


void addContact() {
    Contact contact;
    cout << "введите имя ";
    cin >> contact.name;
    cout << "введите номер телефона ";
    cin >> contact.phone;
    contacts.push_back(contact);
    cout << "контакт успешно добавлен\n";
}


void deleteContact() {
    string name;
    cout << "введите имя контакта для удаления ";
    cin >> name;
    auto it = find_if(contacts.begin(), contacts.end(),
        [&](const Contact& c) { return c.name == name; });
    if (it != contacts.end()) {
        contacts.erase(it);
        cout << "контакт успешно удален\n";
    }
    else {
        cout << "контакт не найден\n";
    }
}


void searchContacts() {
    string query;
    cout << "введите поисковый запрос ";
    cin >> query;
    for (const auto& contact : contacts) {
        if (contact.name.find(query) != string::npos ||
            contact.phone.find(query) != string::npos) {
            cout << contact.name << " " << contact.phone << endl;
        }
    }
}


void viewContacts() {
    for (const auto& contact : contacts) {
        cout << contact.name << " " << contact.phone << endl;
    }
}


void editContact() {
    string name;
    cout << "введите имя контакта для редактирования ";
    cin >> name;
    auto it = find_if(contacts.begin(), contacts.end(),
        [&](const Contact& c) { return c.name == name; });
    if (it != contacts.end()) {
        Contact& contact = *it;
        cout << "введите новое имя (" << contact.name << "): ";
        cin >> contact.name;
        cout << "введите новый номер телефона (" << contact.phone << "): ";
        cin >> contact.phone;
        cout << "контакт успешно отредактирован\n";
    }
    else {
        cout << "контакт не найден\n";
    }
}


int main() {
    setlocale(LC_ALL, "Russian");
    while (true) {
        cout << "меню:\n";
        cout << "1. добавить контакт\n";
        cout << "2. удалить контакт\n";
        cout << "3. поиск контактов\n";
        cout << "4. посмотреть контакты\n";
        cout << "5. изменить контакт\n";
        cout << "6. выход\n";
        int choice;
        cin >> choice;
        switch (choice) {
        case 1:
            addContact();
            break;
        case 2:
            deleteContact();
            break;
        case 3:
            searchContacts();
            break;
        case 4:
            viewContacts();
            break;
        case 5:
            editContact();
            break;
        case 6:
            return 0;
        default:
            cout << "неверный выбор\n";
            break;
        }
    }
}
